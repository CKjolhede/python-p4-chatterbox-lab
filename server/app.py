from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
CORS(app)

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

@app.route('/messages')
def get(self):
    messages_list = [p.to_dict() for p in Message.query.all()]
    body = (messages_list)
    response_code = 201
    headers = {'Content-Type': 'application/json'}
    return make_response(body, response_code, headers)

@app.route('/messages')
def post(self):
    form_json = request.get_json()
    
    message = Message(
    body = form_json['body'],
    username = form_json['username'],    
    )
    db.session.add(message)
    db.session.commit()
    response_dict = message.to_dict()
    body = (response_dict)
    response_code = 201
    headers = {'Content-Type': 'application/json'}
    
    return make_response(body, response_code, headers)

if __name__ == '__main__':
    app.run(port=5555)
