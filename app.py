from flask import Flask, request, jsonify
from flask_cors import CORS  # 导入 CORS
import random
import os

app = Flask(__name__)
CORS(app)  # 允许所有跨域请求

def love_prediction(name1, name2):
    # 这里可以替换更复杂的预测算法
    combined = (name1 + name2).lower()
    seed = sum(ord(c) for c in combined)
    random.seed(seed)
    score = random.randint(1, 100)
    
    # 根据分数生成描述
    if score > 90:
        desc = "天作之合！你们是命中注定的一对！"
    elif score > 70:
        desc = "非常般配！好好珍惜这段缘分吧～"
    elif score > 50:
        desc = "有发展潜力，需要用心经营"
    elif score > 30:
        desc = "缘分尚浅，还需更多了解"
    else:
        desc = "可能不太合适，建议慎重考虑"
    
    return {
        "score": score,
        "description": desc
    }

@app.route('/predict', methods=['POST'])
def index():
    return app.send_static_file('static', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    result = love_prediction(data['name1'], data['name2'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)