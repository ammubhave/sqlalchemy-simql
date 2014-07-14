from sqlalchemy.engine import default
from sqlalchemy_simql import dbapi2
from sqlalchemy_simql.dialect.compiler import SimqlCompiler
from sqlalchemy_simql.dialect.compiler import SimqlDDLCompiler
from sqlalchemy_simql.dialect.compiler import SimqlTypeCompiler


class SimqlDialect(default.DefaultDialect):
    name = "simql"
    supports_native_boolean = True

    statement_compiler = SimqlCompiler
    ddl_compiler = SimqlDDLCompiler
    type_compiler = SimqlTypeCompiler
    default_paramstyle = 'pyformat'

    def __init__(self, **kwargs):
        default.DefaultDialect.__init__(self, **kwargs)

    @classmethod
    def dbapi(cls):
        return dbapi2
