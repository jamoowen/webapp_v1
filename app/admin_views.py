from app import app

@app.route("/admin")
def admin():
    return "ADMIN PAGE"
