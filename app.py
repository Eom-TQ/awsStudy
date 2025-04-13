import pymysql
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

conn = pymysql.connect(
    host='db',
    user='root',        # 사용 중인 MySQL 계정
    password='1234',        # 비밀번호
    db='flask_crud',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/memos', methods=['GET'])
def get_memos():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM memos")
        memos = cursor.fetchall()
    return jsonify(memos)

@app.route('/memos', methods=['POST'])
def create_memo():
    data = request.get_json()
    with conn.cursor() as cursor:
        sql = "INSERT INTO memos (title, content) VALUES (%s, %s)"
        cursor.execute(sql, (data['title'], data['content']))
        conn.commit()
    return jsonify({'status': 'created'})

@app.route('/memos/<int:memo_id>', methods=['PUT'])
def update_memo(memo_id):
    data = request.get_json()
    with conn.cursor() as cursor:
        sql = "UPDATE memos SET title=%s, content=%s WHERE id=%s"
        cursor.execute(sql, (data['title'], data['content'], memo_id))
        conn.commit()
    return jsonify({'status': 'updated'})

@app.route('/memos/<int:memo_id>', methods=['DELETE'])
def delete_memo(memo_id):
    with conn.cursor() as cursor:
        sql = "DELETE FROM memos WHERE id=%s"
        cursor.execute(sql, (memo_id,))
        conn.commit()
    return jsonify({'status': 'deleted'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
