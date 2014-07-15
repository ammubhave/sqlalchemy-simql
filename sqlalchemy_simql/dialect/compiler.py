from sqlalchemy import types as sqltypes, schema, util
from sqlalchemy.sql import compiler
from sqlalchemy import exc


class SimqlDDLCompiler(compiler.DDLCompiler):
    pass


class SimqlTypeCompiler(compiler.GenericTypeCompiler):
    pass


class SimqlCompiler(compiler.SQLCompiler):

    def process(self, obj, **kwargs):
        return '{' + compiler.SQLCompiler.process(self, obj, **kwargs) + '}'

    def visit_column(self, column, include_table=True, **kwargs):
        if column.name is None:
            raise exc.CompileError("Cannot compile Column object until "
                                   "its 'name' is assigned.")

        if column.table is None or not include_table or \
                not column.table.named_with_column:
            return column.name
        else:
            return column.table.name + "/" + column.name

    def visit_alias(self, alias, asfrom=False, ashint=False,
                                iscrud=False,
                                fromhints=None, **kwargs):
        if asfrom or ashint:
            alias_name = alias.name

        if ashint:
            return self.preparer.format_alias(alias, alias_name)
        elif asfrom:
            ret = alias.original._compiler_dispatch(self,
                                asfrom=True, **kwargs) + \
                                " AS " + \
                    self.preparer.format_alias(alias, alias_name)

            if fromhints and alias in fromhints:
                ret = self.format_from_hint_text(ret, alias,
                                fromhints[alias], iscrud)

            return ret
        else:
            return alias.original._compiler_dispatch(self, **kwargs)

    def visit_select(self, select, **kwargs):
        text = 'type:"SELECT",'
        # the actual list of columns to print in the SELECT column list.
        inner_columns = [
            c for c in [
                self._label_select_column(select,
                    column,
                    populate_result_map, asfrom,
                    column_clause_args,
                    name=name)
                for name, column in select._columns_plus_names
                ]
            if c is not None
        ]

        text += ', '.join(inner_columns)

        if froms:
            text += " \nFROM "

            if select._hints:
                text += ', '.join([f._compiler_dispatch(self,
                                    asfrom=True, fromhints=byfrom,
                                    **kwargs)
                                for f in froms])
            else:
                text += ', '.join([f._compiler_dispatch(self,
                                    asfrom=True, **kwargs)
                                for f in froms])
        else:
            text += self.default_from()
        raise Exception(str(select), dir(select))

    def visit_cast(self, cast, **kwargs):
        return '{type:"CAST",what:%s,as:%s}' % \
            (cast.clause._compiler_dispatch(self, **kwargs),
             cast.typeclause._compiler_dispatch(self, **kwargs))

    def visit_null(self, expr, **kw):
        return 'null'
