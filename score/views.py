from django.http import JsonResponse
from django.views import View
import pickle


class ScoreView(View):


    def get(self, *args):
        with open('modelod.pkl', 'rb') as file:
            model = pickle.load(file)
        result = model.predict()
        return JsonResponse({"by": "Andres"})
