def get_recommendation(level, goal):
    """
    level: 'beginner' or 'advanced'
    goal: 'muscle' or 'diet'
    """
    plans = {
        ("beginner", "muscle"): "3분할 (가슴/등/하체) - 머신 위주 12회 3세트",
        ("beginner", "diet"): "전신 서킷 트레이닝 + 유산소 30분",
        ("advanced", "muscle"): "5분할 (가슴/등/하체/어깨/팔) - 프리웨이트 위주 고중량",
        ("advanced", "diet"): "고강도 인터벌 트레이닝(HIIT) + 공복 유산소"
    }

    key = (level, goal)
    msg = plans.get(key, "기본 루틴: 스쿼트 - 푸쉬업 - 런지 (각 15회 3세트)")

    return f"[{level.upper()} / {goal.upper()}] 추천 루틴: {msg}"
