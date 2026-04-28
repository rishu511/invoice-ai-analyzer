<img width="1359" height="682" alt="image" src="https://github.com/user-attachments/assets/981c752e-f3eb-406b-b0cd-4fd77ec8a676" />

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
