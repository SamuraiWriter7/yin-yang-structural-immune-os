#!/usr/bin/env python3
"""
Validate example YAML files against their corresponding JSON Schemas.

This validator is designed for Yin-Yang Structural Immune OS.

It validates:

* examples/humoral-defense-record.example.yaml
  against schemas/humoral-defense-record.schema.json

* examples/cellular-defense-event.example.yaml
  against schemas/cellular-defense-event.schema.json

* examples/reverse-resonance-event.example.yaml
  against schemas/reverse-resonance-event.schema.json

The script is strictly for schema validation.
It does not execute any defensive, offensive, network, or system action.
"""

from **future** import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError, ValidationError

REPO_ROOT = Path(**file**).resolve().parents[1]

VALIDATION_TARGETS = [
{
"name": "Humoral Defense Record",
"schema": "schemas/humoral-defense-record.schema.json",
"example": "examples/humoral-defense-record.example.yaml",
},
{
"name": "Cellular Defense Event",
"schema": "schemas/cellular-defense-event.schema.json",
"example": "examples/cellular-defense-event.example.yaml",
},
{
"name": "Reverse Resonance Event",
"schema": "schemas/reverse-resonance-event.schema.json",
"example": "examples/reverse-resonance-event.example.yaml",
},
]

def load_json(path: Path) -> dict[str, Any]:
"""Load a JSON file."""
try:
with path.open("r", encoding="utf-8") as file:
data = json.load(file)
except FileNotFoundError:
raise FileNotFoundError(f"JSON schema not found: {path}") from None
except json.JSONDecodeError as error:
raise ValueError(f"Invalid JSON in {path}: {error}") from error

```
if not isinstance(data, dict):
    raise ValueError(f"JSON schema must be an object: {path}")

return data
```

def load_yaml(path: Path) -> Any:
"""Load a YAML file."""
try:
with path.open("r", encoding="utf-8") as file:
return yaml.safe_load(file)
except FileNotFoundError:
raise FileNotFoundError(f"YAML example not found: {path}") from None
except yaml.YAMLError as error:
raise ValueError(f"Invalid YAML in {path}: {error}") from error

def format_validation_error(error: ValidationError) -> str:
"""Format a jsonschema validation error into a readable message."""
instance_path = "/".join(str(part) for part in error.absolute_path)
schema_path = "/".join(str(part) for part in error.absolute_schema_path)

```
if not instance_path:
    instance_path = "<root>"

if not schema_path:
    schema_path = "<schema root>"

return (
    f"Validation error:\n"
    f"  Message: {error.message}\n"
    f"  Instance path: {instance_path}\n"
    f"  Schema path: {schema_path}"
)
```

def validate_target(name: str, schema_path: Path, example_path: Path) -> None:
"""Validate a single YAML example against a JSON Schema."""
print(f"Validating target: {name}")
print(f"  Schema : {schema_path.relative_to(REPO_ROOT)}")
print(f"  Example: {example_path.relative_to(REPO_ROOT)}")

```
schema = load_json(schema_path)
example = load_yaml(example_path)

try:
    Draft202012Validator.check_schema(schema)
except SchemaError as error:
    raise ValueError(f"Invalid JSON Schema in {schema_path}: {error.message}") from error

validator = Draft202012Validator(schema, format_checker=FormatChecker())
errors = sorted(
    validator.iter_errors(example),
    key=lambda error: list(error.absolute_path),
)

if errors:
    first_error = errors[0]
    raise ValueError(format_validation_error(first_error))

print("  Result : passed")
print()
```

def main() -> int:
"""Run all validations."""
print("Yin-Yang Structural Immune OS example validation")
print("=" * 56)
print()

```
failed = False

for target in VALIDATION_TARGETS:
    name = target["name"]
    schema_path = REPO_ROOT / target["schema"]
    example_path = REPO_ROOT / target["example"]

    try:
        validate_target(name, schema_path, example_path)
    except Exception as error:
        failed = True
        print("  Result : failed")
        print(f"  Error  : {error}")
        print()

if failed:
    print("Validation failed.")
    return 1

print("All examples passed validation.")
return 0
```

if **name** == "**main**":
sys.exit(main())

