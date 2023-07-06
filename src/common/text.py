def decode_normalize(content: bytes) -> str:
    try:
        decoded = content.decode('utf-8')
    except UnicodeDecodeError:
        decoded = content.decode('latin-1')

    return normalize(decoded)


def normalize(content: str) -> str:
    return content.replace('\r\n', '\n').replace('\r', '').replace('\0', '\n')
