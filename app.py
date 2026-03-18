from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
task_id_counter = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    task = {
        'id': task_id_counter,
        'title': data['title'],
        'description': data.get('description', ''),
        'done': False
    }
    tasks.append(task)
    task_id_counter += 1
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            if 'title' in data:
                task['title'] = data['title']
            if 'description' in data:
                task['description'] = data['description']
            if 'done' in data:
                task['done'] = data['done']
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)