from datetime import datetime
from typing import Union

from marshmallow import Schema, fields


class Image(object):
    def __init__(self, cover_type: str = None, url: str = None):
        self.cover_type = cover_type
        self.url = url


class Ratings(object):
    def __init__(self, votes: int = None, value: float = None):
        self.votes = votes
        self.value = value


class SonarrDateTime(fields.Field):
    OBJ_TYPE = "sonarrdatetime"

    default_error_messages = {
        "invalid": "Not a valid {obj_type}.",
        "format": '"{input}" cannot be formatted as a {obj_type}.',
    }

    def _serialize(
        self, value: datetime, attr: str, obj: dict, **kwargs: dict
    ) -> Union[str, None]:
        if value is None:
            return None

        try:
            date_format = self.get_format(kwargs.get("millis", False))
            return value.strftime(date_format)
        except (TypeError, AttributeError, ValueError):
            self.fail("format", input=value, obj_type=self.OBJ_TYPE)

    def _deserialize(
        self, value: str, attr: str, data: dict, **kwargs: dict
    ) -> datetime:
        if not value:  # Falsy values, e.g. '', None, [] are not valid
            raise self.fail("invalid", input=value, obj_type=self.OBJ_TYPE)

        try:
            has_millis = "." in value
            date_format = self.get_format(has_millis)
            if has_millis:
                return datetime.strptime(value[:-2], date_format)
            else:
                return datetime.strptime(value, date_format)

        except (TypeError, AttributeError, ValueError) as e:
            print(e)
            raise self.fail("invalid", input=value, obj_type=self.OBJ_TYPE)

    @staticmethod
    def get_format(millis: bool = False):
        return "%Y-%m-%dT%H:%M:%S.%f" if millis else "%Y-%m-%dT%H:%M:%SZ"


class ImageSchema(Schema):
    class Meta:
        unknown = "EXCLUDE"
        allow_none = False

    cover_type = fields.Str(data_key="coverType")
    url = fields.Str()

    def load(self, data, many=None, partial=None, unknown=None) -> Image:
        obj = super(Schema, self).load(data, many, partial, unknown)
        return Image(**obj)


class RatingsSchema(Schema):
    class Meta:
        unknown = "EXCLUDE"
        allow_none = False

    votes = fields.Int()
    value = fields.Float()

    def load(self, data, many=None, partial=None, unknown=None) -> Ratings:
        obj = super(Schema, self).load(data, many, partial, unknown)
        return Ratings(**obj)
