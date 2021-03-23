#!/usr/bin/env python3

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

from get_profile import get_player_profile
from find_name import find_name
from top_players import top_players


from footer import Footer


def app():
    st.title("Welcome to T20I-cric-data!")
    st.sidebar.title('Find Player Profile')
    user_input_player = st.sidebar.text_input(label="Enter Cricketer's Name Eg. (DA Warner)")
    #user_input_player = st.sidebar.text_input(label="Enter Cricketer's Name Eg. (DA Warner)")
    get_top_players = st.sidebar.checkbox(label="Get Top Players in the T20Is", value=False)

    if (not user_input_player) or (not get_top_players) :
        st.write("You can try putting a cricket player's name in the left panel to see his profile as well as visualise the data.")

    if user_input_player:
        player_name = find_name(user_input_player, t20=True)
        
        if player_name is None:
            st.markdown('**'+user_input_player+'** '+" is not found.")
        else:
            bat_bowl = st.sidebar.selectbox(label="Batting/Bowling Profile",
                                            options=("bat", "bowl"))

            bat = True; xaxis='season'; yaxis='Runs'
            if bat_bowl=='bowl': 
                bat = False
                yaxis='Wickets'
        
            year_from = st.sidebar.number_input("Year from", min_value=2005, max_value=2021, value = 2005, step=1)
            year_to =   st.sidebar.number_input("Year to", min_value=2005, max_value=2021, value = 2021, step=1)
            visualize = st.sidebar.checkbox(label="Visualize", value=False)

            st.markdown('**'+player_name+'**')
            df = get_player_profile(player_name, batsman=bat, year_from=year_from, year_to=year_to, t20=True)
            st.table(df)
            
            if visualize:
                numeric_cols = list(df.select_dtypes(include=np.number).columns.values)
                xaxis = st.sidebar.selectbox(label="x-axis", options= numeric_cols)
                yaxis = st.sidebar.selectbox(label="y-axis", options= numeric_cols, index = numeric_cols.index(yaxis))

                fig = px.bar(df, x=xaxis, y=yaxis)#, range_x=[year_from, year_to])
                st.plotly_chart(fig)
    
    elif get_top_players:
        top_N = st.sidebar.number_input("Show Top ", max_value=25, value = 10, step=1)
        cols = ['Runs', 'Innings', 'NO', 'BF', 'HS', 'Ave', 'SR', '50s', '100s', '4s', '6s']
        sort_by = st.sidebar.selectbox(label="Sort By", options= cols)
        df_top=top_players(sort_by=sort_by, topN=top_N)
        st.markdown('**'+'Top T20I batsmen sorted by '+sort_by+'**'+' (Cut Off Runs =1000)')
        st.table(df_top)



    
    #st.sidebar.title('Team Profile')
    #all_ipl_teams=("Chennai Super Kings", "Delhi Capitals", "Punjab Kings", "Kolkata Knight Riders",
    #        "Mumbai Indians", "Rajasthan Royals", "Royal Challengers Bangalore", "Sunrisers Hyderabad")
    #team_name = st.sidebar.selectbox(label="Team name", 
    #                                options=all_ipl_teams)
    Footer()
