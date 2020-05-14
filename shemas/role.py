from flask_restful import fields

from shemas import response_schema

__all__ = [
    "role_list_schema",
    "short_role_schema",
    "ext_role_schema",
    "base_role_schema"
]

base_role_schema = dict(
    id=fields.Integer,
    title=fields.String,
)

role_list_schema = dict(
    response_schema,
    data=fields.List(fields.Nested(base_role_schema))
)

short_role_schema = dict(
    response_schema,
    data=fields.List(fields.Nested(base_role_schema))
)

ext_role_schema = dict(
    response_schema,
    data=fields.List(fields.Nested(base_role_schema))
)
