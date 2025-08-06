from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user store (dictionary)
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

# POST - Create user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    if user_id in users:
        return jsonify({'error': 'User already exists'}), 400
    users[user_id] = data
    return jsonify({'message': 'User created', 'user': data}), 201

# PUT - Update user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    users[user_id] = data
    return jsonify({'message': 'User updated', 'user': data}), 200

# DELETE user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    deleted_user = users.pop(user_id)
    return jsonify({'message': 'User deleted', 'user': deleted_user}), 200

if __name__ == '__main__':
    app.run(debug=True)
