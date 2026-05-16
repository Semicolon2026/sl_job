from app.logger import get_logger
from app.client import fetch_url
from app.validator import validate_job

logger = get_logger()

def main():
    logger.info("Starting job validation workflow")

    validate_job()

    response = fetch_url("https://example.com")

    logger.info(f"Response status: {response}")

if __name__ == "__main__":
    main()
