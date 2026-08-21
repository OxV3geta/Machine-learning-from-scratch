from flask import Flask

'''It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface)  application.'''
app = Flask(__name__)

@app.route("/") ## just give the route of the home page "/",In the home page there will welcome function
def welcome():
    return "Hey welcome to this AI/ML learning path! It should be amazing."

@app.route("/index") ## Routing Index page
def index():
    return "This is the index page."

if __name__ == '__main__':
    app.run(debug=True) ## 'debug' restart the server if any changes occures.