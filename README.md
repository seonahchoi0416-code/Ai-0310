# 1. 이미지 다중 분류 모델 구성하기
 - 딥러닝 기술 : google tensorflow (keras)
 - 전처리스케일링 : min-maz scale
 - 이미지 리사이징 : resize_with_pad (32*32 3channel 이미지)
 - 훈련데이터 : cifar10
 - 이미지 라벨 : label = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]
 - 이미지 한글라벨 : han_label = ["비행기","자동차","새","고양이","사슴","강아지","개구리","말","선박","트럭"]
 - 서비스 서버:Flask
 - 통신데이터유형 : json/dict
 - 특징 : conv2D and MaxPOOL_2D 사용으로 특성맵 추출과 풀링층을 거쳐 과대적합 방지
### 디렉토리 구조 : 
<pre>
  portfolio260409(root)
  ㄴai_model
    ㄴai_interface.py(모델인터페이스)
    ㄴconv_ai.py(모델 로딩 및 분석기)
  ㄴstatic
    ㄴapp
        ㄴ index.js(클라이언트 스크립트 파일)
    ㄴ css
        ㄴ index.css( 클라이언트 모양설정)
    ㄴimages  (메일 페이지 이미지 파일)
    ㄴ temp (예측 업로드 파일)
  ㄴ templates
    ㄴ index,html(메인페이지)
  ㄴ web_service.py(web route)
</pre>
