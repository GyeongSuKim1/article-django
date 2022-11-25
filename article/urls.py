from django.urls import path
from article import views


urlpatterns = [
    path("", views.ArticleView.as_view()),
    path("<int:article_id>", views.ArticleView.as_view()),
    path("dp/<int:pk>", views.ArticleDetailView.as_view()),
]