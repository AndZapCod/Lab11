from django.contrib import admin
from score.models import Scores


class ScoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Scores, ScoreAdmin)