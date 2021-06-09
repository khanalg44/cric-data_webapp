#!/usr/bin/env python3
import streamlit as st
import home_page, ipl_page, odi_page, t20_page

all_pages = [
        ["Home Page", home_page.app], 
        ["T20I", t20_page.app], 
        ["ODI", odi_page.app], 
        ["IPL", ipl_page.app], 
        ]

def main():
    pages = []
    for page in all_pages:
        pages.append( {"title":page[0], "app":page[1]}  )
    app = st.sidebar.radio('Go To', pages, format_func = lambda app: app["title"])
    app['app']()

if __name__=="__main__":
    main()
