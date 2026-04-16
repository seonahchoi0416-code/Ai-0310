from ai_model.conv_ai import readImage
def model_pred(file_path):
     #file_path : 업로드된 이미지 전체 경로
     result= readImage(file_path)
     return result
