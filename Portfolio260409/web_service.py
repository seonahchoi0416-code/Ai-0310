from flask import Flask,render_template,jsonify,request
from ai_model.ai_interface import model_pred

app = Flask(__name__)
#C:\Users\itg\PycharmProjects\Portfolio260409
ROOT_PATH = app.root_path
@app.route("/")
def root_page(): #첫페이지
    return render_template("index.html")
@app.route("/service/<param>")
def service(param): #각 메인 페이지
    print(param)

@app.route("/option/<optparam>",methods=["post"])
def option_service(optparam): #각 요청수신
    print(optparam)
    print(request.files["user_img"])
    #이미지 이름
    file = request.files["user_img"]
    fname = file.filename
    fpath=f"{ROOT_PATH}/static/temp/{fname}"
    file.save(fpath)
    print(fpath)
    result = model_pred(fpath)#모델에 파일 이름 넘기기
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)

