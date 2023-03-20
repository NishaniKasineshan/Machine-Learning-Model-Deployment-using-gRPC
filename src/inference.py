import tensorflow as tf
from PIL import Image
import numpy as np
import io

#upload the model
Model=tf.keras.models.load_model("model.h5")

#classes to be predicted
class_names=["cls_0","cls_1","cls_2"]

#Function defined to prepare the image for inference
def preprocess(image):
    #predict expect batch of images
    #in order to predict for only one image we should expand the dimensions
    img=np.expand_dims(image,axis=0)
    return img

def inference(image):
    img=preprocess(image)
    predictions=Model.predict(img)
    pred_cls=class_names[np.argmax(predictions[0])]
    pred_confidence=np.max(predictions[0])
    preds={'class':pred_cls,'confidence':float(pred_confidence)}
    return preds

if __name__=="__main__":
   img_path='XXX.JPG'
   img=preprocess(img_path)
   print(inference(img))
    
