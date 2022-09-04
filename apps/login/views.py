from flask import Blueprint, request, render_template
from database.models import User, db
login_blueprint = Blueprint ( 'login_blueprint',__name__,template_folder="templates" )
@login_blueprint.route("/",methods=['GET'])
def test22():
    return render_template('login.html')

@login_blueprint.route('/register',methods=['POST'])
def register():
    print(request.form)
    user = User(name=request.form["name"], email=request.form["email"], password=request.form["password"])
    print(user)
    db.session.add(user)
    db.session.commit()
    return "therapie"

@login_blueprint.route('/register',methods=['GET'])
def register_view():
    return render_template('register.html')






