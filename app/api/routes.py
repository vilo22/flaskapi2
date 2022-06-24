from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/test', methods=['GET'])
def test():
    return 'testing some data'