import os


BASE_URL = os.getenv(
    "BASE_URL",
    "https://app.workflowpro.com"
)

API_URL = os.getenv(
    "API_URL",
    "https://app.workflowpro.com/api/v1"
)

BROWSER = os.getenv(
    "BROWSER",
    "chromium"
)
