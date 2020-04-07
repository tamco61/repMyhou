from flask import Flask, render_template, redirect, request, abort
from data import db_session
from data.users import User
from data.jobs import Jobs
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import PasswordField, TextAreaField, StringField, SubmitField, BooleanField, IntegerField
from wtforms.fields.html5 import EmailField
from flask_login import current_user, LoginManager, login_user, logout_user, login_required

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.sqlite")
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


class RegisterForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    surname = StringField('Фамилия пользователя', validators=[DataRequired()])
    age = IntegerField('Ваш возраст', validators=[DataRequired()])
    position = StringField("Ваша должность", validators=[DataRequired()])
    speciality = StringField("Ваша специальность", validators=[DataRequired()])
    address = StringField("Ваш адрес", validators=[DataRequired()])
    submit = SubmitField('Зарегитрироваться')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')


class JobForm(FlaskForm):
    job = StringField('Job title', validators=[DataRequired()])
    team_lead = IntegerField('Team leader id', validators=[DataRequired()])
    work_size = IntegerField('Work size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is job finished?')
    submit = SubmitField('Submit')


@app.route("/")
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title="Authorization", form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            address=form.address.data,
            speciality=form.speciality.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/addjob', methods=['GET', 'POST'])
def addjob():
    form = JobForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        job = Jobs(
            job=form.job.data,
            team_leader=form.team_lead.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data
        )
        session.add(job)
        session.commit()
        return redirect("/")
    return render_template('addjob.html', title="Adding a job", form=form)


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = JobForm()
    if request.method == 'GET':
        session = db_session.create_session()
        job = session.query(Jobs).filter(Jobs.id == id,
                                         (Jobs.team_leader == current_user.id) | (current_user.id == 1)).first()
        if job:
            form.job.data = job.job
            form.team_lead.data = job.team_leader
            form.work_size.data = job.work_size
            form.collaborators.data = job.collaborators
        else:
            abort(404)
    if form.validate_on_submit():
        session = db_session.create_session()
        job = session.query(Jobs).filter(Jobs.id == id,
                                         (Jobs.user == current_user) | (current_user.id == 1)).first()
        if job:
            job.job = form.job.data
            job.team_leader = form.team_lead.data
            job.work_size = form.work_size.data
            job.collaborators = form.collaborators.data
            session.commit()
            return redirect('/')
        abort(404)
    return render_template('addjob.html', title='Edit job', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")


def main():
    app.run()


if __name__ == '__main__':
    main()
