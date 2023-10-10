import streamlit as st

from src.entity import Trademark
from src.util import batchfy


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
