
import hashlib

class Member:

    def __init__(self, name, id, pw,):
        self.name = name
        self.id = id
        self.pw = pw

    def display(self):
        print(f'name: {self.name}, ID: {self.id}')


class Post():
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        # if post.author == eunkyu.name:
        print(f'title: {self.title} author: {self.author}')

# eunkyu.display()
# juhee.display()


members = []
posts = []


eunkyu = Member(name='이은규', id='eunkyu22', pw=123456)
juhee = Member(name='이주희', id='juheelee', pw=456789)
mingogi = Member(name='민고기', id='mingogi', pw=999999)

members.append(eunkyu)
members.append(juhee)
members.append(mingogi)
# ps:   여러 값을 한 번에 추가 할때 >>   members.extend([eunkyu, juhee, mingogi])
# ps:   extend(주의 리스트를 닮을때 [] 감싸줘야함 )

# for member in members:
#     member.display()


# append를 해주기 위해 매개변수(회원)를 만들어주고 (처음에 소괄호랑 [헷갈려서 ]) 에러가 났었다.
# 그리고 포문을 돌면서 회원들을 출력해주기 위해 만들어둔 메소드 .display로 돌려줬다.
# 왜래키

eunkyu_post = Post(title='곧 삼일절', content='삼일절에는 코딩이다', author=eunkyu.name)
mingogi_post = Post(
    title='난 고기가 좋다', content='이번주는 흑돼지를 먹었는데 아주 분위기가 좋았다.', author=mingogi.name)
eunkyu_post2 = Post(
    title='이게 맞을까?', content='이게 맞는지 모르겠지만 계속 해보는데까지 생각을 해보자', author=eunkyu.name)
juhee_post = Post(
    title='생각에 생각을', content='계속 꼬리에 꼬리를 물다보면 결국엔 풀린다', author=juhee.name)
mingogi_post2 = Post(
    title='나는 천재 해커다', content='오늘 좀 피곤한데 해결할때 까지 놓지 못한다', author=mingogi.name)
juhee_post2 = Post(title='다중 분신술!', content='세명의 그림자를 소환했다', author=juhee.name)
eunkyu_post3 = Post(title='재미가 있다', content='해결했다..', author=eunkyu.name)
mingogi_post3 = Post(title='나는 천재 해커다', content='내가 마음만 먹으면 뭐든 만들고 뭐든 뚫는다!', author=mingogi.name)
juhee_post3 = Post(title='분신술이 끝나간다 . . ',content='나는 천천...재재...나루토', author=juhee.name)


# TypeError: __init__ missing 2 required positional arguments: content and author : 자꾸 인수 2개가 누락 되었다고 해서 멤버클래스를 상속해줬는데도 안됌 ~
#         ::그래서 이닛에 인자로 추가 해줬는데 ~ ? 이번엔 3개 타이틀까지 모두 누락 되었다고 뜸. 흠...
#         :::틀린점 포스트를 작성하는 인스턴스 문법이 틀렸다.. 쳌!!


posts.extend([eunkyu_post, eunkyu_post2, eunkyu_post3, mingogi_post, mingogi_post2, mingogi_post3, juhee_post, juhee_post2, juhee_post3])


# for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
# 내가 생각했던게 맞았다. 근데 author의 이름 지정 방식에서 문제가 있었다. 왜래키? 라는게 있다는데 일단 나는 .name으로 저장
# 이 조건문을 위에 디스플레이 메소드로 적용시켜서 깔끔하게 정리해보자. 완료

# for post in posts:
#     post.display()


# for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요
# 특정단어를 포함시키는 문법이 생각이안난다!!!
# 포스트.콘텐트 안에 '해' 라는 단어가 포함되면 타이틀을 뽑아줘. 해결
# for post in posts:
#     if '해' in post.content:
#         print(post.title)

name = input("이름 임력 후 Enter: ")
user_id = input("ID 입력 후 Enter: ")
password = input("비밀번호 입력 후 Enter: ")

new_add_member = Member(name=name, id=user_id, pw=password)
members.extend([new_add_member])

print("순서대로 Post를 작성하세요")
add_title = input("Post의 제목 입력 후 Enter")
add_content = input("Post의 내용 입력 후 Enter")
add_author = new_add_member


new_add_post = Post(title=add_title, content=add_content, author=add_author)
posts.extend([new_add_post])


# TypeError: 'list' object is not callable 터미널에서 포스트 입력 후 객체를 호출 할수 없다는 에러가뜸.
# : 헷갈린다 ... 에러 이게 뭘까  posts << 가아니라 Post 였음 쉽게 말해 매개변수 포스츠가 아니라 클래스 포스트 였음. 해결완료
# :: 해결 .... append를 써서 추가 해보니 됬다. 알고보니 리스트를 추가할때는 append 를 써야하는데  extend 같이 전체를 아우르는 경우 []중괄호로 감싸줘야함.
