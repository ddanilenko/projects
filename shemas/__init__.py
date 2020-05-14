from flask_restful import fields

response_schema = dict(
    status=fields.String,
    message=fields.String
)
