from django.urls import path
from . import views
from .views import CharacterList

urlpatterns = [
    path('characters/', CharacterList.as_view(), name='character-list')
]