import boto3
import json
import os
import time

s3 = boto3.client("s3", region_name="us-east-1")
textract = boto3.client("textract", region_name="us-east-1")

BUCKET_NAME = "invoice-analyzer-bucket-1234"
OUTPUT_DIR = "outputs"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def extract_text_from_pdf(file_bytes, file_name):

    # 📤 Upload PDF to S3
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=file_bytes
    )

    # 🧠 Start Textract job
    response = textract.start_document_analysis(
        DocumentLocation={
            "S3Object": {
                "Bucket": BUCKET_NAME,
                "Name": file_name
            }
        },
        FeatureTypes=["FORMS", "TABLES"]
    )

    job_id = response["JobId"]

    # ⏳ Wait for completion
    while True:
        result = textract.get_document_analysis(JobId=job_id)
        status = result["JobStatus"]

        if status == "SUCCEEDED":
            break
        elif status == "FAILED":
            raise Exception("Textract job failed")

        time.sleep(2)

    # Save raw Textract response
    textract_output_path = os.path.join(OUTPUT_DIR, "textract.json")
    with open(textract_output_path, "w") as f:
        json.dump(result, f, indent=4)

    # 📄 Extract text
    text = ""
    for block in result["Blocks"]:
        if block["BlockType"] == "LINE":
            text += block["Text"] + "\n"

    return text