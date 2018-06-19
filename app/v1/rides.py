from flask import Flask, jsonify

app = Flask(__name__)

rides = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/app/v1/rides', methods=['GET'])
def get_rides():
    return jsonify({'rides': rides})

if __name__ == '__main__':
    app.run(debug=True)