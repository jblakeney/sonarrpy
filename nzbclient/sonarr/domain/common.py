from datetime import datetime
from typing import Union

from marshmallow import fields


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
