import enum
from utils.get_envs import Environs


class App(enum.Enum):
    def __str__(self) -> str:
        return self.value

    TITLE = Environs.get("TITLE")
    VERSION = Environs.get("VERSION")
    DOCS_ENABLED = Environs.get("DOCS_ENABLED")
    DOCS_URL = Environs.get("DOCS_URL")


class Database(enum.Enum):
    def __str__(self) -> str:
        return self.value

    HOST = Environs.get("POSTGRES_HOST")
    PORT = Environs.get("POSTGRES_PORT")
    DB = Environs.get("POSTGRES_DATABASE")
    USER = Environs.get("POSTGRES_USER")
    PASSWORD = Environs.get("POSTGRES_PASSWORD")
