from flask import Flask, request, jsonify, render_template, send_file
# 팀원들의 모듈을 불러올 준비 (지금은 없으므로 에러 방지 처리)
try:
    import tracker, ai_utils, viz, routine
except ImportError:
    pass

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/log", methods=["POST"])
def log_workout():
    data = request.get_json()
    # 추후 팀원 C(AI), B(Tracker)의 함수 연결 예정
    return jsonify({"status": "success", "ai_analysis": {"label": "준비중", "score": 3}, "recommended_weight": data.get("weight", 0)})

@app.route("/api/graph/<type>")
def get_graph(type):
    # 추후 팀원 D(Viz) 함수 연결 예정
    return "Graph Module Not Ready", 404

@app.route("/api/routine", methods=["POST"])
def api_routine():
    # 추후 팀원 E(Routine) 함수 연결 예정
    return jsonify({"routine": "루틴 기능 준비중"})

if __name__ == "__main__":
    app.run(debug=True)
    