from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",
                            image_name="Don",
                            role_name="Don",
                            is_farsi=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", \
            port=5000, \
            debug=True)
