import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

colors = sns.color_palette("viridis", 20)

def top_total_goals(df):
    top_15tg = (
        df.groupby("NAME")["TotalGoals"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig1, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(top_15tg["NAME"], top_15tg["TotalGoals"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Total Goals")
    ax.set_title("Top 15 Total Scorers")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,  
            height,                            
            f'{int(height)}',                  
            ha='center',                      
            va='bottom'                      
        )
    
    top_15tg["Rank"] = top_15tg.index + 1
    st.pyplot(fig1)
    st.subheader("Top 15 – Total Goals")
    st.dataframe(
    top_15tg.rename(columns={"NAME": "Player",  "CLUB": "Club", "TotalGoals": "Total Goals"}), use_container_width=True
)
    
def top_penalty_goals(df):
    top_15pg = (
        df.groupby("NAME")["PenaltyGoals"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
)

    fig, ax = plt.subplots(figsize=(15, 6))
    bars = ax.bar(top_15pg["NAME"], top_15pg["PenaltyGoals"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Penalty Goals")
    ax.set_title("Top 15 Penalty Scorers")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,  
            height,                            
            f'{int(height)}',                  
            ha='center',                      
            va='bottom'                      
        )

    top_15pg["Rank"] = top_15pg.index + 1
    st.pyplot(fig)
    st.subheader("Top 15 – Penalty Goals")
    st.dataframe(
    top_15pg.rename(columns={"NAME": "Player", "PenaltyGoals": "Penalty Goals"}), use_container_width=True
)
    
def top_field_goals(df):
    top_15fg = (
        df.groupby("NAME")["FieldGoals"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
)

    fig, ax = plt.subplots(figsize=(15, 6))
    bars = ax.bar(top_15fg["NAME"], top_15fg["FieldGoals"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Field Goals")
    ax.set_title("Top 15 Players by Field Goals")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,  
            height,                            
            f'{int(height)}',                  
            ha='center',                      
            va='bottom'                      
        )

    top_15fg["Rank"] = top_15fg.index + 1
    st.pyplot(fig)
    st.subheader("Top 15 – Field Goals")
    st.dataframe(
    top_15fg.rename(columns={"NAME": "Player", "FieldGoals": "Field Goals"}), use_container_width=True
)
    
def top_avarage_goals(df):
    top_15ag = (
        df.groupby("NAME")["AverageGoals"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(top_15ag["NAME"], top_15ag["AverageGoals"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Goals")
    ax.set_title("Top 15 Average Goals per Game")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,  
            height,                            
            f'{height:.1f}',                  
            ha='center',                      
            va='bottom'                      
        )

    top_15ag["Rank"] = top_15ag.index + 1
    st.pyplot(fig)
    st.caption(
    "Average Goals per Game is calculated by dividing a player’s total number of goals by the number of matches played. "
    "The metric reflects a player’s scoring efficiency on a per-game basis.")
    st.subheader("Top 15 – Average Goals per Game")
    st.dataframe(
    top_15ag.rename(columns={"NAME": "Player", "AverageGoals": "Average Goals"}), use_container_width=True
)
    
def top_steals(df):
    top_15st = (
        df.groupby("NAME")["Steals"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig1, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(top_15st["NAME"], top_15st["Steals"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Steals")
    ax.set_title("Top 15 Steals")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,  
            height,                            
            f'{int(height)}',                  
            ha='center',                      
            va='bottom'                      
        )

    top_15st["Rank"] = top_15st.index + 1
    st.pyplot(fig1)
    st.subheader("Top 15 – Steals")
    st.dataframe(
    top_15st.rename(columns={"NAME": "Player", "Steals": "Steals"}), use_container_width=True
)
    
def top_blocks(df):
    top_15bl = (
        df.groupby("NAME")["Blocks"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig1, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(top_15bl["NAME"], top_15bl["Blocks"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Blocks")
    ax.set_title("Top 15 Blocks")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,  
            height,                            
            f'{int(height)}',                  
            ha='center',                      
            va='bottom'                      
        )

    top_15bl["Rank"] = top_15bl.index + 1
    st.pyplot(fig1)
    st.subheader("Top 15 – Blocks")
    st.dataframe(
    top_15bl.rename(columns={"NAME": "Player", "Blocks": "Blocks"}), use_container_width=True
)
    
def top_yellow_card(df):
    top_15yc = (
        df.groupby("NAME")["YellowCards"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig1, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(top_15yc["NAME"], top_15yc["YellowCards"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Yellow Cards")
    ax.set_title("Top 15 Yellow Cards")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,  
            height,                            
            f'{int(height)}',                  
            ha='center',                      
            va='bottom'                      
        )

    top_15yc["Rank"] = top_15yc.index + 1
    st.pyplot(fig1)
    st.subheader("Top 15 – Yellow Cards")
    st.dataframe(
    top_15yc.rename(columns={"NAME": "Player", "YellowCards": "Yellow Cards"}), use_container_width=True
)
    
def top_min_sus(df):
    top_15ms = (
        df.groupby("NAME")["2MIN"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig1, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(top_15ms["NAME"], top_15ms["2MIN"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("2 Minute Suspensions")
    ax.set_title("Top 15 2 Minute Suspensions")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,  
            height,                            
            f'{int(height)}',                  
            ha='center',                      
            va='bottom'                      
        )

    top_15ms["Rank"] = top_15ms.index + 1
    st.pyplot(fig1)
    st.subheader("Top 15 – 2 Minute Suspensions")
    st.dataframe(
    top_15ms.rename(columns={"NAME": "Player", "2MIN": "2 Minute Suspensions"}), use_container_width=True
)
    

def top_red_cards(df):
    top_15rc = (
        df.groupby("NAME")["RedCards"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig1, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(top_15rc["NAME"], top_15rc["RedCards"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Red Cards")
    ax.set_title("Top 15 Red Cards")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,  
            height,                            
            f'{int(height)}',                  
            ha='center',                      
            va='bottom'                      
        )

    top_15rc["Rank"] = top_15rc.index + 1
    st.pyplot(fig1)
    st.subheader("Top 15 – Red Cards")
    st.dataframe(
    top_15rc.rename(columns={"NAME": "Player", "RedCards": "Red Cards"}), use_container_width=True
)
    
def gk_per(df):
    goalkeepers = df[df["POSITION"] == "GK"]

    top_15_gk_perf = (
        goalkeepers.groupby("NAME")["PerformanceIndex"]
        .mean()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig1, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(top_15_gk_perf["NAME"], top_15_gk_perf["PerformanceIndex"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Performance Index")
    ax.set_title("Top 15 Goalkeeper Performance Index")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height:.2f}',  # visa med två decimaler
            ha='center',
            va='bottom'
        )

    top_15_gk_perf["Rank"] = top_15_gk_perf.index + 1
    st.subheader("Top 15 Goalkeepers – Performance Index")
    st.pyplot(fig1)
    st.caption(
    "The Average Performance Index is a league-developed metric that summarizes a player’s overall match performance based on multiple in-game actions. "
    "Higher values indicate greater overall impact.")
    st.dataframe(
        top_15_gk_perf.rename(columns={"NAME": "Player", "PerformanceIndex": "Performance Index"}),
        use_container_width=True
    )


    bottom_15_gk_perf = (
        goalkeepers.groupby("NAME")["PerformanceIndex"]
        .mean()
        .sort_values(ascending=True)
        .head(15)
        .reset_index()
    )

    fig2, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(bottom_15_gk_perf["NAME"], bottom_15_gk_perf["PerformanceIndex"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Performance Index")
    ax.set_title("Bottom 15 Goalkeeper Performance Index")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height:.2f}',  
            ha='center',
            va='bottom'
        )

    bottom_15_gk_perf["Rank"] = bottom_15_gk_perf.index + 1
    st.subheader("Bottom 15 Goalkeepers – Performance Index")
    st.pyplot(fig2)
    st.caption(
    "The Average Performance Index is a league-developed metric that summarizes a player’s overall match performance based on multiple in-game actions. "
    "Higher values indicate greater overall impact.")
    st.dataframe(bottom_15_gk_perf.rename(columns={"NAME": "Player", "PerformanceIndex": "Performance Index"}), use_container_width=True
    )

def top_ass_gk(df):
    goalkeepers = df[df["POSITION"] == "GK"]

    top_15_gk_as = (
        goalkeepers.groupby("NAME")["Assists"]
        .mean()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(top_15_gk_as["NAME"], top_15_gk_as["Assists"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Assists")
    ax.set_title("Top 15 Goalkeeper Assists")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height}', 
            ha='center',
            va='bottom'
        )

    top_15_gk_as["Rank"] = top_15_gk_as.index + 1
    st.pyplot(fig)
    st.subheader("Top 15 Goalkeepers – Assists")
    st.dataframe(
        top_15_gk_as.rename(columns={"NAME": "Player", "Assists": "Assists"}),
        use_container_width=True
    )

def top_goals_gk(df):
    goalkeepers = df[df["POSITION"] == "GK"]

    top_15_gk_g = (
        goalkeepers.groupby("NAME")["Goals"]
        .mean()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(top_15_gk_g["NAME"], top_15_gk_g["Goals"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Goals")
    ax.set_title("Top 15 Goalkeeper Goals")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height}', 
            ha='center',
            va='bottom'
        )

    top_15_gk_g["Rank"] = top_15_gk_g.index + 1
    st.pyplot(fig)
    st.subheader("Top 15 Goalkeepers – Goals")
    st.dataframe(
        top_15_gk_g.rename(columns={"NAME": "Player", "Goals": "Goals"}),
        use_container_width=True
    )

def def_index(df):
    #Top 15
    top_15di = (
        df.groupby("NAME")["DefenceIndex"]
        .mean()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig1, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(top_15di["NAME"], top_15di["DefenceIndex"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Defence Index")
    ax.set_title("Top 15 Defence Index")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,  
            height,                            
            f'{height:.2f}',                  
            ha='center',                      
            va='bottom'                      
        )

    top_15di["Rank"] = top_15di.index + 1
    st.subheader("Top 15 Defence Index")
    st.pyplot(fig1)
    st.caption(
    "The Defence Index is based on disciplinary actions (yellow cards, red cards, and two-minute suspensions) "
    "as well as defensive contributions such as steals and blocks. "
    "The index is calculated to produce a single value where higher values indicate a more positive defensive impact, "
    "while lower values reflect a less effective or more penalized defensive performance. ")
    st.dataframe(
    top_15di.rename(columns={"NAME": "Player", "DefenceIndex": "Defence Index"}), use_container_width=True
)
   #Bottom 15 
    bottom_15di = (
        df.groupby("NAME")["DefenceIndex"]
        .mean()
        .reset_index()
    )

    bottom_15di = bottom_15di[bottom_15di["DefenceIndex"] != 0]
    bottom_15di = bottom_15di.sort_values("DefenceIndex", ascending=True).head(15).reset_index(drop=True)

    fig2, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(bottom_15di["NAME"], bottom_15di["DefenceIndex"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Defence Index")
    ax.set_title("Bottom 15 Players Defence Index")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,  
            height,                            
            f'{height:.2f}',                  
            ha='center',                      
            va='bottom'                      
        )

    bottom_15di["Rank"] = bottom_15di.index + 1
    st.subheader("Bottom 15 Defence Index")
    st.pyplot(fig2)
    st.caption(
    "The Defence Index is based on disciplinary actions (yellow cards, red cards, and two-minute suspensions) "
    "as well as defensive contributions such as steals and blocks. "
    "The index is calculated to produce a single value where higher values indicate a more positive defensive impact, "
    "while lower values reflect a less effective or more penalized defensive performance. ")
    st.dataframe(
    bottom_15di.rename(columns={"NAME": "Player", "DefenceIndex": "Defence Index"}), use_container_width=True
)
    
def player_per(df):
#Top 15
    top_15_player_perf = (
        df.groupby("NAME")["PerformanceIndex"]
        .mean()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig1, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(top_15_player_perf["NAME"], top_15_player_perf["PerformanceIndex"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Performance Index")
    ax.set_title("Top 15 Players Performance Index")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height:.2f}',  # visa med två decimaler
            ha='center',
            va='bottom'
        )

    top_15_player_perf["Rank"] = top_15_player_perf.index + 1
    st.subheader("Top 15 Players – Performance Index")
    st.pyplot(fig1)
    st.caption(
    "The Average Performance Index is a league-developed metric that summarizes a player’s overall match performance based on multiple in-game actions. "
    "Higher values indicate greater overall impact.")
    st.dataframe(
        top_15_player_perf.rename(columns={"NAME": "Player", "PerformanceIndex": "Performance Index"}),
        use_container_width=True
    )


#bottom 15
    bottom_15_player_perf = (
        df.groupby("NAME")["PerformanceIndex"]
        .mean()
        .sort_values(ascending=True)
        .head(15)
        .reset_index()
    )

    fig2, ax = plt.subplots(figsize=(15,6))
    bars = ax.bar(bottom_15_player_perf["NAME"], bottom_15_player_perf["PerformanceIndex"], color=colors)
    ax.set_xlabel("Player")
    ax.set_ylabel("Performance Index")
    ax.set_title("Bottom 15 Players Performance Index")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height:.2f}',  # visa med två decimaler
            ha='center',
            va='bottom'
        )

    bottom_15_player_perf["Rank"] = bottom_15_player_perf.index + 1
    st.subheader("Bottom 15 Players – Performance Index")
    st.pyplot(fig2)
    st.caption(
    "The Average Performance Index is a league-developed metric that summarizes a player’s overall match performance based on multiple in-game actions. "
    "Higher values indicate greater overall impact.")
    st.dataframe(
        bottom_15_player_perf.rename(columns={"NAME": "Player", "PerformanceIndex": "Performance Index"}),
        use_container_width=True
    )
    
