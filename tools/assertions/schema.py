from jsonschema import validate
from typing import Any
from jsonschema.validators import Draft202012Validator
import jsonschema


def validate_json_schema(instance: Any, schema: dict) -> None:
    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )
