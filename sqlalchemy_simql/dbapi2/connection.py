from errors import NotSupportedError
from cursor import Cursor


class Connection(object):
    def __init__(self):
        return

    def close(self):
        raise NotImplementedError()

    def commit(self):
        raise NotImplementedError()

    def rollback(self):
        raise NotSupportedError("Rollback is not supported in SimQL")

    def cursor(self):
        return Cursor(self)
