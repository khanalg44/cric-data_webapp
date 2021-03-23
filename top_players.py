#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

data_dir= './database/01_t20s/'

def batting_summary_():
    df = pickle.load(open(data_dir+'batting.df', 'rb'))
    all_players = df['batsman'].unique()
    
    data=[]
    for player in all_players:
        dfp = df[ df['batsman']==player ]
        Team_ = dfp['Team'].unique()
        if len(Team_)>1:
            Team_ = Team_[0]+', '+Team_[1]
        else: 
            Team_ = Team_[0]
        
        
        Inns_ = dfp.shape[0]
        Runs_ = dfp.Runs.sum()
        BF_   = dfp.BF.sum()
        NOs_  = dfp.NO.sum()
        
        HS    = max(dfp.Runs)
        Fifty = ((dfp.Runs>=50) & (dfp.Runs<100) ).sum()
        Hundred = (dfp.Runs>=100).sum()
        
        Wins  = sum(dfp.Win)
        Toss_wins = sum(dfp.Toss)
        
        SR    = np.round(100*Runs_/(BF_+0.1), 2) # add 0.1 to avoide deviding by 0
        
        if Inns_== NOs_:
            Ave=dfp.Runs.sum() 
        else:
            Ave   = np.round(Runs_/(Inns_-NOs_), 2)
        Fours = dfp['4s'].sum()
        Sixes = dfp['6s'].sum()

        data.append([player, Team_, Inns_, NOs_, Runs_, BF_, HS, Ave, SR, Fifty, Hundred, Fours, Sixes] )
    df_p = pd.DataFrame(data, columns=['player', 'Team', 'Innings', 'NO', 'Runs', 'BF', 'HS',
                                       'Ave','SR', '50s', '100s', '4s', '6s'])
    return df_p

def top_players(sort_by='Runs', topN=10, threshold_runs=1000):
    df_summary = batting_summary_()
    # get rid of players under the threshold
    dff = df_summary[df_summary['Runs']>=threshold_runs]
    df_sorted = dff.sort_values(by=[sort_by], ascending=False, ignore_index=True).iloc[:topN]
    return df_sorted

if __name__=="__main__":
    df_summary= top_players(sort_by='Runs')
    print ( df_summary )
