import pandas as pd
from pathlib import Path
from datetime import datetime

DATA_DIR = Path("data")
CSV_PATH = DATA_DIR / "workout_db.csv"
COLUMNS = ["date", "exercise", "weight", "reps", "feedback", "ai_score", "ai_label"]

def _init_db():
    if not DATA_DIR.exists(): DATA_DIR.mkdir(parents=True)
    if not CSV_PATH.exists(): pd.DataFrame(columns=COLUMNS).to_csv(CSV_PATH, index=False)

def save_entry(data: dict):
    _init_db()
    row = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "exercise": data.get("exercise", "unknown"),
        "weight": data.get("weight", 0), "reps": data.get("reps", 0),
        "feedback": data.get("feedback", ""),
        "ai_score": data.get("ai_score", 0), "ai_label": data.get("ai_label", "")
    }
    pd.DataFrame([row]).to_csv(CSV_PATH, mode='a', header=False, index=False)

def load_all_data():
    _init_db()
    try: return pd.read_csv(CSV_PATH)
    except: return pd.DataFrame(columns=COLUMNS)
