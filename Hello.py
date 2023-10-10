import streamlit as st
import asyncio
import json

from src.api import search_image_async
from src.component import display_trademarks
from src.constant import RegisterStatusMap, TmDivisionCodeMap
from src.entity import Filter
from src.util import pil2base64, bytes2pil
from src.env import load_env


def extract_image_format(type: str):
    type = type.split("/")[-1].lower()
    mapping = {"png": "PNG", "jpg": "JPEG", "jpeg": "JPEG"}
    return mapping[type]


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

        register_status = st.multiselect(
            "법적 상태",
            RegisterStatusMap.keys(),
            default=[],
            format_func=lambda x: RegisterStatusMap[x],
        )
        tm_division_code = st.multiselect(
            "유형",
            TmDivisionCodeMap.keys(),
            default=[],
            format_func=lambda x: TmDivisionCodeMap[x],
        )

        product_types = st.text_input("상품분류", value="", help="상품분류를 입력하세요 (, 로 구분)")
        similar_group_codes = st.text_input("유사군", value="", help="유사군을 입력하세요 (, 로 구분)")
        ## button
        if st.button("Search"):
            product_types = [t for t in product_types.split(",") if t]
            similar_group_codes = [t for t in similar_group_codes.split(",") if t]

            filter = Filter(
                registerStatus=register_status,
                tmDivisionCode=tm_division_code,
                productTypes=product_types,
                similarGroupCodes=similar_group_codes,
            ).to_dict()

            st.write("Searching...")
            trademarks = asyncio.run(
                search_image_async(
                    env.endpoint,
                    image=base64_image,
                    k=k,
                    filter=filter,
                )
            )

            st.header("Results")
            display_trademarks(trademarks)


if __name__ == "__main__":
    main()
