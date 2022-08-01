from rest_framework.test import APIClient

client = APIClient()


def test_example():
    response = client.get("/user/")
    assert response.data["user"] in ("I", "me", "myself")
