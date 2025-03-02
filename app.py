from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

FILENAME = "users.txt"
cached_users = None

def load_users():
    global cached_users
    if cached_users is None:
        if not os.path.exists(FILENAME):
            cached_users = set()
        else:
            with open(FILENAME, "r") as file:
                cached_users = set(line.strip() for line in file)
    return cached_users

def username_exists(username):
    users = load_users()
    return username in users

@app.route('/check_username', methods=['GET'])
def check_username():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Username parameter is required"}), 400

    exists = username_exists(username)
    return jsonify({
        "exists": exists,
        "message": "Username exists" if exists else "Username available"
    }), 200

@app.route('/remind_password', methods=['GET'])
def remind_password():
    return jsonify({"password_reminder": "S3cur3_Acc0unt!"}), 200

if __name__ == '__main__':
    app.run(debug=True)

