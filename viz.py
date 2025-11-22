import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io, tracker
import pandas as pd

def _save():
    buf = io.BytesIO()
    plt.savefig(buf, format='png'); buf.seek(0); plt.close()
    return buf

def draw_weekly_chart():
    df = tracker.load_all_data()
    plt.figure(figsize=(10, 5)); plt.title("Weekly Workout Volume")
    if not df.empty:
        df['vol'] = pd.to_numeric(df['weight'], errors='coerce').fillna(0) * pd.to_numeric(df['reps'], errors='coerce').fillna(0)
        df.groupby('date')['vol'].sum().plot(kind='line', marker='o')
        plt.tight_layout()
    return _save()

def draw_area_chart():
    df = tracker.load_all_data()
    plt.figure(figsize=(6, 6)); plt.title("Exercise Distribution")
    if not df.empty:
        df['exercise'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    return _save()