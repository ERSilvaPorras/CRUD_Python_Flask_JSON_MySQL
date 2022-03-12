from flask import Flask
from src.routes.routes import *
app = Flask(__name__)
# secret_key sessions ------------------------------------------------------------------
# app.config['SECRET_KEY'] = 'the random string'
# Asociation Routes and Controllers  ---------------------------------------------------
app.add_url_rule(routes['index_route'], view_func=routes['index_controller'])
app.add_url_rule(routes['create_route'], view_func=routes['create_controller'])
app.add_url_rule(routes['edit_route'], view_func=routes['edit_controller'])
# URLs Error ---------------------------------------------------------------------------
app.register_error_handler(routes["not_found_route"], routes['not_found_controller'])
