from django.http import JsonResponse
from django.views import View
from .models import Scores
import pickle
import numpy as np


class ScoreView(View):

    # def get(self, *args):
    #     with open('modelod.pkl', 'rb') as file:
    #         model = pickle.load(file)
    #     x = np.array([[5.1, 3.5, 1.4, 0.2]])
    #     result = model.predict(x)
    #     return JsonResponse({'score': f'{result}', 'origin': 'Andres Zapata', 'date': 'hoy'})

    def get(self, *args):
        score_object = Scores.objects.filter(pk=1).first()
        return JsonResponse({'score': f'{score_object.score}', 'origin': f'{score_object.origin}', 'date': f'{score_object.date}'})
