from utils.api_client import APIClient
from utils.config import API_URL


TOKEN = "sample_token"


def test_create_project():

    client = APIClient(API_URL, TOKEN)

    payload = {
        "name": "Automation Project"
    }

    response = client.post(
        "/projects",
        payload
    )

    assert response.status_code in [200, 201]
