import json
from datetime import datetime
from typing import List

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:test@2020@192.168.147.131:3306/lagou'
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


class TestCase(db.Model):
    __tablename__ = 'testcase'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)
    steps = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    status = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<User %r>' % self.username


# 测试任务和测试用例的关联关系表
class TaskTestCase(db.Model):
    __tablename__ = 'task_testcase'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer)
    testcase_id = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.username


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    description = db.Column(db.String(120), nullable=True)


class TestCaseService(Resource):
    def get(self):
        testcases: List[TestCase] = TestCase.query.all()
        res = [{
            'id': testcase.id,
            'name': testcase.name,
            'description': testcase.description,
            'steps': json.loads(testcase.steps)
        } for testcase in testcases]
        return {
            'body': res
        }

    def post(self):
        testcase = TestCase(
            name=request.json.get('name'),
            description=request.json.get('description'),
            steps=json.dumps(request.json.get('steps'))
        )
        db.session.add(testcase)
        db.session.commit()
        return {
            'msg': 'ok'
        }


class TaskService(Resource):
    def get(self):
        id = request.args.get('id')
        print('id:', id)
        res_testcase = []
        if id:
            task = Task.query.filter_by(id=id).first()
            task_cases = TaskTestCase.query.filter_by(task_id=id).all()
            for task_case in task_cases:
                testcase = TestCase.query.filter_by(id=task_case.testcase_id).first()
                res_testcase += [{
                    'id': testcase.id,
                    'name': testcase.name,
                    'description': testcase.description,
                    'steps': json.loads(testcase.steps)
                }]
            print('res_testcase:', res_testcase)
            return {
                'body': [{
                    'id': task.id,
                    'name': task.name,
                    'description': task.description,
                    'start_time': str(task.start_time),
                    'end_time': str(task.end_time),
                    'status': task.status,
                    'testcases': res_testcase
                }]
            }
        else:
            tasks: List[Task] = Task.query.all()
            res_task = []
            for task in tasks:
                res_testcase = []
                task_cases = TaskTestCase.query.filter_by(task_id=task.id).all()
                for task_case in task_cases:
                    testcase = TestCase.query.filter_by(id=task_case.testcase_id).first()
                    res_testcase += [{
                        'id': testcase.id,
                        'name': testcase.name,
                        'description': testcase.description,
                        'steps': json.loads(testcase.steps)
                    }]
                res_task += [{
                    'id': task.id,
                    'name': task.name,
                    'description': task.description,
                    'start_time': str(task.start_time),
                    'end_time': str(task.end_time),
                    'status': task.status,
                    'testcases': res_testcase
                }]

            return {
                'body': res_task
            }

    def post(self):
        task = Task(
            name=request.json.get('name'),
            description=request.json.get('description'),
            start_time=request.json.get('start_time'),
            end_time=request.json.get('end_time')
        )
        db.session.add(task)
        db.session.commit()
        name = request.json.get('name')
        print("name:", name)
        task = Task.query.filter_by(name=name).first()
        print('task', task.id)
        for testcase_id in request.json.get('testcase_ids'):
            task_testcase = TaskTestCase(
                task_id=task.id,
                testcase_id=testcase_id
            )
            db.session.add(task_testcase)
        db.session.commit()
        return {
            'msg': 'ok'
        }

    def put(self):
        task_id = request.json.get('id')
        task = Task.query.filter_by(id=task_id).first()
        task_cases = TaskTestCase.query.filter_by(task_id=task_id).all()
        task.name=request.json.get('name')
        task.description = request.json.get('description')
        task.start_time = request.json.get('start_time')
        task.end_time = request.json.get('end_time')
        task.update_time = datetime.now()
        for task_case in task_cases:
            db.session.delete(task_case)
        for testcase_id in request.json.get('testcase_ids'):
            task_testcase = TaskTestCase(
                task_id=task.id,
                testcase_id=testcase_id
            )
            db.session.add(task_testcase)
        db.session.commit()
        return {
            'msg': 'ok'
        }

    def delete(self):
        id = request.json.get('id')
        print('id:', id)
        task = Task.query.get(id)
        task_cases = TaskTestCase.query.filter_by(task_id=id).all()
        for task_case in task_cases:
            db.session.delete(task_case)
        db.session.delete(task)
        db.session.commit()
        return {
            'msg': 'ok'
        }


class ReportService(Resource):
    def get(self):
        pass


api.add_resource(TestCaseService, '/testcase')
api.add_resource(TaskService, '/task')
api.add_resource(ReportService, '/report')

if __name__ == '__main__':
    app.run(debug=True)
