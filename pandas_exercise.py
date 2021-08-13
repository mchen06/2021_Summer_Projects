import pandas as pd

nba[
    (nba["_iscopy"] == 0) &
    (nba["date_game"].str.startswith(3 or 4 or 5)) &
    (nba["date_game"].str.endswith ('1992')) &
    (nba["notes"].notnull()) &
        )

#all found on describe, but can be called individually
nba["elo_i"].sum()
nba["elo_i"].min()
nba["elo_i"].max()
