from flask import Blueprint
login_blueprint = Blueprint ( 'login_blueprint',__name__,template_folder="templates" )
@login_blueprint.route("/",methods=['GET'])
def test22():
    return "therapie"






