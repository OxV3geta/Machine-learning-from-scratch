### put and delete methods
### Working with API's -- Json

from flask import Flask,jsonify,request

app = Flask(__name__)

## Initial Data in my to do list

items = [
    {'id':1 , 'name':"Item 1","description":"This is item 1"},
    {'id':2 , 'name':"Item 2","description":"This is item 2"}
]

@app.route('/')
def home():
    return "welcome to the sample To Do list"

## Get: Retrive all the items

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## get : Retrive a specific item by ID
@app.route('/item/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    return jsonify(item)

## create a new item
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"Item not found"})
    new_item={
        "id": items[-1]['id'] + 1 if items else 1,
        "name":request.json['name'],
        "description":request.json['description']
        
    }

if __name__ == '__main__':
    app.run(debug=True)