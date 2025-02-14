from .log import create_logger
from .variable import *
logger = create_logger()

__all__ = [
    "logger",
    "VERSION"
]