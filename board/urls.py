from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:board_id>/comment/create/',
         views.comment_create, name='comment_create'),
    path('<int:board_id>/comment/<int:comment_id>/delete/',
         views.comment_delete, name="comment_delete"),
]
