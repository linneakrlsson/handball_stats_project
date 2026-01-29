import streamlit as st
import seaborn as sns
from plots import top_total_goals, top_penalty_goals, top_field_goals, top_avarage_goals, top_steals, top_blocks, top_yellow_card,top_min_sus, top_red_cards, gk_per, top_ass_gk, top_goals_gk, def_index, player_per
from data import load_data

colors = sns.color_palette("viridis", 20)

df = load_data()

def Home():
    st.title("Bundesliga Handball Data Dashboard")
    st.markdown("Visualisations of Bundesliga season 2022/2023")
Home()
 
st.sidebar.header("Choose visualisation")
val1 = st.sidebar.selectbox("Goalscoring Stats", ["None", "Performance Index", "Top 15 Total Goals", "Top 15 Penalty Scorers", "Top 15 Field Scorers", "Top 15 Average Goals"])
val2 = st.sidebar.selectbox("Defending Stats", ["None", "Defence Index", "Top 15 Steals", "Top 15 Blocks", "Top 15 Yellow Cards", "Top 15 2 Minute Suspensions", "Top 15 Red Cards"])
val3 = st.sidebar.selectbox("Goalkeeping Stats", ["None", "Performance index", "Top 15 Assists by Goalkeepers", "Top 15 Goals by Goalkeepers"])


#Total Goals
if val1 == "Top 15 Total Goals": 
    top_total_goals(df)

#Penalty Goals
if val1 == "Top 15 Penalty Scorers": 
    top_penalty_goals(df)

#Field Goals
if val1 == "Top 15 Field Scorers":
    top_field_goals(df)

#Avarage Goals
if val1 == "Top 15 Average Goals":
    top_avarage_goals(df)

#Performance Index players
if val1 == "Performance Index":
    player_per(df)

#Defence Index
if val2 == "Defence Index":
    def_index(df)

#Steals
if val2 == "Top 15 Steals":
    top_steals(df)

#Blocks 
if val2 == "Top 15 Blocks":
    top_blocks(df)

#Yellow Cards
if val2 == "Top 15 Yellow Cards":
    top_yellow_card(df)
    
#2 Minute Suspensions
if val2 == "Top 15 2 Minute Suspensions":
    top_min_sus(df)
  
#Red Cards
if val2 == "Top 15 Red Cards":
    top_red_cards(df)

 #Goalkeeper Performance index   
if val3 == "Performance index":
    gk_per(df)

#Assists by Goalkeepers
if val3 == "Top 15 Assists by Goalkeepers":
    top_ass_gk(df)

#Goals by Goalkeepers
if val3 == "Top 15 Goals by Goalkeepers":
    top_goals_gk(df)