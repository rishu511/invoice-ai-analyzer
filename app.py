import streamlit as st
import json
import os
from textract_utils import extract_text_from_pdf
from bedrock_utils import analyze_invoice
import os

if not os.path.exists("uploads"):
    os.makedirs("uploads")

if not os.path.exists("outputs"):
    os.makedirs("outputs")

    
st.set_page_config(layout="wide")

st.title("📄 AI Invoice Analyzer")

# Create two columns
col1, col2 = st.columns(2)

# ---------------- LEFT PANEL ----------------
with col1:
    st.header("📥 Input")

    uploaded_file = st.file_uploader(
        "Upload Invoice (PDF)",
        type=["pdf"]
    )

    if uploaded_file:
        # Save input file
        if not os.path.exists("uploads"):
            os.makedirs("uploads")
        input_path = os.path.join("uploads", uploaded_file.name)

        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"Saved: {uploaded_file.name}")

        file_bytes = uploaded_file.read()

# ---------------- RIGHT PANEL ----------------
with col2:
    st.header("📤 Output")

    if uploaded_file:
        with st.spinner("🔍 Processing..."):

            # Textract
            text = extract_text_from_pdf(file_bytes, uploaded_file.name)

            # Bedrock
            data = analyze_invoice(text)

        st.success("✅ Extraction Complete")

        # Clean display (label : value)
        st.subheader("📊 Extracted Data")

        for key, value in data.items():
            st.write(f"**{key}** : {value}")

        # Save JSON output
        if not os.path.exists("outputs"):
            os.makedirs("outputs")
        output_path = os.path.join(
            "outputs",
            uploaded_file.name.replace(".pdf", ".json")
        )

        with open(output_path, "w") as f:
            json.dump(data, f, indent=4)

        st.success(f"Saved JSON → {output_path}")

        # Download button
        st.download_button(
            "⬇️ Download JSON",
            data=json.dumps(data, indent=4),
            file_name="output.json",
            mime="application/json"
        )