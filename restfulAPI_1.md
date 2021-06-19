## Restful API

---

### 1. url을 어떻게 쓸것인가 -> url 규칙이있다.

ex)  
http://~/members/1  
http://~/clubs/

### 2. CRUD 호출할때 방식을 하나로 통일하자.

> Create : 생성(POST)  
> Read : 조회(GET)  
> Update : 수정(PUT)  
> Delete : 삭제(DELETE)

ex)  
~/member/1 GET  
~/member/1 PUT

<br>
<br>

## 가상환경을 왜 쓰는지?

---

개발을 하다보면 프로젝트 별로 쓰는 라이브러리들의 각기 다른 버전들을 사용해야할
경우가 생기기때문에 사용한다.

<br>

## Django

---

> pip : 라이브러리를 설치해주는 유틸리티  
> django-admin 장고 기본 명령어 이자 다른 명령어들을 알려줌  
> django-admin startproject <projectname>

<br>

### ALLOWED_HOSTS = ['ip주소,url주소']

- 접근 권한 설정

<br>

### runserver 127.0.0.1:8000 -> local

### rumserver 0.0.0.0:8000 -> 외부에서도 이 포트로 들어올수있음
