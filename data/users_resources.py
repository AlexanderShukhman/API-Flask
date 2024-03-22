from flask import jsonify
from  data import db_session
from flask_restful import Resource, abort
from  .users import User
from .users_parse import parser

def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")
        return None
    return user


class UsersResource(Resource):
    def get(self, user_id):
        user = abort_if_user_not_found(user_id)
        if user:
            return jsonify({'users': user.to_dict(only=('id',
                'surname', 'name', 'age', 'address', 'email'))})

    def delete(self, user_id):
        user = abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'surname', 'name', 'age', 'address', 'email'))
            for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            address=args['address'],
            email=args['email']
        )
        session.add(user)
        session.commit()
        return jsonify({'id': user.id})
