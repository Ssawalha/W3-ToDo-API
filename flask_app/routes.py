#!/usr/bin/env python3

from flask import request, jsonify, make_response
from flask_app.app import app #note that app here is app = Flask(__name__)
from model.todoitem import TodoItem

@app.route('/')
def home():
    return jsonify({"message": "To Do List api"})

@app.route('/todo/api/tasks', methods=['GET']) #<-- /api/all is a URI
def get_all_items(): #jsonify and request object will only work under an app decorator (@app.)
    items = [item.json() for item in TodoItem.all()]
    return jsonify(items)

@app.route('/todo/api/tasks/<int:pk>', methods=['GET'])
def get_item(pk):
    if pk == 0:
        return not_found(404)
    item = TodoItem.from_pk(pk)
    if item == None:
        return not_found(404)
    return jsonify(item.json())

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'404'}), 404) #<--- make_response makes a header | this gives you the error codes
                                                        # otherwise just return places in body and only 'renders' formatting

@app.route('/todo/api/tasks', methods=['POST']) #note that index and create_task have the same route. This is fine because they have different methods
def create_task():
    if not request.json or not 'title' in request.json:
        return jsonify({'error':'bad request'}), 400
    
    new_task = TodoItem(title = request.json['title'], description = request.json.get('description'), status = False)
    new_task.save()
    return jsonify(new_task.json())

@app.route('/todo/api/tasks/<int:pk>', methods=['PUT'])
def update_task(pk):
    task = TodoItem.from_pk(pk)
    
    if not request.json:
        return jsonify({'error':'bad request'}), 400
    if 'title' in request.json and type(request.json['title']) != bytes:
        return jsonify({'error':'bad request'}), 400
    if 'description' in request.json and type(request.json['description']) != bytes:
        return jsonify({'error':'bad request'}), 400
    if 'status' in request.json and type(request.json['status']) is not bool:
        return jsonify({'error':'bad request'}), 400
    
    if request.json.get('title') != None:
        task.title = request.json.get('title')

    if request.json.get('description') != None: #keeps getting set to null for some reason
        task.description = request.json.get('description')
        
    if request.json.get('status') != None:
        task.status = request.json.get('status')
    
    task.save()
    return jsonify(task.json())

@app.route('/todo/api/tasks/<int:pk>', methods=['DELETE'])
def delete_task(pk):
    task = TodoItem.from_pk(pk)
    task.delete()
    return jsonify({'result':True})


