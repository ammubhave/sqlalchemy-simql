from errors import NotSupportedError


class Cursor():
    def __init__(self, connection):
        self.connection = connection

        # (name, type_code, display_size, internal_size, precision, scale
        #  null_ok)
        self.description = None
        self.name_info = None
        self.arraysize = 1
        self.rowcount = -1

    def execute(self, operation, parameters={}):
        raise NotImplementedError('[[%s], [%s]]' % (operation, parameters))

    def executemany(self, operation, seq_of_params=[]):
        raise NotImplementedError('[[%s], [%s]]' % (operation, seq_of_params))

    def callproc(procname, parameters={}):
        raise NotSupportedError()

    def fetchone(self):
        raise NotImplementedError()

    def fetchmany(self, size=None):
        if size is None:
            size = self.arraysize
        raise NotImplementedError()

    def fetchall(self):
        raise NotImplementedError()

    def setinputsizes(self, sizes):
        pass

    def setoutputsize(self, size, column):
        pass
