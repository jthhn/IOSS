from .models import get_db
from .utils import normalize_url, base62_encode

def create_short_url(long_url, custom_code=None):
    db = get_db()
    long_url = normalize_url(long_url)

    if custom_code:
        code = custom_code
        row = db.execute("SELECT 1 FROM urls WHERE short_code = ?", (code,)).fetchone()
        if row:
            raise ValueError("Custom code already exists")
        db.execute(
            "INSERT INTO urls (long_url, short_code, clicks, created_at) VALUES (?, ?, 0, datetime('now'))",
            (long_url, code)
        )
    else:
        # Insert first to get ID
        cur = db.execute(
            "INSERT INTO urls (long_url, short_code, clicks, created_at) VALUES (?, ?, 0, datetime('now'))",
            (long_url, "")
        )
        new_id = cur.lastrowid
        code = base62_encode(new_id)
        # Update with generated short code
        db.execute("UPDATE urls SET short_code = ? WHERE id = ?", (code, new_id))

    db.commit()
    return code
