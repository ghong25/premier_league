import requests
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import numpy as np
import os

<<<<<<< HEAD

endpoint = os.environ.get('PREMDB')
=======
>>>>>>> f332729bdbdce08457545c26742abfdd71dabd25
engine = create_engine(endpoint)



"""
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r_json = requests.get(url).json()
# print(r['events'][1])

# load up elements key into player df
player_df = pd.DataFrame(r_json['elements'])
# take only useful columns and filter rest out
player_df = player_df.set_index('id')
#player_df = player_df[['id', 'second_name', 'team', 'element_type', 'form', 'points_per_game', 'selected_by_percent', 'now_cost', 'minutes',
#                       'transfers_in', 'value_season', 'total_points']]

#player_df = player_df[['now_cost', 'value_season']]

print(player_df.head())

"""
# Insert the player df into AWS RDS Postgres
# player_df.to_sql('players', con=engine)

sql = "SELECT * FROM players ORDER BY selected_by_percent DESC LIMIT 10;"
print(engine.execute(sqlalchemy.text(sql)).fetchall())
