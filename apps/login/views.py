from flask import Blueprint, request
from database.models import User, db
login_blueprint = Blueprint ( 'login_blueprint',__name__,template_folder="templates" )
@login_blueprint.route("/",methods=['GET'])
def test22():
    return "therapie"

@login_blueprint.route('/register',methods=['POST'])
def register():
    print(request.form)
    user = User(name=request.form["name"], email=request.form["email"], password=request.form["password"])
    print(user)
    db.session.add(user)
    db.session.commit()
    return "therapie"





