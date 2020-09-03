from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/hello/<name>')
def hello_name(name):
    return f"<html><body><h1>Hello {name}!</h1></body></htlm>"


@app.route('/check', methods=['GET'])
def try_url_for_redirect():
    name = request.args.get('name')
    return redirect(url_for('hello_name', name=name))


@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/result', methods=["POST"])
def result():
    if request.method == 'POST':
        form_result = request.form
        return render_template('result.html', result=form_result)


# By default debug = false
app.run()
