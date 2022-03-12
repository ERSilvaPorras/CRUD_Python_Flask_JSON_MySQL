from src.controllers.indexController import *
from src.controllers.createController import *
from src.controllers.edittController import *
from src.controllers.errorsController import NotFoundController
# URLs de pages of project
routes = {
    "index_route": "/", "index_controller": IndexController.as_view("index"),
    "create_route": "/create-user", "create_controller": CreateController.as_view("create"),
    "edit_route": "/edit-user", "edit_controller": EdittController.as_view("edit"),
    "not_found_route":404, "not_found_controller": NotFoundController.as_view("not_found")
}