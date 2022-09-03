from flask import Blueprint
api_blueprint = Blueprint ( 'api_blueprint',__name__,template_folder="templates" )
@api_blueprint.route("/",methods=['GET'])
def test22():
    return "therapie"
@api_blueprint.route('/', defaults={'path': ''})
@api_blueprint.route('/<path:path>')



