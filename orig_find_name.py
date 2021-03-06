#!/usr/bin/env python3

import pickle

def find_name(user_input, data_dir="./database/", ipl=False, t20=False):
    user_input_lower = user_input.lower()
    if ipl:
        df_bat  = pickle.load(open(data_dir+'03_ipl/batting.df', 'rb'))
        df_bowl = pickle.load(open(data_dir+'03_ipl/bowling.df', 'rb'))
    elif t20:
        df_bat  = pickle.load(open(data_dir+'01_t20s/batting.df', 'rb'))
        df_bowl = pickle.load(open(data_dir+'01_t20s/bowling.df', 'rb'))

    all_batsman = list(df_bat['batsman'].values )
    all_bowlers = list(df_bowl['bowler'].values )

    all_player = list(set(all_batsman + all_bowlers ))
    
    all_player_lower = [x.lower() for x in all_player]
    lower_name_dict = {x.lower() : x for x in all_player}
    last_name_dict = {all_player_lower[i].split()[-1]: all_player[i] for i in range(len(all_player))}

    if user_input in all_player:
        return user_input
    elif user_input_lower in all_player_lower:
        return lower_name_dict[user_input_lower]
    elif user_input_lower in last_name_dict.keys():
        return last_name_dict[user_input_lower]
    return None

if __name__=="__main__":

    user_input = "Sangakkara"
    print ( find_name(user_input) )

