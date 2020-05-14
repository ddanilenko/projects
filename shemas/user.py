from flask_restful import fields

from shemas import response_schema
from shemas.project import base_project_schema
from shemas.role import base_role_schema

__all__ = [
    "user_list_schema",
    "short_user_schema",
    "ext_user_schema",
]

base_user_schema = dict(
    id=fields.Integer,
    first_name=fields.String,
    last_name=fields.String,
)

user_list_schema = dict(
    response_schema,
    data=fields.List(
        fields.Nested(dict(
            base_user_schema,
            email=fields.String,
            city=fields.String,
            district=fields.String,
        ))
    )
)

short_user_schema = dict(
    response_schema,
    data=fields.List(fields.Nested(base_user_schema))
)

ext_user_schema = dict(
    response_schema,
    data=fields.List(
        fields.Nested(dict(
            base_user_schema,
            email=fields.String,
            city=fields.String,
            district=fields.String,
            projects=fields.List(fields.Nested(base_project_schema)),
            votes=fields.List(fields.Nested(base_project_schema)),
            roles=fields.List(fields.Nested(base_role_schema))
        ))
    )
)
