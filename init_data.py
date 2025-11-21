import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
CSV_PATH = DATA_DIR / "workout_db.csv"
COLUMNS = ["date", "exercise", "weight", "reps", "feedback", "ai_score", "ai_label"]

def generate_fake_data():
    print("🔄 가짜 데이터 생성 중...", end="")
    exercises = ["Bench Press", "Squat", "Deadlift", "Overhead Press", "Barbell Row"]
    feedbacks = [("Easy", 5, "5 stars"), ("Good", 4, "4 stars"), ("Hard", 2, "2 stars")]
    
    data = []
    for i in range(30):
        date = (datetime.now() - timedelta(days=30-i)).strftime("%Y-%m-%d %H:%M")
        for _ in range(random.randint(1, 3)):
            fb = random.choice(feedbacks)
            data.append({
                "date": date, "exercise": random.choice(exercises),
                "weight": random.randint(40, 100), "reps": random.randint(5, 12),
                "feedback": fb[0], "ai_score": fb[1], "ai_label": fb[2]
            })
            
    pd.DataFrame(data, columns=COLUMNS).to_csv(CSV_PATH, index=False)
    print(f"\n✅ 완료! {len(data)}개의 데이터 생성됨.")

if __name__ == "__main__":
    generate_fake_data()