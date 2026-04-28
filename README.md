# 📄 AI Invoice Analyzer (AWS Textract + Bedrock)

## 🚀 Overview
This project extracts and analyzes invoice data using:
- Amazon Textract (OCR)
- Amazon Bedrock (LLM)
- Streamlit UI

## 🔁 Pipeline
PDF → S3 → Textract → Bedrock → JSON → UI

## 📂 Features
- Upload PDF invoices
- Extract structured data
- Save JSON output
- Clean UI display

## 🛠 Tech Stack
- Python
- Streamlit
- AWS Textract
- AWS Bedrock
- AWS S3

## ▶️ Run Locally
```bash
pip install -r requirements.txt
python3 -m streamlit run app.py