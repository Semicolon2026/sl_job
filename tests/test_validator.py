from app.validator import validate_job

def test_validate_job():
    result = validate_job()

    assert result is not None
