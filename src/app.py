from flask import Flask,jsonify, request
import json
app = Flask(__name__)

todos = [ { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }]

@app.route('/todos',methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    todos.append(request_body)
    respuesta = jsonify(todos)
    return respuesta
   
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    respuesta = jsonify(todos)
    return respuesta

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)