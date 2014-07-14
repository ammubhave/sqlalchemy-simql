import exceptions

# DBAPI2 Errors


class Warning(exceptions.StandardError):
    pass


class Error(exceptions.StandardError):
    def __init__(self, msg, code=None):
        exceptions.StandardError.__init__(self, msg)
        self.code = code


class InterfaceError(Error):
    pass


class DatabaseError (Error):
    pass


class DataError(DatabaseError):
    pass


class OperationalError(DatabaseError):
    pass


class IntegrityError(DatabaseError):
    pass


class InternalError(DatabaseError):
    pass


class ProgrammingError(DatabaseError):
    pass


class NotSupportedError(DatabaseError):
    pass


class NotAuthenticated(DatabaseError):
    pass