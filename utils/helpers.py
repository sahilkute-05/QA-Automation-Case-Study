import uuid


def generate_project_name():

    return f"Automation-{uuid.uuid4().hex[:6]}"
