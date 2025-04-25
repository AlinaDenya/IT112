from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "My Awesome Flask App"

@app.route("/about")
def about():
    return "Hi, I'm Alina, a student learning Flask! 👩‍💻"

if __name__ == "__main__":
    app.run(debug=True)