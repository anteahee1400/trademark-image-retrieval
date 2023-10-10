import streamlit as st
import asyncio
import json

from src.entity import Trademark
from src.api import search_image_async
from src.util import batchfy, pil2base64, bytes2pil
from src.env import load_env


def extract_image_format(type: str):
    type = type.split("/")[-1].lower()
    mapping = {"png": "PNG", "jpg": "JPEG", "jpeg": "JPEG"}
    return mapping[type]


def display_trademarks(trademarks: list[Trademark]):
    ## 표 형식으로 이미지를 출력한다.
    st.write("## Trademark List")

    columns = st.columns(5)

    for batch in batchfy(trademarks, batch_size=5):
        imgs = [t.image_url or "assets/no-image.png" for t in batch]
        cpts = [t.product_name or t.product_name_eng for t in batch]

        for i in range(len(batch)):
            with columns[i]:
                st.image(imgs[i], caption=cpts[i], use_column_width=True)


def main():
    env = load_env()

    st.title("Trademark Image Search")
    st.markdown(
        """
        This is a demo of the Trademark Image Search API.
        """
    )

    ## input local image
    st.header("Input Image")
    image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        image = image_file.read()
        format = extract_image_format(image_file.type)
        st.image(image, caption="Uploaded Image", width=256)

        pil_image = bytes2pil(image)
        base64_image = pil2base64(pil_image, format=format)

        ## search
        st.header("Search")
        k = st.number_input("k", min_value=1, max_value=100, value=32)
        filter = st.text_input("filter", value="{}")
        ## button
        if st.button("Search"):
            st.write("Searching...")
            trademarks = asyncio.run(
                search_image_async(
                    env.endpoint,
                    image=base64_image,
                    k=k,
                    filter=json.loads(filter),
                )
            )

            st.header("Results")
            display_trademarks(trademarks)


if __name__ == "__main__":
    main()
