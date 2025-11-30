from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    lastname = request.form['lastname']
    firstname = request.form['firstname']
    sex = request.form['sex']
    institution = request.form['institution']
    email = request.form['email']
    event = request.form['event']

    return render_template(
        'output.html',
        lastname=lastname,
        firstname=firstname,
        sex=sex,
        institution=institution,
        email=email,
        event=event
    )

if __name__ == '__main__':
    app.run(debug=True)
    

