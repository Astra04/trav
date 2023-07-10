import vertexai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.auth import credentials
from google.oauth2 import service_account
import google.cloud.aiplatform as aiplatform
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
import json
from vertexai.language_models import TextGenerationModel


# Update the values in the json file with your own
with open(
    "service_account.json"
) as f:  # replace 'serviceAccount.json' with the path to your file if necessary
    service_account_info = json.load(f)

my_credentials = service_account.Credentials.from_service_account_info(
    service_account_info
)


# Initialize Google AI Platform with project details and credentials
aiplatform.init(
    credentials=my_credentials,
)

with open("service_account.json", encoding="utf-8") as f:
    project_json = json.load(f)
    project_id = project_json["project_id"]


vertexai.init(project="ace-study-392208", location="us-central1")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 1024,
    "top_p": 0.8,
    "top_k": 1
}
model = TextGenerationModel.from_pretrained("text-bison@001")
response = model.predict(
    """What are some strategies for overcoming writer\'s block:""",
    **parameters
)
print(f"Response from Model: {response.text}")
