from flask import Flask, render_template, request
from forms import PasswordForm
from password_utils import analyze_password

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PasswordForm()
    result = None
    if form.validate_on_submit():
        password = form.password.data
        result = analyze_password(password)
        return render_template('result.html', result=result)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
