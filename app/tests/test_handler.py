from app.handler import os, requests, show_rows


def test_db_exist() -> bool:
    """
    test db exists
    """
    assert os.path.exists("posts.db")


def test_db_data() -> bool:
    """
    test for response from db
    """
    data = show_rows()
    assert data


def test_api_response() -> bool:
    """
    test response from https://randomuser.me/
    """
    status_code = requests.get(f"https://randomuser.me/api/?results={10}").status_code
    assert status_code == 200
