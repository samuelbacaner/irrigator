import os
import json
import base64

def load_creds() -> dict:
    creds_base64 = os.environ["SERVICE_ACCOUNT_CREDS"]
    return json.loads(base64.b64decode(creds_base64).decode("utf-8"))