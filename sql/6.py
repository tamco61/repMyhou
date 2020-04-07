from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['DEBUG'] = True
db_session.global_init("db/mars_explorer.sqlite")


class JobsForm(FlaskForm):
    job = StringField('Job title', validators=[DataRequired()])
    team_leader = IntegerField('Team leader id', validators=[DataRequired()])
    work_size = IntegerField('Work size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is job finished?', default=False)
    submit = SubmitField('Войти')


@app.route('/')
@app.route('/index')
def index():
    session = db_session.create_session()
    jobs = []
    for user in session.query(Jobs).all():
        jobs.append(user)
    session.commit()
    return render_template('index.html', jobs=jobs)


@app.route('/addjob', methods=['GET', 'POST'])
def addjob():
    form = JobsForm()
    if form.validate_on_submit():
        if form.validate_on_submit():
            session = db_session.create_session()
            job = Jobs()
            job.team_leader = form.team_leader.data
            job.job = form.job.data
            job.work_size = form.work_size.data
            job.collaborators = form.collaborators.data
            job.is_finished = form.is_finished.data
            session.add(job)
            session.commit()
            return redirect("/")
        return redirect('/logout')
    return render_template('addjob.html', title='Добавление работы', form=form)


if __name__ == '__main__':
    app.run()
