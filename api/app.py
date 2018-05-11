import logging

import falcon

from api.handlers import HealthHandler, TodosHandler
from api.request import CustomRequest, LoggingMiddleware, RequestMiddleware
from config import settings
from config.settings import config
from api.unitTest import TestMyApp

settings.configure_logging(config.api_logging)

log = logging.getLogger()

app = falcon.API(request_type=CustomRequest, middleware=[RequestMiddleware(), LoggingMiddleware()])
app.add_route('/health', HealthHandler())
app.add_route('/todos', TodosHandler())
app.add_route('/todos/{id}', TodosHandler())

log.info("Started with config file: {}".format(settings.config_file))

testApp = TestMyApp()
testApp.setUp(app)
testApp.test_get_todos()
testApp.test_update_todo()
testApp.test_update_todo_not_found()
