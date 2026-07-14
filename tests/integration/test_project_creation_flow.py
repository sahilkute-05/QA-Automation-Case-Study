from utils.api_client import APIClient
from utils.helpers import generate_project_name
from utils.config import API_URL


TOKEN = "sample_token"


def test_project_creation_flow():

    client = APIClient(API_URL, TOKEN)

    project_name = generate_project_name()

    payload = {
        "name": project_name
    }

    response = client.post(
        "/projects",
        payload
    )

    assert response.status_code == 201
