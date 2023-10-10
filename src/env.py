import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class Env:
    kipris_api_key: str
    endpoint: str


def load_env(path: str = ".env"):
    load_dotenv(path)
    return Env(
        kipris_api_key=os.getenv("KIPRIS_API_KEY"),
        endpoint=os.getenv("ENDPOINT"),
    )
