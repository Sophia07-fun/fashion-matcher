from flask import Blueprint, render_template

fashion_blueprint = Blueprint ( 'fashion_blueprint',__name__,template_folder="templates" )
@fashion_blueprint.route("/",methods=['GET'])
def add_clothes():
    return render_template('add_clothes.html')

@fashion_blueprint.route("/setup",methods=['GET'])
def setup():
    return render_template('setup.html')
