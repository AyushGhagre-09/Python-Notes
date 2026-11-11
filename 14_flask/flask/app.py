from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return "Home Route"


@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/form",methods=['GET','POST'])
def form():
    print(request.method)
    if request.method=='POST':
        name=request.form["name"]
        return f"Hello {name}"
    
    return render_template('form.html')

#variable rule
@app.route("/success/<int:score>")
def success(score):
    if(score>=50):
        res="PASSED"
    else:
        res="FAILED"
    exp={"score":score,"res":res}
    return render_template("result.html",results=exp)


#dynamic url redirect
@app.route("/get_results", methods=["GET","POST"])
def get_result():
    total_score=0
    if request.method=='POST':
        print(request.form)
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    else:
        return render_template("getresult.html")
    return redirect(url_for("success",score=total_score))

if __name__=="__main__":
    app.run(debug=True)