from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        data = {"message":"This is a GET request", "content": None}
        return jsonify(data)
    elif request.method == "POST":
        content = request.json
        return jsonify({"message": "Recived your data", "Your cont": content})
    

    
@app.route('/api/update/<int:task_id>', methods=['PUT','PATCH'])
def update_item(item_id):
    context = request.json
    if request.method == "PUT":
        return jsonify({"message":"Item updated with new data", "ItemID": item_id, "newData":context})
    elif request.method == "PATCH":
        return jsonify({"message":"Item partialy updated", "ItemID": item_id, "newData":context})

        
@app.route('/api/delete/<int:task_id>', methods=['DELETE'])
def delete_task(item_id):
    if request.method == "DELETE":
        return jsonify({"message":"Item is deleted", "ItemID": item_id})

