from flask import Blueprint, render_template, request, redirect, abort 
from .services import create_short_url
from .models import get_db


main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET'])
def index():
    db = get_db()
    recent = db.execute('SELECT * FROM urls ORDER BY id DESC LIMIT 20').fetchall()
    return render_template('index.html', recent=recent)


@main_bp.route('/shorten', methods=['POST'])
def shorten():
    url = request.form.get('url')
    custom = request.form.get('custom_code') or None
    try:
        code = create_short_url(url, custom)
        db = get_db()
        recent = db.execute('SELECT * FROM urls ORDER BY id DESC LIMIT 20').fetchall()
        return render_template('index.html', recent=recent, short_code=code)
    except Exception as e:
        abort(400, str(e))

@main_bp.route('/<code>')
def redirect_code(code):
    db = get_db()
    row = db.execute('SELECT long_url FROM urls WHERE short_code = ?', (code,)).fetchone()
    if not row:
        abort(404)
    db.execute('UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?', (code,))
    db.commit()
    return redirect(row['long_url'])