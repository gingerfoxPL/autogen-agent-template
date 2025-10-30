import os
import requests

APP_MONITOR_ENDPOINT = os.getenv("APP_MONITOR_ENDPOINT")

def create_record(project_id: int):
    payload = {"project_id" : project_id}
    response = requests.post(
        url=APP_MONITOR_ENDPOINT,
        json=payload
    )   
    return response
