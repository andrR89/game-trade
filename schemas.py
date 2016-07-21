from marshmallow import fields
from marshmallow.decorators import post_load
from marshmallow.schema import Schema

from models import User


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    password = fields.Str(required=True)

    @post_load
    def make_skin(self, data):
        return User(**data)