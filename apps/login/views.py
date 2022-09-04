from flask import Blueprint, request, render_template, session, abort, url_for, redirect
from database.models import User, db

login_blueprint = Blueprint ( 'login_blueprint',__name__,template_folder="templates" )

@login_blueprint.route("/",methods=['GET'])
def test22():
    return render_template('login.html')

@login_blueprint.route("/",methods=['POST'])
def login():
    password = request.form.get("Userpassword")
    user = request.form.get("Usermail")

    database = User.query.filter_by(email=user).first()
    if password == database.password:
        session['logged_in'] = True
        return redirect(url_for('fashion_blueprint.setup'))
    else:
        session['logged_in'] = False
        return redirect(url_for('login_blueprint.login'))

    print (database)
    print (request.form)
    return ""



@login_blueprint.route('/register',methods=['POST'])
def register():
    print(request.form)
    user = User(name=request.form["name"], email=request.form["email"], password=request.form["password"])
    print(user)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("fashion_blueprint.setup"))

@login_blueprint.route('/register',methods=['GET'])
def register_view():
    return render_template('register.html')






