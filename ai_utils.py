from transformers import pipeline

print("Loading AI Model...")
try:
    sentiment_pipeline = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")
except:
    sentiment_pipeline = None

def get_ai_feedback(text: str):
    if not sentiment_pipeline or not text: return {"score": 3, "label": "Neutral"}
    try:
        res = sentiment_pipeline(text)[0]
        return {"score": int(res['label'].split()[0]), "label": res['label']}
    except: return {"score": 3, "label": "Error"}

def recommend_next_weight(current, score):
    current = float(current)
    if score <= 2: return max(current - 5, 0)
    elif score >= 4: return current + 5
    return current