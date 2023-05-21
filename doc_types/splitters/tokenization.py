import tiktoken

ENCODING = tiktoken.encoding_for_model('gpt-3.5-turbo')


def tiktoken_len(text):
    tokens = ENCODING.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)
