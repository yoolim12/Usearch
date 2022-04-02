from flask import Flask, render_template, redirect, session, request, url_for, flash, Blueprint
from main.model import db, Preference
# import re
# from sqlalchemy import update
# app = Flask(__name__)
# from __init__ import userdb, userinfo
# from main.preference_model import preference

# pref = Blueprint('bp', __name__)
preference_api = Blueprint("preferencepage", __name__, url_prefix="/preference")

category_pred = ['문학/책', '영화', '미술/디자인', '공연/전시', '음악', '드라마', '스타/연예인', '만화/애니',
                         '방송', '일상/생각', '육아/결혼', '애완/반려동물', '좋은글/이미지', '패션/미용', '인테리어/DIY',
                         '요리/레시피', '상품리뷰', '원예/재배', '게임', '스포츠', '사진', '자동차', '취미', '국내여행',
                         '세계여행', '맛집', 'IT/컴퓨터', '사회/정치', '건강/의학', '비즈니스/경제', '어학/외국어','교육/학문']

# @app.route('/')
# def home():
#     return redirect(url_for('preference'))

@preference_api.route('/', methods=["GET", "POST"])
def preference():
    if request.method == 'POST':
        if request.form.get('pref_set'):
            pref_select = request.form.getlist('options')
            user_id = db.session.query(Preference).filter(Preference.id == session['id']).all()
            print(user_id)
            print(pref_select)
            user = Preference(id=session['id'], preference1=pref_select[0], preference2=pref_select[1], preference3=pref_select[2])
            print(type(user_id))
            if user_id != []:
                print("update")
                db.session.query(Preference).filter(Preference.id == session['id']).update({'preference1': pref_select[0], 'preference2': pref_select[1], 'preference3': pref_select[2]})
                db.session.commit()
            else:
                print("insert")
                db.session.add(user)
                db.session.commit() # session.rollback()
            return redirect(url_for('mainpage.home'))
        if request.form.get('cancel'):
            return redirect(url_for('mainpage.home'))
    else:
        # return render_template("/preference.html")
        # return render_template("preference.html", pref_select = [pref_select[0], pref_select[1], pref_select[2]])
        pref_select = list()
        preference = db.session.query(Preference).filter(Preference.id == session['id']).all()

        if len(preference) != 0:
            preference = preference[0]
            pref_select.append(category_pred.index(preference.preference1)+1)
            pref_select.append(category_pred.index(preference.preference2)+1)
            pref_select.append(category_pred.index(preference.preference3)+1)

        return render_template("/preference.html", pref_select=pref_select)


