from django.urls import path
from . import views

app_name = 'chains'
urlpatterns = [
    path('', views.index, name='index'),
    path('view_chain/<int:story_id>/', views.view_chain, name='view_chain'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
