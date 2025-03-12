from django.urls import path
from .views import PageScrapperViews
urlpatterns = [
    path('scrapper',PageScrapperViews.as_view(),name='pagescrapper.view'),
    path('scrapper/<int:pk>',PageScrapperViews.as_view(),name="pagescrapper.view")
]