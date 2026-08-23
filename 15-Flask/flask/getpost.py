from flask import Flask,render_template,request
### render_template responsible for the redirect at any specific html page

##WSGI (Web Server Gateway Interface)  application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<htlm><h1>Welcome to the learning path!</h1></html>"

@app.route("/index",methods=['GET']) ## Routing Index page
def index():
    return render_template('index.html') ## that will redirect to index.html

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST': # this is condition if user give any input in the form and something then it'll be 'POST' method
        name = request.form['name'] ## request the name form the 'form.html' and with using the id:name.
        return f'Hello {name}.'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)