from flask import Flask,render_template
### render_template responsible for the redirect at any specific html page

##WSGI (Web Server Gateway Interface)  application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<htlm><h1>Welcome to the learning path!</h1></html>"

@app.route("/index") ## Routing Index page
def index():
    return render_template('index.html') ## that will redirect to index.html

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) 