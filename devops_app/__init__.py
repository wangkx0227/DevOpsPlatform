from devops_app.init import create_app
from devops_app.settings.config import DevelopmentConfig


app = create_app(DevelopmentConfig)
__all__ = [
    "app",
]
