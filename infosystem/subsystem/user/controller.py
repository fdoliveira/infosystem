from infosystem.common.subsystem import controller
from infosystem.subsystem.user import entity


class Controller(controller.Controller):

    def __init__(self):
        super(Controller, self).__init__(entity.User)
