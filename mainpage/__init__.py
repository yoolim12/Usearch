from flask import Flask, render_template, redirect, session, request, url_for, flash, jsonify, Blueprint
from main.model import *
from sqlalchemy.sql import func

mainpage_api = Blueprint("mainpage", __name__, url_prefix="/")

@mainpage_api.route("/")
def home():
    # session['logged_in'] = False
    if session.get('logged_in'):
        return redirect(url_for('mainpage.main'))
    else:
        return redirect(url_for('mainpage.login'))

@mainpage_api.route('/login', methods=['GET', 'POST'])
def login():
    global userinfo
    
    if request.method == 'POST':
        if request.form.get("login"):
            id = request.form.get('id')
            password = request.form.get('password')
            print(id)
            print(password)

            try:
                user_id = db.session.query(Account).filter(Account.ID == id).all()
                print(type(user_id))
                print(user_id)
                if user_id != []:
                    # 비밀번호 검증 후 일치하는 경우 초기 페이지로 이동하세요.
                    session['logged_in'] = True
                    session['id'] = user_id[0].ID
                    session['password'] = user_id[0].password
                    session['name'] = user_id[0].name
                    session['birth'] = str(user_id[0].birth)
                    session['email'] = user_id[0].email
                    session['gender'] = user_id[0].gender
                    print(session['id'])
                    print(session['password'])
                    print(session['name'])
                    return redirect(url_for('mainpage.home'))
            except:
                flash("아이디 또는 비밀번호가 올바르지 않습니다.")
                return redirect(url_for('mainpage.login'))
        if request.form.get("register"):
            return redirect(url_for("mainpage.register"))
    else:
        return render_template('login.html')

@mainpage_api.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print('COME POST')
        if request.form.get('query_id_check'):
            id = request.form.get('id')
            ids = db.session.query(Account).filter(Account.ID==id).all()
            if len(ids) != 0:
                flash("중복된 아이디 입니다.")
                return render_template('registerpage.html', exist_id='')
            else:
                flash("사용가능한 아이디 입니다.")
                return render_template('registerpage.html', exist_id=id)
        print("pASS IDCHECK")
        if request.form.get('query_regist'):
            print("COME HERER")
            # username을 key, password를 value로 하여 userinfo 리스트에 추가하세요.
            id = request.form.get('id')
            name = request.form.get('name')
            password = request.form.get('password')
            password_check = request.form.get('passwordcheck')
            name = request.form.get('name')
            birth = request.form.get('birth')
            gender = request.form.get('gender')
            email = request.form.get('email')

            if password == password_check:
                members = Account(name, id, password, gender, birth, email)
                db.session.add(members)
                db.session.commit()

                session['id'] = id
                session['password'] = password
                session['name'] = name
            
                # return redirect(url_for('mainpage.login'))
                return redirect(url_for('preferencepage.preference'))
            else:
                flash("비밀번호가 일치하지 않습니다.")
                return redirect(url_for('mainpage.register'))
    else:
        return render_template('registerpage.html', exist_id='')

@mainpage_api.route('/logout')
def logout():
    # https://ohdowon064.tistory.com/123
    session['logged_in'] = False
    session.pop('id')
    session.pop('password')
    session.pop('name')
    session.pop('birth')
    session.pop('email')
    session.pop('gender')
    return redirect(url_for('mainpage.home'))

@mainpage_api.route("/main", methods=["GET", "POST"])
def main():
    # return redirect(url_for('usercategory'))
    if request.method == 'POST':
        if request.form.get("mainpage.logout"):
            session['logged_in'] = False
            return redirect(url_for('mainpage.home'))
        if request.form.get("preference"):
            return redirect(url_for("preference"))
        if request.form.get("information"):
            return redirect(url_for("correct_information"))
        if request.form.get("searchbtn"):
            session['keyword'] = request.form.get('keyword')
            return redirect(url_for("resultpage.result"))
    else:
        return render_template('mainpage.html', username = session['name'])


# @mainpage_api.route('/home')
# def home():
#     return render_template('home.html')
    
# @mainpage_api.route("/one")
# def home():
# 	member = Members.query.first()
# 	return 'Hello {0}, {1}, {2}, {3}, {4}'\
# 		.format(member.name, member.email, member.phone, member.start.isoformat(), member.end.isoformat())
# 	#return render_template('home.html')
    
# @mainpage_api.route('/all')
# def select_all():
#     members = Members.query.all()
#     return render_template('db.html', members=members)
