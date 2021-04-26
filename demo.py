from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# default
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title='home', posts=posts,inside='true')


@app.route("/about")
def about():
    return render_template('about.html', title='About',inside='true')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register',inside='true', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'admin':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Profile created for {form.username.data}!', 'success')
        return redirect(url_for('profile'))
    return render_template('profile.html', title='Profile',inside='true', form=form)

@app.route("/notifications")
def notifications():

    return render_template('notifications.html', title='notifications',inside='true')


@app.route("/connections")
def connections():

    return render_template('connections.html', title='connections',inside='true')


if __name__ == '__main__':
    app.run(debug=True)