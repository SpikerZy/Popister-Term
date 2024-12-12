import logging

def setup_logger():
    """Configure and return a logger instance."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger("LyretaAgent")
