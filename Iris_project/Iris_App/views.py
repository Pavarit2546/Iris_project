from django.shortcuts import render
import pickle
import numpy 
import pandas as pd
from joblib import load
import sklearn


#Load your model here
model = load('IRIS_Dtree_model.joblib')
# Create your views here.
def homepage(request):

    if request.method == 'POST':
        try:
            SepalLengthCm = float(request.POST['SepalLengthCm'])
            SepalWidthCm = float(request.POST['SepalWidthCm'])
            PetalLengthCm = float(request.POST['PetalLengthCm'])
            PetalWidthCm = float(request.POST['PetalWidthCm'])
            
            data = {
                'sepal length (cm)': [SepalLengthCm],
                'sepal width (cm)': [SepalWidthCm],
                'petal length (cm)': [PetalLengthCm],
                'petal width (cm)': [PetalWidthCm]
            }
            
            df = pd.DataFrame(data)

            #inp = numpy.array([ [SepalLengthCm, SepalWidthCm, PetalLengthCm , PetalWidthCm] ])
            prediction = model.predict(df)
            #percent_iris = round(prediction[0][0])
            result = ""
            if prediction == 0 :
                result = "setosa"
            elif prediction == 1 :
                result = "versicolor"
            else:
                result = "virginica"
            context = {
                'result' : result
            }
            return render(request, "index.html", context)
 
        except (ValueError, KeyError) as e:
            context = {
                'result': "An error has occurred: " + str(e)
            }
            return render(request, "index.html", context)
 
    return render(request, "index.html")