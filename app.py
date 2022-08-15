from flask import Flask, render_template, request



app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def indes():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression_DBS")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree_DBS")
        r2 = model2.predict([[rates]])   
        return (render_template("index.html",result1="temp",result2="temp"))
    else:
        return (render_template("index.html",result1="waiting",result2="waiting"))


if __name__== "__main__":
    app.run()



