from core.init import create_app
from core.settings.public import DevelopmentConfig
from . import __version__

print(f"DevOpsPlatform api Current version: {__version__.__version__}")

app = create_app(DevelopmentConfig)
__all__ = [
    "app",
]
