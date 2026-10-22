from flask import Flask, send_file, Response
from datetime import datetime, timezone
from pathlib import Path
import logging

app = Flask(__name__)
IMAGE = Path(__file__).parent / "sle.jpeg"

logging.basicConfig(level=logging.INFO, format="%(message)s")

@app.get("/")
def home():
    return """
    <!doctype html>
    <html lang="ar" dir="rtl">
    <meta charset="utf-8">
    <title>عارض الصور</title>
    <h2>عارض الصور</h2>
    <p>بالمتابعة، أنت توافق على تسجيل عنوان IP
    ووقت طلب الصفحة لأغراض الاختبار.</p>
    <a href="/photo">عرض الصورة</a>
    </html>
    """

@app.get("/photo")
def photo():
    visitor_ip = request_ip()
    timestamp = datetime.now(timezone.utc).isoformat()

    app.logger.info(
        "IP=%s | UTC=%s | Path=/photo",
        visitor_ip, timestamp
    )

    if not IMAGE.is_file():
        return "الصورة photo.jpg غير موجودة", 404

    response = send_file(IMAGE, mimetype="image/jpeg")
    response.headers["Cache-Control"] = "no-store"
    return response

def request_ip():
    from flask import request
    return request.remote_addr or "unknown"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
