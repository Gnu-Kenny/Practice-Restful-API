## restful 규칙

> 홈 경로/복수 명사/  
> ex) 127.0.0.1:8000/users

<br>

django-admin super user 회원가입 필요

```
python3 manage.py createsuperuser
```

- django REST framework 로그인 가능해짐.

<br>

## UserSerializer

- data를 JSON형태로 만들어줌.

<br>

## router.register(r'users', UserViewSet)

->users를 실행시키면 ViewSet을 실행시킴.

## ORM(Oject Relational Mapping)

> Framwork에서 모델을 만들면 연동된 DB에
> 자동으로 테이블을 만들어줌.

장점 : 연동된 DB에 자동으로 테이블들을 생성해주고 프레임워크 내의 메소드로 퀘리를 짤 수 있어 개편함.  
단점 : sql이 익숙하면 새로 배워야해서 불편

## restframework 만들때 순서

1. model 설계 (ERD 설계)
2. model -> serializer (이름, 전화, 주소 등을 필드로 JSON 형식화함.)
3. url [~/addresses] -> 주소록 model을 가져오는 url

<br>

## MVC 패턴

\*일반적\*

- **Model** : 데이터 형식
- **View** : 보여주는 곳
- **Control** : 데이터를 가공하는 곳

\*장고\*

- **Model** : 데이터 형식
- **Template** : 보여주는곳
- **View** : 데이터 가공하는 곳

## startproject vs startapp

> 하나의 Project가 하나의 Website라고 생각하면된다.  
> Project안에는 다양한 기능들이 있고, 어떤 의미있는 기능들을 App으로 관리한다.

<br>

## [views]

```python
elif request.method == 'POST':
        data = JSONParser().parse(request) 	#client에서 온 데이터들을 변수 data에 parsing 함
        serializer = AddressesSerializer(data=data)	#앞에 data가 model에서 설계된 형태 뒤의 data가 client에서 받아온 데이터 형태 일치하면 is_valid =True
        if serializer.is_valid():
            serializer.save()	#save => object를 만듦
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)
```

- ### 어떤 url로 view의 address_list를 호출할것인가

views에서 함수 사용할때

@csrf_exempt 의미 : 뷰에 토큰이 필요하지 않다는 것