import requests
from fastapi import FastAPI
import json

app = FastAPI()

def applicant_detail_webhook_ping(applicant_detail):
    WEBHOOK_URL = 'https://hook.integromat.com/lq9179ib27rjp7febg1cute4jrkkees1'
    response = requests.post(WEBHOOK_URL, data=applicant_detail)
    return print(applicant_detail)

def project_creator_webhook_ping(project_creator_detail):
    WEBHOOK_URL = 'https://hook.integromat.com/yi6v4f5gpjhesbk3ollm6mx7fcgfvtru'
    response = requests.post(WEBHOOK_URL, data=project_creator_detail)
    return print(project_creator_detail)