from flask import Blueprint, render_template, request, redirect, url_for
from database.models import Clothing, User

fashion_blueprint = Blueprint ( 'fashion_blueprint',__name__,template_folder="templates" )
@fashion_blueprint.route("/",methods=['GET'])
def serve_add_clothes():
    return render_template('add_clothes.html')

@fashion_blueprint.route("/setup",methods=['GET'])
def setup():
    if len(request.args) > 0:
        preference = request.args['contrast']
        # user = User.query.filter_by(username='admin').first()
        return redirect(url_for('fashion_blueprint.serve_add_clothes'))
    return render_template('setup.html')

# @fashion_blueprint.route("/setup",methods=['POST'])
# def setup_user():
#     return render_template('setup.html')


@fashion_blueprint.route("/clothing",methods=['POST'])
def add_clothes():
    name = request.form.get('name')
    color = request.form.get("color")
    clothingtype = request.form.get('clothingtype')

    print(name)
    print(color)
    print(clothingtype)

    clothing = Clothing(name=name, color=color)

    return render_template('add_clothes.html')

    # return render_template('setup.html')
