import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore


init(autoreset=True)


genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

def dots():
    """Prints ... with delay (AI thinking effect)."""
    for _ in range(3): print(Fore.YELLOW + ".", end="", flush=True); time.sleep(0.5)

def senti(p):
    """Polarity -> label."""
    return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

def recommend(genre=None, mood=None, rating=None, n=5):
    """Filter by genre/rating, shuffle, analyze Overview polarity, return n (title, polarity) or message."""
    
    d= df
    if genre: d = d[d["Genre"]. str.contains(genre, case=False, na=False)]
    if rating is not None:d = d[d["IMOB_Rating"] >= rating]
    if d.empty:return"No suitable movie recommendations found."
    d, need_nonneg, out = d.sample(frac=1). reset_index(drop=True), boo1(mood),
    for, r in d.iterrows():
def show(recs, name):
    """Print in same format: header + numbered 🎥 lines with polarity + senti()."""
    
    pass

def get_genre():
    """Print genres, then ask: Enter genre number or name: (repeat until valid)."""
    
    pass

def get_rating():
    """Ask rating or 'skip' (repeat until valid)."""
    
    pass

