from flask import Flask 

app = Flask(__name__)

@app.route("/")
def head():
    
    return "<h1>Hello Bronze World!</h1>"

@app.route("/second")
def second():
    return "This is my second page"

@app.route("/third")
def third():
    return "<h2> This is third page </h2>"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'

if __name__ == "__main__":
    app.run(debug=True)
