from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key="clave secreta"
@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        session['form']=request.form
        return redirect("/results")
    else:
        print("renderizando pagina index.html")
        return render_template("index.html")

@app.route("/results", methods=['GET'])
def results_survey():
    print(session['form'])
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)