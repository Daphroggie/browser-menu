import streamlit as st


class Redirect:
    def __init__(self, logo, name, link):
        st.image(logo)
        st.link_button(label=name, url=link)


st.header("WELCOME TO THE BROWSER HUB")
socials, utils, work, docs = st.columns(4)
with socials:
    youtube = Redirect("site icons/youtube.png", "YouTube", "https://youtube.com")