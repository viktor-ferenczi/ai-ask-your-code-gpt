def decode_replace(content: bytes) -> str:
    return content.decode('utf-8', errors='replace')
