
import pdfplumber
import pandas as pd
import re

def extract_table_until_subtotal(pdf_path, output_excel_path):
    expected_headers_6_cols_a = ["Qty", "Manuf.", "Manuf #", "Description", "Unit Price", "Ext. Price"]
    expected_headers_6_cols_b = ["Qty", "Manuf.", "Manuf #", "Description", "Unit List Price", "Ext. Price"]
    expected_headers_7_cols = ["Qty", "Manuf.", "Manuf #", "Description", "Unit List Price", "Unit Price", "Ext. Price"]

    extracted_data = []
    start_extracting = False
    num_columns_detected = None
    detected_table_format = None
    header_config = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            lines = text.split("\n")

            for line_number, line in enumerate(lines, start=1):
                clean_line = re.sub(r'\s+', ' ', line).strip()

                if "Qty" in clean_line and "Manuf" in clean_line and "Manuf #" in clean_line:
                    line_no_dots = clean_line.replace('.', '')
                    if all(h.replace('.', '') in line_no_dots for h in expected_headers_7_cols):
                        detected_table_format = "7"
                        header_config = expected_headers_7_cols
                    elif all(h.replace('.', '') in line_no_dots for h in expected_headers_6_cols_a):
                        detected_table_format = "6a"
                        header_config = expected_headers_6_cols_a
                    elif all(h.replace('.', '') in line_no_dots for h in expected_headers_6_cols_b):
                        detected_table_format = "6b"
                        header_config = expected_headers_6_cols_b
                    else:
                        continue

                    start_extracting = True
                    num_columns_detected = len(header_config)
                    continue

                if re.search(r'\bsubtotal\b', clean_line, re.IGNORECASE):
                    if extracted_data:
                        df = pd.DataFrame(extracted_data)
                        df.columns = header_config
                        df.to_excel(output_excel_path, index=False)
                    return

                if start_extracting:
                    row_added = False

                    if detected_table_format in ["6a", "6b"]:
                        match = re.match(r'^(\d+)\s+([A-Za-z]+)\s+([A-Za-z0-9-]+)\s+(.+?)\s+(-?\$[\d,]+\.\d{2})\s+(-?\$[\d,]+\.\d{2})$', clean_line)
                        if match:
                            values = list(match.groups())
                            extracted_data.append(values)
                            row_added = True

                    elif detected_table_format == "7":
                        match = re.match(
                            r'^(\d+)\s+([A-Za-z]+)\s+([A-Za-z0-9-]+)\s+(.+?)\s+(-?\$[\d,]+\.\d{2})\s+(-?\$[\d,]+\.\d{2})\s+(-?\$[\d,]+\.\d{2})$',
                            clean_line)
                        if match:
                            values = list(match.groups())
                            extracted_data.append(values)
                            row_added = True

                    if not row_added:
                        filler_row = [clean_line] + [""] * (len(header_config) - 1)
                        extracted_data.append(filler_row)

    if extracted_data:
        df = pd.DataFrame(extracted_data)
        df.columns = header_config
        df.to_excel(output_excel_path, index=False)
