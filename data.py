import requests
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import numpy as np
import os

os.environ['db_endpoint'] = 'postgresql://postgres:postgres@fpl.c5aqdxmdgobi.us-east-1.rds.amazonaws.com:5432/postgres'

endpoint = 'postgresql://postgres:postgres@fpl.c5aqdxmdgobi.us-east-1.rds.amazonaws.com:5432/postgres'
engine = create_engine(endpoint)

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r_json = requests.get(url).json()
# print(r['events'][1])

# load up elements key into player df
player_df = pd.DataFrame(r_json['elements'])
# take only useful columns and filter rest out
#player_df = player_df[['second_name', 'team', 'element_type', 'selected_by_percent', 'now_cost', 'minutes',
#                       'transfers_in', 'value_season', 'total_points']]

#player_df = player_df[['now_cost', 'value_season']]

print(player_df.head())

# Insert the player df into AWS RDS Postgres
# player_df.to_sql('players', con=engine)

sql = "SELECT * FROM players WHERE web_name LIKE 'P%';"
print(engine.execute(sqlalchemy.text(sql)).fetchall())
