from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
rot = DefaultRouter()
rot.register('qq', views.Khaled)

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    path('khaled/', include(rot.urls)),
    path('react/', views.ReactAppView.as_view(), name='react')
]