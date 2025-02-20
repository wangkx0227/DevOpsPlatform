from .log import create_logger
from .mail import send_email

logger = create_logger()

__all__ = ["logger", "send_email"]
