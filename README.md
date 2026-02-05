# UUIDv4

Simple wrapper around the standard library `uuid.UUID` that only allows v4 UUIDs.

Placed here for easy access, when I need to create semantic types using `typing.NewType`, which requires classes not types, so something like `pydantic.types.UUID4` wouldn't work, nor `uuid.uuid4()`.