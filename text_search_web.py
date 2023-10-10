import streamlit as st
import asyncio
import json

from src.api import search_text_async
from src.component import display_trademarks
from src.constant import RegisterStatusMap, TmDivisionCodeMap
from src.entity import Filter
from src.env import load_env


def main():
    env = load_env()

    st.title("Trademark Text Search")
    st.markdown(
        """
        This is a demo of the Trademark Text Search API.
        """
    )

    ## input Text
    st.header("Input Text")
    text = st.text_input("Text", value="")
    if text is not None:
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
            st.write("Searching...")
            product_types = [t for t in product_types.split(",") if t]
            similar_group_codes = [t for t in similar_group_codes.split(",") if t]

            filter = Filter(
                registerStatus=register_status,
                tmDivisionCode=tm_division_code,
                productTypes=product_types,
                similarGroupCodes=similar_group_codes,
            ).to_dict()

            trademarks = asyncio.run(
                search_text_async(
                    env.endpoint,
                    text=text,
                    k=k,
                    filter=filter,
                )
            )

            st.header("Results")
            display_trademarks(trademarks)


if __name__ == "__main__":
    main()
