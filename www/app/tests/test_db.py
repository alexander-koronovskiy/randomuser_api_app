from app.handler import db, show_rows


def test_data():
    """
    test for response from db
    """
    data = show_rows()
    assert data
