import boto3
import json

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")


def analyze_invoice(text):

    prompt = f"""
    You are an invoice data extractor.
    Extract every relevant invoice field from the text below and return ONLY valid JSON.
    Use null for any field that is missing.

    Required fields and possible values:
    - invoice_number: string
    - invoice_date: date or string
    - due_date: date or string
    - vendor_name: string
    - vendor_address: string
    - vendor_phone: string
    - vendor_email: string
    - customer_name: string
    - customer_address: string
    - customer_phone: string
    - customer_email: string
    - purchase_order_number: string
    - payment_terms: string
    - currency: string (e.g. USD, EUR, GBP)
    - subtotal: number
    - tax_amount: number
    - discount_amount: number
    - shipping_amount: number
    - total_amount: number
    - balance_due: number
    - invoice_status: string (e.g. paid, unpaid, past due)
    - notes: string
    - line_items: array of objects with fields:
        - description: string
        - quantity: number
        - unit_price: number
        - total_price: number

    If a field is not present in the invoice, include it with a null value.
    Do not return any text outside the JSON object.

    Invoice text:
    {text}
    """

    body = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 500,
        "anthropic_version": "bedrock-2023-05-31"
    }

    response = bedrock.invoke_model(
        modelId="anthropic.claude-3-haiku-20240307-v1:0",
        body=json.dumps(body)
    )

    result = json.loads(response["body"].read())

    # extract actual text content
    output_text = result["content"][0]["text"]

    try:
        return json.loads(output_text)
    except:
        return {"raw_output": output_text}