from calendar import timegm

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import io
import base64
from PIL import Image
from tensorflow.keras import Sequential, Input
from tensorflow.keras.layers import Dense, Flatten,Dropout


label = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]
han_label=["비행기","자동차","새","고양이","사슴","강아지","개구리","말","배","트럭"]

from numpy.lib import recfunctions as rfn
#서버 시작시 모델 불러오기
model=None
if os.path.exists(f"{os.getcwd()}\\ai_model\\conv_model.weights.h5"):
    print(tf.__version__)
    model = Sequential()
    model.add(Input((32, 32, 3)))
    conv_1 = tf.keras.layers.Conv2D(
    16,  # 출력할 특성맵의 수량
    3,  # 합성곱을 수행할 커널 사이즈
    strides=1,
    padding='same',
    activation="relu"
    )

    model.add(conv_1)
    maxpool_1 = tf.keras.layers.MaxPool2D(
        pool_size=4,
        strides=1,
        padding='same')
    model.add(maxpool_1)
    conv_2 = tf.keras.layers.Conv2D(
        32,#출력할 특성맵의 수량
        5,#합성곱을 수행할 커널 사이즈
        strides=1,
        padding='same',
        activation="relu"
    )
    maxpool_2 = tf.keras.layers.MaxPool2D(
        pool_size=4,
        strides=1,
        padding='same')
    model.add(conv_2)
    model.add(maxpool_2)
    conv_3 = tf.keras.layers.Conv2D(
        64,
        7,
        strides=2,
        padding='same')
    model.add(conv_3)
    maxpool_3 = tf.keras.layers.MaxPool2D(
        pool_size=6,
        strides=1,
        padding='same')
    model.add(maxpool_3)

    model.add(Flatten())#완전연결층 full connection
    model.add(Dense(256,activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(32,activation="relu"))
    model.add(Dropout(0.4))
    model.add(Dense(10,activation="softmax"))
    adam = tf.keras.optimizers.Adam(
        learning_rate=0.0005,
        beta_1=0.9,
        beta_2=0.999
    )
    model.compile(loss="categorical_crossentropy",optimizer=adam,metrics=["acc"])
    model.load_weights(f"{os.getcwd()}\\ai_model\\conv_model.weights.h5")



#if os.path.exists()
def scaler_sample(img_data):
  if img_data.shape[2]==4:# png 같은 4채널은 마지막 알파채널 제거
    #new_shape = img_data.shape[0],img_data.shape[1],3
    #img_data = np.delete(img_data,3,axis=1)
    img_data = img_data[:,:,:3]#3채널로 변경
  if "int" in str(type(img_data[0][0][0])) :# int 타입인 데이터만 스케일링실행
    img_data = img_data/255.
  img_data = img_data.astype("float64")#훈련데이터와 동일한 타입으로 변경
  return img_data
  print(type(img_data[0][0][0]))
#이미지 사이즈 조정
def resize_image(target_img):
 return tf.image.resize_with_pad(
    target_img,
    32,
    32,
    method=tf.image.ResizeMethod.GAUSSIAN,
    antialias=True
)
def readImage(img_path):

    global model
    tmpimg = plt.imread(img_path)
    tmpimg = scaler_sample(tmpimg)
    x_user = []
    x_user.append(resize_image(tmpimg))
    x_users = np.array(x_user)
    y_users = model.predict(x_users)
    buffer = io.BytesIO()
    x_img = x_users[0]
    x_img*=255
    x_img=x_img.clip(0,255).astype(np.uint8)
    print(type(x_img[0][0][0]))
    Image.fromarray(x_img).save(buffer,format="png")
    timg = base64.b64encode(buffer.getvalue()).decode("utf-8")
    buffer.close()
    return {"yred":han_label[np.argmax(y_users[0])],
            "yrat":f"{int(y_users[0][np.argmax(y_users[0])]*100)}%",
            "timg":timg
            }