#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:09:40 2019

@author: lta100163
"""

import os
import pandas as pd

#-------------------------------------------------------------------------------------------------
# %% ENVIRONMENT SETUP SECTION
# Define key display and other attributes of the PYTHON environment.

pd.set_option("display.max_columns", 30)
pd.set_option("display.max_colwidth", 64)
pd.set_option("display.max_rows", 999)
pd.set_option("display.width", 150)

#-------------------------------------------------------------------------------------------------
# %% CONSTANTS DEFINITION SECTION
# Define key constants used within the script

# Directory and filename constants.
CURRENTDIR = os.path.dirname(os.path.realpath(__file__))     # Current working directory
USERHOMEDIR = os.path.expanduser('~')                        # Home director of current user
PROJECTSUBDIR = 'Google Drive/IST718 Project'
DATAFILENAME = 'historical tournament games.csv'             # Name of input data file
CSVOUTFILENAME = 'tournament_seeds.csv'                      # Name of output data file
PICKLEOUTFILENAME = 'tournament_seeds.zip'                   # Name of output data file

#-------------------------------------------------------------------------------------------------
# %% GLOBAL VARIABLE DECLARATIONS

output = pd.DataFrame()

#-------------------------------------------------------------------------------------------------
# %% FUNCTION DECLARATION SECTION

def record_team (season, seed, region, market, name, alias, team_id, school_ncaa, code_ncaa) :
    df = pd.DataFrame ( {
        'season':season, 'seed':seed, 'region':region, 'market':market, 'name':name, 
        'alias':alias, 'team_id':team_id, 'school_ncaa':school_ncaa, 'code_nccaa':code_ncaa })
    return df


#-------------------------------------------------------------------------------------------------
# %% DATA READ

import_cols = [
    'season', 'round', 'game_date', 
    'win_seed', 'win_region', 'win_market', 'win_name', 'win_alias',
    'win_team_id', 'win_school_ncaa', 'win_code_ncaa',
    'lose_seed', 'lose_region', 'lose_market', 'lose_name', 'lose_alias',
    'lose_team_id', 'lose_school_ncaa', 'lose_code_ncaa']

datafilepath = os.path.join(USERHOMEDIR, PROJECTSUBDIR, DATAFILENAME)
df = pd.read_csv(filepath_or_buffer = datafilepath, header=0, usecols=import_cols)

#-------------------------------------------------------------------------------------------------
# %% PROCESS DATA

# Loop through each season...
df_by_season = df.groupby(by='season')
for n1, grp1 in df_by_season : 
    # Take only the first round of each season to get the field of 64.
    season_by_round = grp1.groupby(by='round')
    round1 = season_by_round.get_group(name=64)
    # Make no asumptions. Get the max seed based on the data.
    max_seed = max(max(round1.lose_seed), max(round1.lose_seed))
    # First process the winners...
    seeds = round1.groupby(by='win_seed')
    for n2, grp2 in seeds:
        output = output.append(
            record_team(
                season=n1, seed=n2, 
                region=grp2['win_region'], market=grp2['win_market'], name=grp2['win_name'], 
                alias=grp2['win_alias'], team_id=grp2['win_team_id'], 
                school_ncaa=grp2['win_school_ncaa'], code_ncaa=grp2['win_code_ncaa']),
            ignore_index=True)
    # Then record the defeated team.
    seeds = round1.groupby(by='lose_seed')
    for n2, grp2 in seeds:
        output = output.append(
            record_team(
                season=n1, seed=n2, 
                region=grp2['lose_region'], market=grp2['lose_market'], name=grp2['lose_name'], 
                alias=grp2['lose_alias'], team_id=grp2['lose_team_id'], 
                school_ncaa=grp2['lose_school_ncaa'], code_ncaa=grp2['lose_code_ncaa']),
            ignore_index=True)
output.sort_values(by = [ 'season', 'seed', 'alias'], inplace=True)


#-------------------------------------------------------------------------------------------------
# %% OUPTUT THE DATA

csvoutputfilepath = os.path.join(USERHOMEDIR, PROJECTSUBDIR, CSVOUTFILENAME)
pickleoutputfilepath = os.path.join(USERHOMEDIR, PROJECTSUBDIR, PICKLEOUTFILENAME)
output.to_csv(path_or_buf=csvoutputfilepath, header=True, index=False)
# output.to_pickle(path=pickleoutputfilepath)
