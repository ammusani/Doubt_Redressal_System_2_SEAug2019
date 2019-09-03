from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
	# path('admin', admin.site.urls),
    path('', views.index, name='index'),

=======
    path('', views.index, name='index'),
>>>>>>> 2e32c2472bf41fcdddbabe04478545049f0e8299
]