from flask_restful import reqparse

from .base import ControllerBase
from wafec.fi.hypothesis.services import TestService

__all__ = [
    "TestController"
]


class TestController(ControllerBase):
    def __init__(self):
        ControllerBase.__init__(self)
        self.service = TestService()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uuid', type=str, help='Test Universal Unique Identifier')
        args = parser.parse_args()
        test = self.service.create(args['uuid'])
        self.db_session.commit()
        return test.id, 201
