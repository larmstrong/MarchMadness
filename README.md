# MarchMadness

This project was handled by the team of [Leonard Armstrong](https://github.com/larmstrong), [Tanbir Biryajh](https://github.com/tbiryajh), [Pierre Casco](https://github.com/PierreCasco), Kyle Wojtaszek.

## Purpose

The purpose of the project is to use machine learning to predict NCAA Tournament (AKA, _"March Madness"_) team selections and team seedings.

## File Descriptions

- `Champ Polar Graph.ipynb`: Jupyter notebook code for creating a polar graph of key statistics of tournament champions.
- `Data Transformation - Box Score to Team Stats.ipynb`: Jupyter notebook for creating an aggregate data file that transforms detailed team game statistics into a simpler set of year-by-year aggregate statistics.
- `data`: Subdirectory holding and the data files that the code uses. (See notes.)
- `exploratory_analysis.py`: Exploratory data analysis creating additional graphs and tables on the NCAA March Madness data.
- `Data_Analysis_Who's_In.ipynb`: Machine learning and prediction code to determine who would be selected to the NCAA tournament.
- `get_seeds.py`: Creates a consolidated list of NCAA Tournament seeds, year-by-year from a larger data set of all NCAA games.
- `LICENSE`: License to use this code. (MIT-based.)
- `seeding.ipynb`: Machine learning and prediction code to determine what seed teams selected for the tournament will be given. 
- `README.md`: This file.

## Notes

1. Some of the code was developed locally, some using [Google Colaboratory](https://colab.research.google.com). As such, how/where the code reads in the data may be inconsistent across scripts and you may need to update the code to point correctly to the data files for your instance.
