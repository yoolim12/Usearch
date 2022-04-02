from flask import Blueprint, session, request, render_template
from main.model import db, Preference
from ml.src.recommender import SearchResultRecommender

result_api = Blueprint('resultpage', __name__, url_prefix='/result')

srr = SearchResultRecommender()

@result_api.route('/')
def result():
    user_preference = db.session.query(Preference).filter(Preference.id == session['id']).all()
    # keyword = param.args('keyword')
    # keyword = request.form.get('search')
    # keyword = '레드벨벳'
    keyword = session['keyword']

    search_list = srr(keyword, user_preference)
    # print("search: ",search_list)

    title = []
    description = []
    thumbnailUrl = []
    link = []

    for dictionary in search_list:
        title.append(dictionary['title'])
        description.append(dictionary['description'])
        link.append(dictionary['link'])
        if dictionary['thumbnailUrl'] == 'NoImage':
            thumbnailUrl.append('https://www.nativespeakeronline.com/wp-content/uploads/2013/06/no_not2.png')
        else:
            thumbnailUrl.append(dictionary['thumbnailUrl'])

    from pprint import pprint as pp
    pp(search_list[:3])

    return render_template('searchresult.html', title=title, description=description, thumbnailUrl=thumbnailUrl, link=link, keyword=keyword)