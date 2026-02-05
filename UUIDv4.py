from uuid import UUID, SafeUUID

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