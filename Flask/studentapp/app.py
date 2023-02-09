from flask import Flask, render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#login code
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'Login'

#This is our model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
 
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer)
    group = db.Column(db.String(300))
    college = db.Column(db.String(300))
    
    def __init__(self, name, age, group, college):
        self.name = name
        self.age = age
        self.group = group
        self.college = college

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#creating our routes
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/index')
def index():
    all_data = Student.query.all()
    return render_template("index.html", students=all_data)

@app.route('/signup', methods=['POST'])
def signup():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
     # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    
    user = User.query.filter_by(email=email).first()

    if request.method == "POST":
    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login')) # if the user doesn't exist or password is wrong, reload the page
        # if the above check passes, then we know the user has the right credentials

        login_user(user, remember=remember)
        return redirect(url_for('profile'))
    else:
        return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/insert', methods=['POST'])
def insert():

    if request.method == 'POST':
        if not request.form['name'] or not request.form['group'] or not request.form['college']:
            flash('Please enter all the fields', 'error')
        else:
            student = Student(request.form['name'], request.form['age'],request.form['group'],request.form['college'])   
 
        try:
            db.session.add(student)
            db.session.commit()
            flash("Student Inserted Successfully")
            return redirect(url_for('index'))
        except:
            return 'There is an issue in adding the task'
    else:
        return render_template('index.html')

@app.route('/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Student.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.age = request.form['age']
        my_data.group = request.form['group']
        my_data.college = request.form['college']

        try:
            db.session.commit()
            flash("Student Updated Successfully")
            return redirect(url_for('index'))
        except:
            return 'There is an issue in updating the task'
    else:
        return render_template('index.html')   

@app.route('/delete/<int:id>/', methods = ['GET', 'POST'])

def delete(id):
    my_data = Student.query.get(id)

    try:
        db.session.delete(my_data)
        db.session.commit()
        flash("Student Deleted Successfully")
        return redirect(url_for('index'))
    except:
        return "There was an issue in deleting the task" 
       

if __name__ == "__main__":
    app.run(debug=True)