import requests
import aiohttp

from src.entity import Trademark


def search_text(
    endpoint: str,
    text: str,
    k: int = 32,
    filter: dict = None,
) -> list[Trademark]:
    url = f"{endpoint}/trademark/search/text"
    if filter is None:
        filter = {}

    body = {"text": text, "k": k, "filter": filter}
    response = requests.post(url, json=body)
    response.raise_for_status()
    results = response.json()

    trademarks = []
    for r in results:
        trademark = Trademark(
            application_number=r["applicationNumber"],
            product_name=r.get("koreanName"),
            product_name_eng=r.get("englishName"),
            register_status=r["registerStatus"],
            tm_division_code=r["tmDivisionCode"],
            image_url=r["imageUrl"],
            product_types=r.get("productTypes"),
            similar_group_codes=r.get("similarGroupCodes"),
        )
        trademarks.append(trademark)

    return trademarks


async def search_text_async(
    endpoint: str,
    text: str,
    k: int = 32,
    filter: dict = None,
) -> list[Trademark]:
    url = f"{endpoint}/trademark/search/text"
    if filter is None:
        filter = {}

    body = {"text": text, "k": k, "filter": filter}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=body) as response:
            results = await response.json()

    trademarks = []
    for r in results:
        trademark = Trademark(
            application_number=r["applicationNumber"],
            product_name=r.get("koreanName"),
            product_name_eng=r.get("englishName"),
            register_status=r["registerStatus"],
            tm_division_code=r["tmDivisionCode"],
            image_url=r["imageUrl"],
            product_types=r.get("productTypes"),
            similar_group_codes=r.get("similarGroupCodes"),
        )
        trademarks.append(trademark)

    return trademarks


def search_image(
    endpoint: str,
    image: str,
    k: int = 32,
    filter: dict = None,
) -> list[Trademark]:
    url = f"{endpoint}/trademark/search/image"
    if filter is None:
        filter = {}

    body = {"image": image, "k": k, "filter": filter}
    response = requests.post(url, json=body)
    response.raise_for_status()
    results = response.json()

    trademarks = []
    for r in results:
        trademark = Trademark(
            application_number=r["applicationNumber"],
            product_name=r.get("koreanName"),
            product_name_eng=r.get("englishName"),
            register_status=r["registerStatus"],
            tm_division_code=r["tmDivisionCode"],
            image_url=r["imageUrl"],
            product_types=r.get("productTypes"),
            similar_group_codes=r.get("similarGroupCodes"),
        )
        trademarks.append(trademark)

    return trademarks


async def search_image_async(
    endpoint: str,
    image: str,
    k: int = 32,
    filter: dict = None,
) -> list[Trademark]:
    url = f"{endpoint}/trademark/search/image"
    if filter is None:
        filter = {}

    body = {"image": image, "k": k, "filter": filter}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=body) as response:
            if response.status != 200:
                raise Exception(await response.text())
            results = await response.json()

    trademarks = []
    for r in results:
        trademark = Trademark(
            application_number=r["applicationNumber"],
            product_name=r.get("koreanName"),
            product_name_eng=r.get("englishName"),
            register_status=r["registerStatus"],
            tm_division_code=r["tmDivisionCode"],
            image_url=r["imageUrl"],
            product_types=r.get("productTypes"),
            similar_group_codes=r.get("similarGroupCodes"),
        )
        trademarks.append(trademark)

    return trademarks