from datetime import datetime

import requests


def test_testcase_get():
    testcase_url = 'http://127.0.0.1:5000/testcase'
    r = requests.post(
        testcase_url,
        json={
            'name': f'name1{datetime.now().isoformat()}',
            'description': 'description1',
            'steps': ['1', '2', '3']
        }
    )
    assert r.status_code == 200

    r = requests.get(testcase_url)
    print(r.json())
    assert r.json()['body']


def test_task_post():
    task_url = 'http://127.0.0.1:5000/task'
    r = requests.post(
        task_url,
        json={
            'name': f'测试任务{datetime.now().isoformat()}',
            'description': 'description1',
            'start_time': '2020-10-10',
            'end_time': '2020-11-11',
            'testcase_ids': [1, 2, 3]
        }
    )
    print(r.json())


def test_task_get():
    task_url = 'http://127.0.0.1:5000/task'
    r = requests.get(
        task_url,
        params={
            'id': '5'
        }
    )
    print(r.json())


def test_task_put():
    task_url = 'http://127.0.0.1:5000/task'
    r = requests.put(
        task_url,
        json={
            'id': 6,
            'name': f'测试任务{datetime.now().isoformat()}',
            'description': 'description2',
            'start_time': '2020-10-10',
            'end_time': '2020-12-12',
            'testcase_ids': [1, 2, 3, 4, 5]
        }
    )
    print(r.json())


def test_task_delete():
    task_url = 'http://127.0.0.1:5000/task'
    r = requests.delete(
        task_url,
        json={
            'id': '5'
        }
    )
    print(r.json())
