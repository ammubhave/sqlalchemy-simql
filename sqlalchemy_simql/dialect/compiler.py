from sqlalchemy import types as sqltypes, schema, util
from sqlalchemy.sql import compiler


class SimqlDDLCompiler(compiler.DDLCompiler):
    pass


class SimqlTypeCompiler(compiler.GenericTypeCompiler):
    pass


class SimqlCompiler(compiler.SQLCompiler):

    def process(self, obj, **kwargs):
        return '{' + compiler.SQLCompiler.process(self, obj, **kwargs) + '}'

    #def visit_select(self, select, **kwargs):
    #    text = 'type:"SELECT",'
        #return text
        #raise Exception(str(select), dir(select))

    def visit_cast(self, cast, **kwargs):
        return '{type:"CAST",what:%s,as:%s}' % (cast.clause._compiler_dispatch
            (self, **kwargs), cast.typeclause._compiler_dispatch(self, **kwargs)
            )

    def visit_null(self, expr, **kw):
        return 'null'
