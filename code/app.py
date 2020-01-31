from flask import Flask, render_template, request, jsonify
from flask_restful import Api
from service.db_service import Workout

app = Flask(__name__)
app.secret_key = 'issa secret'
api = Api(app)

@app.route('/')
def homepage():
    return render_template('sign_in.html')


@app.route('/get_signin_token/', methods=['POST'])
def get_signin_token():
    data = request.get_json()

    print('Token: {}'.format(data))
    return jsonify(status="success", data=data)


if __name__ == '__main__':
    api.add_resource(Workout, '/workout/<string:name>')
    app.run(port=5000, debug=True)
