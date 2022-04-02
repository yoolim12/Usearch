import numpy as np

CATEGORIES = {'문학/책': 0, '영화': 0, '미술/디자인': 0, '공연/전시': 0, '음악': 0, '드라마': 0, '스타/연예인': 0, '만화/애니': 0,
              '방송': 0, '일상/생각': 0, '육아/결혼': 0, '애완/반려동물': 0, '좋은글/이미지': 0, '패션/미용': 0, '인테리어/DIY': 0,
              '요리/레시피': 0, '상품리뷰': 0, '원예/재배': 0, '게임': 0, '스포츠': 0, '사진': 0, '자동차': 0, '취미': 0, '국내여행': 0,
              '세계여행': 0, '맛집': 0, 'IT/컴퓨터': 0, '사회/정치': 0, '건강/의학': 0, '비즈니스/경제': 0, '어학/외국어': 0, '교육/학문': 0}

STAR = [4, 6, 8]
FOOD = [15, 16, 25]


class SearchResultSorter:
    def __init__(self, model):
        self.model = model

    # fasttext를 사용할 때 카테고리에 붙는 __label__을 제거
    def remove_label(self, pred):
        clear_pred = []
        for x in pred:
            try:
                x = x.replace('_', '').replace('label', '')
                clear_pred.append(x)
            except:
                continue
        return clear_pred

    def sort_search_list(self, result, user_preference):

        user_rate = self.get_user_rate(user_preference)

        for i, x in enumerate(result):
            pred_title = self.model.predict(x["title"], k=32)
            pred_content = self.model.predict(x["description"], k=32)
            
            pred_category = pred_title[0]
            pred_category = self.remove_label(pred_category)

            for j in range(32):
                # CATEGORIES[pred_category[j]] = pred_title[1][j] + pred_content[1][j]
                CATEGORIES[pred_category[j]] = pred_title[1][j]

            category_pred_value = list(CATEGORIES.values())
            result[i]["pred"] = self.get_preference(category_pred_value, user_rate)

        result = sorted(result, key=lambda content: (-content['pred'], content['title']))

        return result

    # 사용자의 카테고리별 선호도를 바탕으로 검색 결과의 선호도를 유추
    def get_preference(self, category_pred_value, user_rate):
        user_rate_np = np.array(user_rate).flatten()
        category_pred_value_np = np.array(category_pred_value).flatten()

        return np.dot(category_pred_value_np, user_rate_np)

    def get_user_rate(self, user_preference):
        user_rate = list()
        category_list = list(CATEGORIES.keys())
        user_preference = user_preference[0]
        user_preference = [user_preference.preference1,user_preference.preference2,user_preference.preference3]
        
        for x in category_list:
            if x in user_preference:
                user_rate.append(1)
            else:
                user_rate.append(-1)

        # print("User interest")
        # for x in range(32):
        #     print(f"{category_list[x]}: {user_rate[x]}, ", end='')
        #     if x % 5 == 4:
        #         print("\n")
        # print("\n")

        print("Top-3 user interest")
        top3_idx = select_top_k(user_rate, 3)
        for idx in top3_idx:
            print(f'{category_list[idx]}: {user_rate[idx]}, ', end='')
        print('\n')

        return user_rate


def select_top_k(_list, k=3):
    return sorted(range(len(_list)), key=lambda i: _list[i])[-k:]
