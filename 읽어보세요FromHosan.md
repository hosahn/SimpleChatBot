# 1. 간단히 구조부터 설명드릴게요.
 - back
 
 말 그대로 서버 파일들이 들어있습니다.
 저희 서버는 총 두가지예요.
 프론트와 직접 통신하는 NodeJS 서버, 그리고 NodeJS서버에게 데이터를 전달해주는 파이썬 Flask 서버.
 파이썬 Flask 서버는 학생들이 만든 코드로 작성한거예요. 
 app.js라는 파일이 NodeJS 서버고, back 폴더 하위에 있는 python 폴더에 여러분들이 만든 python 코드를 이용한 flask 서버가 작성되어있습니다.
 
 - front
 
 여기는 프론트엔드, 즉 웹사이트 관련 파일들이 들어있어요. 
 학생들이 하고있는 프로젝트 같은 경우는 '동적'웹사이트가 가장 보기 좋을거라고 판단해서, React라는 
 자바스크립트 언어 방식으로 정말, 정말 간단히 프로그래밍 했습니다.
 
 
 # 2. 간단한 로직 설명드릴게요.
 
 자, 우리는 프론트엔드, 즉 사용자로부터 입력을 받습니다. 입력을 받기 위한 인터페이스, 즉 화면이 front에 작성한 react 기반 html 파일들이예요.
 작성을 하고, 버튼을 누르면 http프로토콜이라는 통신 규약을 통해 미리 정해진 주소로 작성한 정보가 날아가게됩니다. 물론 주소는 서버 주소고, 제가 어떤 주소로 정보가
 날아가야 하는지는 다 설정해놨어요. 
 
 다시 돌아와서, 사용자가 전송을 누르면, 입력한 정보가 날아서 NodeJS 서버에 도착합니다. NodeJS서버는 이 요청이 유효한지(불법적인 프로그램을 쓰거나 한 건 아닌지) 또는
 기타 에러가 있는지를 간단히 파악해 줄거예요. 그리고 NodeJS 서버는 또다시 Python Flask 서버로 요청을 보냅니다. 
 
 원래는 한 서버에서 처리하는게 맞지만, 보안과 에러처리하기가 (저한테는) NodeJS가 더 유리하기때문에 두 서버를 분리했습니다. 그리고 원래 서버 요청과 데이터 처리는
 각각 분리된 공간에서 처리하는게 좋기도 하구요.
 Flask 서버는 여기서 데이터베이스같은 역할을 하신다고 보면 됩니다. NodeJS가 전달해준 정보로 그에 맞는 답을 찾고, 그것을 다시 NodeJS 서버로 보내줍니다.
 그럼 NodeJS서버가 전달받은 결과값이 유효한지 체크하고, 그걸 사용자에게 다시 보내줘요.
 
 그럼 사용자 PC가 그 전달받은 데이터로 다시 동적 사이트를 랜더링하고, 결과값이 보이게 되는거죠.
 
 
 자, 요약해서
 
 
 
 1. 사용자 (React) 정보전달 ============> NodeJS 서버 : 정보 유효성 확인 후 전달============> Flask 서버 : 정보를 바탕으로 값을 찾음(여러분들이 작성한 로직)
 2. Flask 서버 : 결과값 전달 =============> NodeJS 서버 : 결과값 유효성 확인 후 전달 =============> 사용자 (React) : 전달받은 결과값으로 웹페이지 보여주기
 
 
 의 형식이라고 이해하시고, 이따 자세히 설명드릴게요.
