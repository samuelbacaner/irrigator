from datetime import datetime
from google.cloud import bigquery
from google.oauth2 import service_account

from src.utils import load_creds
from src.models import MoistureReading

DATASET_KEY = "irrigation"
SOIL_MOISTURE_TABLE_KEY = "soil_moisture"


credentials = service_account.Credentials.from_service_account_info(load_creds())
client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

# TODO create dataset and table if they don't already exist
def write_moisture_reading(moisture_reading: MoistureReading):
    dataset = client.get_dataset(DATASET_KEY)
    table_ref = dataset.table(SOIL_MOISTURE_TABLE_KEY)
    table = client.get_table(table_ref)
    rows = [moisture_reading.to_tuple()]
    client.insert_rows(table, rows)
