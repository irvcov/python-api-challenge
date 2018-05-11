
import logging
import json

from falcon import testing


class MyTestCase(testing.TestCase):
    def setUp(self, app):
        super(MyTestCase, self).setUp()
        # function called `create()` to initialize and
        # return a `falcon.API` instance.
        print("*********** Unit Testing **************+")
        self.app = app


class TestMyApp(MyTestCase):
    def test_get_todos(self):
        result = self.simulate_get('/todos')
        self.assertNotEqual(result, None)
        
    def test_update_todo(self):
    	doc = {u'status': u'Pending'}
    	testTodo = {u'title': u'Test Todo', u'status': u'Pending'}

    	self.simulate_request('POST', '/todos', json=testTodo)
    	todosList = self.simulate_get('/todos')

    	todoId = None
    	for todo in todosList.json:
    		if todo['title'] == testTodo['title']:
    			todoId = todo['id']

    	result = self.simulate_request('PUT', "/todos/{}".format(todoId), json=testTodo)
    	self.assertEqual(result.json, doc)

    def test_update_todo_not_found(self):
        testTodo = {u'title': u'Test Todo', u'status': u'Pending'}
        result = self.simulate_request('PUT', "/todos/{}".format(10000), json=testTodo)
        self.assertEqual(result.status, "204 No Content")
