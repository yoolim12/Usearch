from flask import Flask, render_template, redirect, session, request, url_for, flash, Blueprint
from main.model import db, Preference

correct_infor_api = Blueprint("correct_information", __name__, url_prefix="/correct_information")

@correct_infor_api.route('/', methods=["GET", "POST"])
def main():
    if request.method == 'POST':
        if request.form.get('correct'):
            password = request.form.get('password')
            name = request.form.get('name')
            birth = request.form.get('birth')
            gender = request.form.get('gender')
            email = request.form.get('email')
            '''
            update please I cannot type korean
            '''
            return redirect(url_for('loginpage.home'))
        if request.form.get('cancel'):
            return redirect(url_for('loginpage.home'))
    else:
# def main():
        info = {
            'name':session['name'],
            'birth':session['birth'],
            'email':session['email'],
            'gender':session['gender'],
        }

        return render_template("/correct_information.html", info=info)


