"""
MTGJSON Meta Object
"""
import datetime
from typing import Any, Dict, Union

from .. import constants
from ..mtgjson_config import MtgjsonConfig
from ..utils import to_camel_case


class MtgjsonMetaObject:
    """
    MTGJSON Meta Object
    """

    date: str
    version: str

    def __init__(
        self,
        date: Union[str, datetime.datetime] = constants.MTGJSON_BUILD_DATE,
        version: str = MtgjsonConfig().mtgjson_version,
    ) -> None:
        self.date = date if isinstance(date, str) else date.strftime("%Y-%m-%d")
        self.version = version

    def to_json(self) -> Dict[str, Any]:
        """
        Support json.dump()
        :return: JSON serialized object
        """
        options = {
            to_camel_case(key): value
            for key, value in self.__dict__.items()
            if "__" not in key and not callable(value)
        }

        for key, value in options.items():
            if isinstance(value, datetime.datetime):
                options[key] = value.strftime("%Y-%m-%d")

        return options
