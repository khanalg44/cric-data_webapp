#!/usr/bin/env python3

import streamlit as st
from PIL import Image

from footer import Footer

def app():

    st.title("Welcome to Cric-Data!")
    st.markdown("Thank you for visiting the webpage. You can find a lot of data analysis as well as data visualization on this page. Please choose your format on the left panel to see your data as well as visualize the data.")

    image = Image.open('./images/consistency.png')
    st.image(image, caption='Runs vs the standard deviation (normalized) for all the players in IPL (2008-2020) with a cut off runs 2500. (Number of 30+ scores in the bracket.)')
    Footer()


