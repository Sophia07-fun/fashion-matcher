from flask import Blueprint
suggestions_blueprint = Blueprint ( 'suggestions_blueprint',__name__,template_folder="templates" )
@suggestions_blueprint.route("/",methods=['GET'])
def test11():
    return "roses are red"
