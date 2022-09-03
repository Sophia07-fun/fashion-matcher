from flask import Blueprint
fashion_blueprint = Blueprint ( 'fashion_blueprint',__name__,template_folder="templates" )
@fashion_blueprint.route("/",methods=['GET'])
def test33():
    return "u go girl"
