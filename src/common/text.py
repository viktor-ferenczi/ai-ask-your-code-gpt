def decode_escape(content: bytes) -> str:
    return content.decode('utf-8', errors='surrogateescape')
