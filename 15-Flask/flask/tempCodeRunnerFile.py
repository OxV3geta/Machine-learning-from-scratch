@app.route("/submit")
def submit(score):
    total_socre = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        
        total_score = (science+maths+c+datascience)/4
        
    return redirect(url_for('successres',score = total_score))