import string
from urllib.parse import urlparse

ALLOWED_CHARS = string.ascii_letters + string.digits

def base62_encode(num):
    if num == 0:
        return ALLOWED_CHARS[0]
    s = []
    base = len(ALLOWED_CHARS)
    while num:
        num, rem = divmod(num, base)
        s.append(ALLOWED_CHARS[rem])
    return ''.join(reversed(s))

def normalize_url(url):
    if not urlparse(url).scheme:
        url = 'http://' + url
    return url