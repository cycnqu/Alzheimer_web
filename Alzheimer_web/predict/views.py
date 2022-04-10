from django.shortcuts import render
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from upload.models import Upload_Image
import keras.backend as K
import tensorflow as tf
from keras.preprocessing import image
import numpy as np
from django.contrib.auth.decorators import login_required
# prediction page
@login_required(login_url='/login')
def prediction(request):
    #R_model_evaluate()
    #M_model_evaluate()
    latest_image = Upload_Image.objects.last()
    test_image=latest_image.image.url 
    #print(test_image)
    R_pred = R_model_predict(test_image)
    M_pred = M_model_predict(test_image)
    D_pred = D_model_predict(test_image)
    return render(request,'predict.html',locals())



# ResNet evaluate
def R_model_evaluate():

    #def f1 score
    def f1_score(y_true, y_pred): #taken from old keras source code
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        recall = true_positives / (possible_positives + K.epsilon())
        f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
        return f1_val
    #scores metrics
    METRICS = [
      tf.keras.metrics.BinaryAccuracy(name='accuracy'),
      tf.keras.metrics.Precision(name='precision'),
      tf.keras.metrics.Recall(name='recall'),  
      tf.keras.metrics.AUC(name='auc'),
      f1_score,
    ]
    #load model and evaluate
    R_model = load_model('static/models/Resnet_smote_20211228.hdf5',custom_objects={'f1_score' :f1_score})
    test_datagen  = ImageDataGenerator(rescale = 1./255)
    test_dataset = test_datagen.flow_from_directory(directory='static/images/Alzheimer_sDataset/test',target_size=(224,224),class_mode='categorical',batch_size=30)
    scores = R_model.evaluate(test_dataset)
    print('pass')
    print("Accuracy = ", scores[1]) # Accuracy =  0.9462470412254333
    print("Precision = ", scores[2]) # Precision =  0.8958990573883057
    print("Recall = ", scores[3])   # Recall =  0.8881939053535461  
    print("AUC = ", scores[4])  # AUC =  0.9774209856987
    print("F1_score = ", scores[5]) # F1_score =  0.892345666885376
#def f1 score
def f1_score(y_true, y_pred): #taken from old keras source code
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        recall = true_positives / (possible_positives + K.epsilon())
        f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
        return f1_val
def R_model_predict(test_image):
    #preds_class =['MildDemented','ModerateDemented','NonDemented','VeryMildDemented']
    R_model = load_model('static/models/Resnet_smote_20211228.hdf5',custom_objects={'f1_score' :f1_score})
    img_path ='.'+test_image
    print(img_path)
    img = image.load_img(img_path,target_size=(224,224))
    x = image.img_to_array(img)
    x = np.expand_dims(x,axis=0)
    preds = R_model.predict(x)
    print('_predicted:',preds)
    Alzheimer_class ={'NonDemented':preds[0][0],'VeryMildDemented':preds[0][1],'MildDemented':preds[0][2],'ModerateDemented':preds[0][3]}
    answer = max(Alzheimer_class, key=Alzheimer_class.get)
    print('R_which possible:',answer,"{0:.0%}".format(preds.max()))
    return answer

def M_model_predict(test_image):
    #preds_class =['MildDemented','ModerateDemented','NonDemented','VeryMildDemented']
    M_model = load_model('static/models/smote_mobile.h5',custom_objects={'f1_score' :f1_score})
    img_path ='.'+test_image
    print(img_path)
    img = image.load_img(img_path,target_size=(224,224))
    x = image.img_to_array(img)
    x = np.expand_dims(x,axis=0)
    preds = M_model.predict(x)
    print('M_predicted:',preds)
    Alzheimer_class ={'NonDemented':preds[0][0],'VeryMildDemented':preds[0][1],'MildDemented':preds[0][2],'ModerateDemented':preds[0][3]}
    answer = max(Alzheimer_class, key=Alzheimer_class.get)
    print('M_which possible:',answer,"{0:.0%}".format(preds.max()))
    return answer


def D_model_predict(test_image):
    #preds_class =['MildDemented','ModerateDemented','NonDemented','VeryMildDemented']
    D_model = load_model('static/models/smote_dense.h5',custom_objects={'f1_score' :f1_score})
    img_path ='.'+test_image
    print(img_path)
    img = image.load_img(img_path,target_size=(224,224))
    x = image.img_to_array(img)
    x = np.expand_dims(x,axis=0)
    preds = D_model.predict(x)
    print('D_predicted:',preds)
    Alzheimer_class ={'NonDemented':preds[0][0],'VeryMildDemented':preds[0][1],'MildDemented':preds[0][2],'ModerateDemented':preds[0][3]}
    answer = max(Alzheimer_class, key=Alzheimer_class.get)
    print('D_which possible:',answer,"{0:.0%}".format(preds.max()))
    return answer


# MobileNet evaluate
def M_model_evaluate():
    import tensorflow as tf
    import keras.backend as K
    #def f1 score
    def f1_score(y_true, y_pred): #taken from old keras source code
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        recall = true_positives / (possible_positives + K.epsilon())
        f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
        return f1_val
    #scores metrics
    METRICS = [
      tf.keras.metrics.BinaryAccuracy(name='accuracy'),
      tf.keras.metrics.Precision(name='precision'),
      tf.keras.metrics.Recall(name='recall'),  
      tf.keras.metrics.AUC(name='auc'),
      f1_score,
    ]
    #load model and evaluate
    R_model = load_model('static/models/smote_mobile.h5',custom_objects={'f1_score' :f1_score})
    test_datagen  = ImageDataGenerator(rescale = 1./255)
    test_dataset = test_datagen.flow_from_directory(directory='static/images/Alzheimer_sDataset/test',target_size=(224,224),class_mode='categorical',batch_size=30)
    scores = R_model.evaluate(test_dataset)
    print('pass')
    print("Accuracy = ", scores[1]) # Accuracy =  0.9407740235328674
    print("Precision = ", scores[2]) # Precision =  0.8836477994918823
    print("Recall = ", scores[3])   # Recall =  0.8788115978240967  
    print("AUC = ", scores[4])  # AUC =  0.9749141335487366
    print("F1_score = ", scores[5]) # F1_score =  0.8811036944389343
    




    
    
      
    






