def decode_replace(content: bytes) -> str:
    for encoding in ('utf-8', 'latin-1', 'latin-2'):
        try:
            return content.decode(encoding)
        except UnicodeDecodeError:
            pass

    return content.decode('utf-8', errors='replace')
