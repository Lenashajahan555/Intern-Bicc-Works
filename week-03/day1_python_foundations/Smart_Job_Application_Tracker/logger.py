import logging
from config import LOGGING

logging.basicConfig(
    filename=LOGGING["filename"],
    level=getattr(logging, LOGGING["level"].upper()),
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger=logging.getLogger(__name__)