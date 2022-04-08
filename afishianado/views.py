from django.shortcuts import render
from .forms import InputForm
import pickle
import os
from sklearn.preprocessing import PolynomialFeatures


def index(request):
    formsub = InputForm()
    context = {'form': formsub}
    if request.method == 'POST':
        es = dict(request.POST)
        for x in list(es.values()):
            if x == "":
                return render(request, '../templates/form.html', context=context)
        pt = {"length1": es["vertical_length"][0], "length2": es["diagnal_length"][0], "length3": es["cross_length"][0],
              "height": es["height"][0], "width": es["width"][0], "species_Bream": 0, "species_Parkki": 0,
              "species_Perch": 0, "species_Pike": 0, "species_Roach": 0, "species_Smelt": 0, "species_Whitefish": 0}
        pt['species_' + es['species'][0]] = 1
        inp = [[float(x) for x in list(pt.values())]]

        def poly_feature(features, degree_):
            poly = PolynomialFeatures(degree=degree_)
            return poly.fit_transform(features)

        inp = poly_feature(inp, 2)
        try:
            module_dir = os.path.dirname(__file__)
            file_path = os.path.join(module_dir, '../static/RANSACRegressor_model.sav')
            loaded_model = pickle.load(open(file_path, 'rb'))
            y_pred = loaded_model.predict(inp)[0]
            if y_pred < 0:
                return render(request, '../templates/error.html',context={"species": es['species'][0]})
            return render(request, '../templates/output.html',
                          context={"species": es['species'][0], "weight": "{:.2f}".format(y_pred),"csrfviewmiddleware":})
        except Exception as e:
            print(e)
            return render(request, '../templates/form.html', context=context)
    else:
        return render(request, '../templates/form.html', context=context)
