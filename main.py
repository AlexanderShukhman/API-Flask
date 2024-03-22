from flask import Flask, make_response, jsonify, abort
from flask_restful import reqparse, abort, Api, Resource
from data import db_session, jobs_api2, users_resources

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


def main():
    db_session.global_init("db/mars.db")
    # app.register_blueprint(jobs_api2.blueprint)
    api.add_resource(users_resources.UsersResource, '/api/v2/users/<int:user_id>')
    api.add_resource(users_resources.UsersListResource, '/api/v2/users')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)



if __name__ == '__main__':
    main()