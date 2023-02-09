from flask import Flask, render_template, request
from flask_restful import Resource, Api, marshal_with,fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///Items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

taskFields = {
    'id':fields.Integer,
    'name':fields.String,
}

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return self.name

    

"""
@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"

"""

class Items(Resource):
    @marshal_with(taskFields)
    def get(self):
        tasks = Task.query.all()
        return tasks

    @marshal_with(taskFields)
    def post(self):
        data = request.json
        task = Task(name=data['name'])
        db.session.add(task)
        db.session.commit()

        tasks = Task.query.all()
        return tasks

class Item(Resource):

    @marshal_with(taskFields)
    def get(self,pk):
        task = Task.query.filter_by(id=pk).first()
        return task

    @marshal_with(taskFields)
    def put(self,pk):
        data = request.json
        task = Task.query.filter_by(id=pk).first()
        task.name = data['name']
        db.session.commit()
        return task

    @marshal_with(taskFields)
    def delete(self,pk):
        task = Task.query.filter_by(id=pk).first()
        db.session.delete(task)
        db.session.commit()
        tasks = Task.query.all()
        return tasks
    

api.add_resource(Items, '/')
api.add_resource(Item, '/<int:pk>')


if __name__ == '__main__':
    app.run(debug=True)