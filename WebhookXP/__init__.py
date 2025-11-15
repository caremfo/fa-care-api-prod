import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("WebhookXP disparado.")

    try:
        data = req.get_json()
    except ValueError:
        data = {}

    logging.info(f"Payload recebido: {data}")

    # Exemplo: extrair a URL do relatório (caso venha)
    report_url = data.get("response", {}).get("url")

    return func.HttpResponse(
        json.dumps({
            "status": "ok",
            "report_url": report_url,
            "received": data
        }),
        status_code=200,
        mimetype="application/json"
    )
