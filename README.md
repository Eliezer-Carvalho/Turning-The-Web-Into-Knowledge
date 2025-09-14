# Football Match Data Dataset - 2025/2026

This repository contains a dataset of football match statistics collected through web scraping from various football leagues around the world. The data was extracted using Playwright, BeautifulSoup, and Pandas. This dataset includes detailed information about the performance of teams in the leagues:

1. La Liga 
2. Premier League 
3. Bundesliga 
4. Serie A 
5. Ligue 1
6. Brasileirão 
7. Eredivisie 
8. Liga Portugal 
9. Liga Profesional


# Features

* main.py

This function allows you to add data from a league's web page, collecting complete information for all matches listed on the page.

* add_more.py 

This function is optimised to add only the most recent data, i.e. if there are already 10 match days in the dataset and the 11th match day was played yesterday, the function will only add the data from this new match day.


# Dataset Structure

The dataset contains the following columns, which provide detailed statistics for each football match:


DATE	

HOME_TEAM	

AWAY_TEAM	

HOME_GOALS	

AWAY_GOALS	

EXPECTED_GOALS

TEAM_POSSESION

TOTAL_SHOTS

SHOTS_ON_TARGET

BIG_CHANCES

CORNERS

%_PASSES_SUCCEED

EXPECTED_GOALS_REMATES_À_BALIZA

SHOTS_OF_TARGET

BLOCKED_SHOTS

SHOTS_INSIDE_THE_BOX

SHOTS_OUTSIDE_THE_BOX

SHOTS_AT_CROSSBAR

TOUCHES_IN_THE_OPPOSITION_AREA

ACCURATE_DEEP_PASSES

OFFSIDES

FREE_KICK

%_LONG_PASSES

%_PASSES_FINAL_THIRD

%_CROSSES

EXPECTED_ASSISTS

THROWS

FOULS

%_TACKLES

DUELS_WON

CLEARENCES

INTERCEPTIONS

ERRORS_THAT_LEAD_TO_SHOTS

ERROS_THAT_LEAD_TO_GOAL	

EXPECTED_GOALS_ON_TARGET_FACED

GOALS_PREVENTED


# Important

To use the code, specific links from the page from which the data is taken are required.

To do so, please contact me.


# Libraries Used

Playwright - (https://pypi.org/project/playwright/)

BeautifulSoup - (https://pypi.org/project/beautifulsoup4/)

Pandas - (https://pypi.org/project/pandas/)
