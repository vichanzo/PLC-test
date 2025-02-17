from flask import Flask, render_template, jsonify

app = Flask(
 __name__,
 template_folder="./templates",
 static_folder="./static",
)

# https://dev.to/pratap2210/beginners-guide-to-setting-up-and-running-flask-web-server-1710


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/location")
def location():
    return render_template('location.html')

@app.route("/table")
def mytable():
    return render_template('table.html')

@app.route("/t2")
def table2():
    return render_template('table2.html')

@app.route("/json")
def json_response():
    response = {"name": "MyName", "age": 24}
    return jsonify([response])

if __name__ == "__main__":
    app.run(debug=True)
