from django.urls import path
#このドットはこのファイルのあるディレクトリのすべてという意味。
#これでフォルダ内のすべてのビューをインポートしている。
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
