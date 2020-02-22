from django.urls import path
from .views import IndexView, RepositoryView


urlpatterns = [
    path('', IndexView.as_view()),
    path('repository/', RepositoryView.as_view()),
]
