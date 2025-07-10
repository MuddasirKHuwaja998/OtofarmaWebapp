from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder="assets", template_folder=".")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/assets/<path:filename>")
def assets(filename):
    return send_from_directory("assets", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)