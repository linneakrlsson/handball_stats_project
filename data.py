import pandas as pd

def load_data():
    df = pd.read_csv("handball_stats_cleaned.csv")
    df.columns = df.columns.str.strip()

    #Uträkning på totalt gjorda mål
    df["TotalGoals"] = df["PenaltyGoals"] + df["FieldGoals"]

    #Uträkning på ett genomsnitt antal gjorda mål per match
    df["AverageGoals"] = df["TotalGoals"] / df["GamesPlayed"]

    #Uträkning av ett "försvarsindex" där ett högt värde är ett bra försvar med få bestraffningar och ett lågt värde motsatsen.
    df["DefenceIndex"] = (df["Steals"] + df["Blocks"]) / (df["YellowCards"] + df["2MIN"]*2 + df["RedCards"]*3 + 1)

    return df