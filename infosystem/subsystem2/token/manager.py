import uuid

from infosystem.common.subsystem import manager
from infosystem.common.subsystem import operation


class Create(operation.Operation):

    def pre(self, **kwargs):
        # FIXME(samueldmq): this method needs to receive the parameters
        # explicitly.
        if kwargs.get('user'):
            # FIXME(samueldmq): how to avoid someone simply passing the user
            # in the body and then having a valid token?
            self.user = kwargs['user']
        else:
            domain_name = kwargs.get('domain_name', None)
            username = kwargs.get('username', None)
            password = kwargs.get('password', None)

            # TODO(samueldmq): allow get by unique attrs
            domains = self.manager.api.domains.list(name=domain_name)

            if not domains:
                return False

            domain_id = domains[0].id

            users = self.manager.api.users.list(domain_id=domain_id, name=username, password=password)
            if not users:
                return False

            self.user = users[0]

        return self.user.is_stable()

    def do(self, session, **kwargs):
        # TODO(samueldmq): use self.user.id instead of self.user_id
        token = self.driver.instantiate(id=uuid.uuid4().hex, user_id=self.user.id)

        self.driver.create(token, session=session)
        return token


class Manager(manager.Manager):

    def __init__(self, driver):
        super(Manager, self).__init__(driver)
        self.create = Create(self)