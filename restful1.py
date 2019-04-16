from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from requests import get

app = Flask(__name__)
api = Api(app)

TODOS={
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    }

# TodoList
#shows a list of all todos, and lets you POST to add new tasks

class TodoList(Resource):
    def get(self):
        print("debug: sending full list")
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        print("debug: added task with id '{}'".format(todo_id))
        return TODOS[todo_id], 201

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

## Todo shows a single todo item and lets you delete a todo item

class Todo(Resource):
    def get(self, todo_id):
        print("debug: getting task with id '{}'".format(todo_id))
        abort_iftodo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        print("debug: deleting task with id '{}'".format(todo_id))
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        print("debug: creating task with id '{}'".format(todo_id))
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

class Ping(Resource):
    def get(self, ip)
        print("Ping statistics for ip '{}'".format(ip))
        url = get('{}')


parser = reqparse.RequestParser()
parser.add_argument('task')


# Actually setup the Api resource routing here

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(pingUrl, '/ping/

if __name__ == '__main__':
    app.run(debug=True)
