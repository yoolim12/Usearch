from pprint import pprint as pp

from src.recommender import SearchResultRecommender

if __name__ == '__main__':
    recommender = SearchResultRecommender()

    keyword = input('검색어를 입력하세요 ')
    search_results = recommender(keyword)

    pp(search_results[:3])
