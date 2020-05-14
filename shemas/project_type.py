from flask_restful import fields

from shemas import response_schema

__all__ = [
    "project_type_list_schema",
    "short_project_type_schema",
    "ext_project_type_schema",
    "base_project_type_schema"
]

base_project_type_schema = dict(
    id=fields.Integer,
    title=fields.String,
)

project_type_list_schema = dict(
    response_schema,
    data=fields.List(fields.Nested(base_project_type_schema))
)

short_project_type_schema = dict(
    response_schema,
    data=fields.List(fields.Nested(base_project_type_schema))
)

ext_project_type_schema = dict(
    response_schema,
    data=fields.List(fields.Nested(base_project_type_schema))
)
