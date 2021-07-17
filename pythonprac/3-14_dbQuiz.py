from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


# 한 개 찾기 - 예시
movie = user = db.movies.find_one({'title':'매트릭스'},{'_id':False})
print(movie['star'])

target_star = movie['star']

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
target_movies = list(db.movies.find({'star':target_star},{'_id':False}))
for target in target_movies:
    print(target['title'])

db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': '0'}})

