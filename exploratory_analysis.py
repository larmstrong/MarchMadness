#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:43:28 2019

@author: lta100163
"""

import matplotlib.pyplot as plt
import numpy             as np
import os
import pandas            as pd

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

#-------------------------------------------------------------------------------------------------
# %% GLOBAL VARIABLE DECLARATIONS

output = pd.DataFrame()

#-------------------------------------------------------------------------------------------------
# %% FUNCTION DECLARATION SECTION

def jitter (pct = 0.2) :
    return np.random.uniform(low=0.0, high=pct)


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

print(df.corr())
plt.matshow(df.corr())
plt.show()

# %% There seems to be a correlation between the losing seed and the round. Let's plot it.

new_lose_seed = df['lose_seed'].apply(func=jitter)
new_round = df['round'].apply(func=jitter)
fig, ax = plt.subplots(figsize=(16,9))
plt.scatter(new_lose_seed, new_round)
plt.yticks(labels = (2, 4, 8, 16, 32, 64))

