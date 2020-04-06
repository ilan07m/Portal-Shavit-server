from Server.app import app
from flask import jsonify, make_response


# Return a http 400 error to client
@app.errorhandler(400)
def handle_400_error(_error):
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


# Return a http 401 error to client
@app.errorhandler(401)
def handle_401_error(_error):
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


# Return a http 404 error to client
@app.errorhandler(404)
def handle_404_error(_error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# Return a http 500 error to client
@app.errorhandler(500)
def handle_500_error(_error):
    return make_response(jsonify({'error': 'Server error'}), 500)
