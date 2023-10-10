from typing import Literal, TypeVar
import requests
from io import BytesIO
import base64
from PIL import Image

T = TypeVar("T")


def bytes2pil(image: bytes):
    return Image.open(BytesIO(image)).convert("RGB")


def url2pil(image_url: str) -> Image.Image:
    image_res = requests.get(image_url)
    image_res.raise_for_status()
    image = bytes2pil(image_res.content)
    return image


def pil2base64(image: Image.Image, format: Literal["PNG", "JPEG"]) -> str:
    buffered = BytesIO()
    image.save(buffered, format=format)
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def batchfy(items: list[T], batch_size: int):
    for i in range(0, len(items), batch_size):
        yield items[i : i + batch_size]
