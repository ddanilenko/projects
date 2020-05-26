from flask_restful import fields
from flask_restful.reqparse import RequestParser

from shemas import response_schema
from shemas.project_type import base_project_type_schema

__all__ = [
    "project_list_schema",
    "short_project_schema",
    "ext_project_schema",
    "post_project_parser",
    "base_project_schema"
]

base_project_schema = dict(
    id=fields.Integer,
    title=fields.String,
    description=fields.String,
    level_title=fields.String,
    status_title=fields.String,
    format_title=fields.String,
    author_id=fields.Integer,
)

project_list_schema = dict(
    response_schema,
    data=fields.List(fields.Nested(base_project_schema))
)

short_project_schema = dict(
    response_schema,
    data=fields.List(fields.Nested(base_project_schema))
)

from shemas.user import base_user_schema

ext_project_schema = dict(
    response_schema,
    data=fields.Nested(
        dict(base_project_schema,
             tags=fields.List(fields.String),
             project_types=fields.List(fields.Nested(base_project_type_schema)),
             responsible=fields.List(fields.Nested(base_user_schema)),
             project_votes=fields.List(fields.Nested(base_user_schema))
             )
    )
)

post_project_parser = RequestParser()
post_project_parser.add_argument("title", type=str, required=True)
post_project_parser.add_argument("description", required=True)
post_project_parser.add_argument("level_title", required=True)
post_project_parser.add_argument("format_title", required=True)
post_project_parser.add_argument("author_id", type=int, required=True)
post_project_parser.add_argument("tags", required=False, action='append')
post_project_parser.add_argument("project_types", required=False, store_missing=False, action='append')
post_project_parser.add_argument("responsible", required=False, store_missing=False, action='append')
post_project_parser.add_argument("project_votes", required=False, store_missing=False, action='append')

get_project_parser = RequestParser()
get_project_parser.add_argument("id", store_missing=False)
get_project_parser.add_argument("title", store_missing=False)
get_project_parser.add_argument("description", store_missing=False)
get_project_parser.add_argument("level_title", store_missing=False)
get_project_parser.add_argument("status_title", store_missing=False)
get_project_parser.add_argument("format_title", store_missing=False)
get_project_parser.add_argument("author_id", store_missing=False)
get_project_parser.add_argument("tags", store_missing=False, action='append')
get_project_parser.add_argument("project_types", store_missing=False, action='append')
get_project_parser.add_argument("responsible", store_missing=False, action='append')
get_project_parser.add_argument("project_votes", store_missing=False, action='append')
