import requests
import pandas as pd
import numpy as np

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r_json = requests.get(url).json()

print(r_json.keys())

# print(r['events'][1])
"""
The player are are in the elements key, find a way to load up SQL database with players in database
"""

# load up elements key into player df
player_df = pd.DataFrame(r_json['elements'])
# take only useful columns and filter rest out
#player_df = player_df[['second_name', 'team', 'element_type', 'selected_by_percent', 'now_cost', 'minutes',
#                       'transfers_in', 'value_season', 'total_points']]

#player_df = player_df[['now_cost', 'value_season']]
player_cols = list(player_df.columns)
print(player_cols)
"""
player_df = player_df[['chance_of_playing_next_round', 'chance_of_playing_this_round', 'code', 'cost_change_event',
                       'cost_change_event_fall', 'cost_change_start', 'cost_change_start_fall', 'dreamteam_count',
                       'element_type', 'ep_next', 'ep_this', 'event_points', 'first_name', 'form', 'id', 'in_dreamteam',
                       'news', 'news_added', 'now_cost', 'photo', 'points_per_game', 'second_name', 'selected_by_percent',
                       'special', 'squad_number', 'status', 'team', 'team_code', 'total_points', 'transfers_in',
                       'transfers_in_event', 'transfers_out', 'transfers_out_event', 'value_form', 'value_season',
                       'web_name', 'minutes', 'goals_scored', 'assists', 'clean_sheets', 'goals_conceded', 'own_goals',
                       'penalties_saved', 'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'bonus', 'bps',
                       'influence', 'creativity', 'threat', 'ict_index', 'influence_rank', 'influence_rank_type',
                       'creativity_rank', 'creativity_rank_type', 'threat_rank', 'threat_rank_type', 'ict_index_rank',
                       'ict_index_rank_type', 'corners_and_indirect_freekicks_order', 'corners_and_indirect_freekicks_text',
                       'direct_freekicks_order', 'direct_freekicks_text', 'penalties_order', 'penalties_text']]
"""
print(player_df['chance_of_playing_next_round'].value_counts)

print(player_df.head())
