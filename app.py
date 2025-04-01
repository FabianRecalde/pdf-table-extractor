
import streamlit as st
from io import BytesIO
import tempfile
from extract_function import extract_table_until_subtotal

st.title("📄 PDF Table Extractor")

uploaded_file = st.file_uploader("Subí tu archivo PDF", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        temp_pdf_path = temp_pdf.name

    output = BytesIO()
    output_excel_path = temp_pdf_path.replace(".pdf", ".xlsx")

    extract_table_until_subtotal(temp_pdf_path, output_excel_path)

    with open(output_excel_path, "rb") as f:
        output.write(f.read())
        output.seek(0)

    st.success("✅ Extracción completa. ¡Descargá tu archivo!")
    st.download_button(label="📥 Descargar Excel", data=output, file_name="resultado.xlsx")
