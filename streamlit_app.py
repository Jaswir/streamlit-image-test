
import streamlit as st
import os
import streamlit as st
from streamlit_javascript import st_javascript
from PIL import Image
import re
from io import BytesIO

import image_to_code
import script_to_image

import streamlit as st


#Or you can use images in HTML or SVG:

with st.echo():
    st.markdown(
        '<img src="./app/static/twitter-icon.png" height="333" style="border: 5px solid orange">',
        unsafe_allow_html=True,
    )

window_width = st_javascript("window.innerWidth")

file_path_html = "./my_website/index.html"
file_path_css = "./my_website/styles.css"

if os.path.exists(file_path_html) and os.path.exists(file_path_css):
    with open(file_path_html, "r", encoding="utf8") as file:
        html_string = file.read()
    with open(file_path_css, "r", encoding="utf8") as file:
        css_string = "<style>" + file.read() + "</style>"

    html_plus_css = re.sub(r"<link.*?css.*?>", css_string, html_string)

    st.components.v1.html(
        html_plus_css,
        width=window_width,
        height=window_width / 16 * 9,
    )