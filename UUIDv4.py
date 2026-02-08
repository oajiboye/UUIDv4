from typing import Any
from uuid import UUID, SafeUUID

from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema, CoreSchema

class UUIDv4(UUID):
    def __init__(
        self,
        hex: str | None = None,
        bytes: bytes | None = None,
        bytes_le: bytes | None = None,
        fields: tuple[int, int, int, int, int, int] | None = None,
        int: int | None = None,
        version: int | None = None,
        *,
        is_safe: SafeUUID = SafeUUID.unknown
    ) -> None:
        
        super().__init__(hex, bytes, bytes_le, fields, int, version, is_safe=is_safe)

        if self.version != 4:
            raise ValueError(f"{self} is not a valid UUIDv4")

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source_type: Any,
        handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        
        return core_schema.no_info_after_validator_function(
            function=lambda x: cls(str(x)),
            schema=core_schema.uuid_schema(version=4),
            serialization=core_schema.plain_serializer_function_ser_schema(
                function=lambda x: str(x)
            )
        )