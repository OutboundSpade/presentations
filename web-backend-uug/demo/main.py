import uuid
from flask import Flask, jsonify, request, make_response
from typing import TypedDict

app = Flask(__name__)


class Todo(TypedDict):
    id: str
    title: str


class TodoStore:
    def __init__(self) -> None:
        pass

    def get_all(self) -> list[Todo]:
        return []

    def add(self, todo: Todo):
        pass

    def remove(self, id: str):
        pass


class InMemoryTodoStore(TodoStore):
    def __init__(self) -> None:
        self.todos: list[Todo] = []

    def get_all(self) -> list[Todo]:
        return self.todos

    def add(self, todo: Todo):
        # check if todo already exists
        for t in self.todos:
            if t['id'] == todo['id']:
                return
        self.todos.append(todo)

    def remove(self, id: str):
        self.todos = [t for t in self.todos if t['id'] != id]


MONGO_CONNECTION_STRING = 'mongodb+srv://uug-db:<password>@uug-web.hgx2isj.mongodb.net/?retryWrites=true&w=majority&appName=UUG-Web'


class MongoTodoStore(TodoStore):
    def __init__(self) -> None:
        from pymongo import MongoClient
        self.client: MongoClient = MongoClient(MONGO_CONNECTION_STRING, 27017)
        self.db = self.client['todo']
        self.collection = self.db['todo']

    def get_all(self) -> list[Todo]:
        return list(self.collection.find({}))

    def add(self, todo: Todo):
        self.collection.insert_one(todo)

    def remove(self, id: str):
        self.collection.delete_one({'id': id})


store: TodoStore = InMemoryTodoStore()


@app.route('/todo', methods=['GET'])
def get_todos():
    return jsonify(store.get_all())


@app.route('/todo', methods=['POST'])
def add_todo():
    post_data = request.get_json()
    print(post_data)
    if 'title' not in post_data:
        return 'Invalid request', 400
    post_data['id'] = uuid.uuid4().hex
    store.add(post_data)
    return make_response('', 200)


@app.route('/todo/<id>', methods=['DELETE'])
def remove_todo(id: str):
    store.remove(id)
    return make_response('', 200)


app.run(port=8080, debug=True)
