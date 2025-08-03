from flask import Blueprint, request, jsonify, redirect
from app.utils import generate_short_code, is_valid_url
from app.models import save_url_mapping, get_original_url, increment_click, get_stats

url_bp = Blueprint("url_shortener", __name__)

@url_bp.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })

@url_bp.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "message": "URL Shortener API is running"
    })

@url_bp.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    url = data.get("url")

    if not url or not is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_short_code()
    save_url_mapping(short_code, url)

    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    }), 201

@url_bp.route("/<short_code>", methods=["GET"])
def redirect_to_url(short_code):
    entry = get_original_url(short_code)
    if not entry:
        return jsonify({"error": "Short URL not found"}), 404

    increment_click(short_code)
    return redirect(entry["original_url"])

@url_bp.route("/api/stats/<short_code>", methods=["GET"])
def get_url_stats(short_code):
    stats = get_stats(short_code)
    if not stats:
        return jsonify({"error": "Short URL not found"}), 404
    return jsonify(stats)
