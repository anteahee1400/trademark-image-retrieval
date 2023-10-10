import streamlit as st
import asyncio
import json

from src.entity import Trademark
from src.api import search_text_async
from src.util import batchfy
from src.env import load_env


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
        filter = st.text_input("filter", value="{}")
        ## button
        if st.button("Search"):
            st.write("Searching...")
            trademarks = asyncio.run(
                search_text_async(
                    env.endpoint,
                    text=text,
                    k=k,
                    filter=json.loads(filter),
                )
            )

            st.header("Results")
            display_trademarks(trademarks)


if __name__ == "__main__":
    main()
