## Building URL Dynamically
## Variable Rule
## JInja 2 Template Engine

### Jinja2 Template Engine
'''
{{ }} expressions to print output in html
{%...%} conditions,for loop
{#...#} this is for comments
'''


from flask import Flask,render_template,request,redirect,url_for

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

# submit rule
@app.route("/submits",methods=['GET','POST'])
def submits():
    if request.method == 'POST': 
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


## Variable Rule
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score>=50:
        res = 'PASSED'
    else:
        res = 'FAILED'
        
    return render_template('result.html',r=res)


@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score>=50:
        res = 'PASSED'
    else:
        res = 'FAILED'
        
    exp = {'score':score,'res':res}
    
    return render_template('result1.html',results=exp)


## if condition
@app.route("/successif/<int:score>")
def successif(score):
    
    return render_template('result.html',result=score)


# dynamic url
@app.route("/fail/<int:score>")
def fail(score):

    return render_template('result.html',results=score)

# @app.route("/submits", methods=['GET', 'POST'])
# def submits():
#     total_score = 0
#     if request.method == 'POST':
#         science = float(request.form['science'])
#         maths = float(request.form['maths'])
#         c = float(request.form['c'])
#         datascience = float(request.form['datascience'])
        
#         total_score = (science+maths+c+datascience)/4
        
#     return redirect(url_for('successres',score = total_score))
@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        total_score = int((science + maths + c + datascience) / 4)

        return redirect(url_for('successres', score=total_score))

    return render_template('getresult.html')


    

if __name__ == '__main__':
    app.run(debug=True)