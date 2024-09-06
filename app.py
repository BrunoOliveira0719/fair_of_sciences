from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def calculadora ():
    if request.method == 'POST':
        pass
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug = True)
    