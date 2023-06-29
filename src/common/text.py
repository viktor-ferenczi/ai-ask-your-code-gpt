def decode_replace(content: bytes) -> str:
    for encodings in ('utf-8', 'latin-1', 'latin-2'):
        try:
            return content.decode('utf-8')
        except UnicodeDecodeError:
            pass

    return content.decode('utf-8', errors='replace')
