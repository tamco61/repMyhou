import flask
from data import db_session
from data.users import User
from flask import jsonify, request
from datetime import datetime, timedelta

blueprint = flask.Blueprint('user_api', __name__,
                            template_folder='templates')


@blueprint.route('/api/user')
def get_user():
    session = db_session.create_session()
    user = session.query(User).all()
    return jsonify(
        {
            'user':
                [item.to_dict()
                 for item in user]
        }
    )


@blueprint.route('/api/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'user': user.to_dict(only=('name', 'surname', 'email', 'age', 'address', 'position', 'speciality'))
        }
    )


@blueprint.route('/api/user', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'surname', 'name', 'age', 'position', 'speciality',
                  'address', 'email', 'hashed_password']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    user = User(
        id=request.json['id'],
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
        hashed_password=request.json['hashed_password'],
        modified_date=datetime.now()
    )
    if session.query(User).filter(User.id == user.id).first():
        return jsonify({'error': 'Id already exists'})
    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    session.delete(user)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/user/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    session = db_session.create_session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        k = ['surname', 'name', 'age', 'position', 'speciality',
             'address', 'email', 'hashed_password']
        for key in k:
            if key in request.json:
                if key == 'surname':
                    user.surname = request.json[key]
                if key == 'name':
                    user.name = request.json[key]
                if key == 'age':
                    user.age = request.json[key]
                if key == 'position':
                    user.position = request.json[key]
                if key == 'speciality':
                    user.speciality = request.json[key]
                if key == 'address':
                    user.address = request.json[key]
                if key == 'email':
                    user.email = request.json[key]
                if key == 'hashed_password':
                    user.set_password(request.json[key])
        session.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'Bad request'})
