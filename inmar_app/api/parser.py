from typing import Optional

import jsonschema

from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from inmar_app.api import schema


class JSONSchemaParser(JSONParser):
    def parse(
        self,
        stream: str, media_type: Optional[str] = None,
        parser_context: Optional[str] = None
    ) -> dict:

        """
        Parser to validate schema

        :param stream: WSGI request
        :param media_type: media_type it should come api/json
        :param parser_context: Parser context request
        :return: return Parse data if the schema get validated
        :raise: ValueError if schema won't get validated
        """
        data = super(JSONSchemaParser, self).parse(stream, media_type,
                                                   parser_context)
        try:
            jsonschema.validate(data, schema.store_json)
        except ValueError as error:
            raise ParseError(detail=str(error))
        else:
            return data
