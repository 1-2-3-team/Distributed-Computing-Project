from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('./index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    with open("variable.txt", "w") as f:
        f.write(variable)
        f.close()
    return variable

if __name__ == '__main__':
    app.run(debug = True)