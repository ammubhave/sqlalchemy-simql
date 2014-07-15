from sqlalchemy.engine import default
from sqlalchemy_simql import dbapi2
from sqlalchemy_simql.dialect.compiler import SimqlCompiler
from sqlalchemy_simql.dialect.compiler import SimqlDDLCompiler
from sqlalchemy_simql.dialect.compiler import SimqlTypeCompiler


class SimqlDialect(default.DefaultDialect):
    name = "simql"
    supports_native_boolean = True
    supports_alter = False
    supports_views = False
    supports_right_nested_joins = False
    supports_simple_order_by_label = False

    statement_compiler = SimqlCompiler
    ddl_compiler = SimqlDDLCompiler
    type_compiler = SimqlTypeCompiler
    default_paramstyle = 'pyformat'

    def __init__(self, **kwargs):
        default.DefaultDialect.__init__(self, **kwargs)

    @classmethod
    def dbapi(cls):
        return dbapi2

    def initialize(self, connection):
        self.server_version_info = None
        self.default_schema_name = None
        self.default_isolation_level = None
        self.returns_unicode_strings = False
