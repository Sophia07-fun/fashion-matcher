from flask import Blueprint, render_template

fashion_blueprint = Blueprint ( 'fashion_blueprint',__name__,template_folder="templates" )
@fashion_blueprint.route("/",methods=['GET'])
def add_clothes():
    return render_template('add_clothes.html')

@fashion_blueprint.route("/setup",methods=['GET'])
def setup():

    if request.args.lengh > 0:
        preference = request.args['contrast']
        return redirect(url_for('fashion_blueprint.add_clothes'))
    return render_template('setup.html')

@fashion_blueprint.route("/setup",methods=['POST'])
def setup_user():
    return render_template('setup.html')
