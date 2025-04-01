
# 📄 PDF Table Extractor (Streamlit App)

This Streamlit app allows you to upload a PDF file that contains product tables and extract the data up to the **subtotal** line. The extracted table is converted into an Excel file that you can download with a single click.

---

## 🚀 Features

- ✅ Upload a PDF file with itemized product tables
- 📑 Automatically detects the correct table format (6 or 7 columns)
- 🔍 Stops reading at the word **"Subtotal"**
- 📥 Exports results to a clean Excel spreadsheet
- 💻 Runs entirely in your browser – no installation needed!

---

## 🛠 Technologies

- [Streamlit](https://streamlit.io/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

---

## 🧪 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/pdf-table-extractor.git
cd pdf-table-extractor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

---

## ☁️ Hosted on Streamlit Cloud

You can try the app live here:  
👉 [https://YOUR_USERNAME.streamlit.app](https://YOUR_USERNAME.streamlit.app) ← *(replace with your actual link)*

---

## 📂 File Structure

```
pdf-table-extractor/
│
├── app.py                  # Main Streamlit interface
├── extract_function.py     # PDF parsing and Excel writing logic
├── requirements.txt        # Dependencies
└── README.md               # This file
```

---

## 📬 Contact

Built with ❤️ by [YOUR NAME]  
🔗 GitHub: [https://github.com/YOUR_USERNAME](https://github.com/YOUR_USERNAME)
