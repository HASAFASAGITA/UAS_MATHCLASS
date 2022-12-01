from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('materimtk/', views.materimtk, name='materimtk'),
    path('sejarahmtk/', views.sejarahmtk, name='sejarahmtk'),
    path('tokohmtk/', views.tokohmtk, name='tokohmtk'),
    path('soallatihan/', views.soallatihan, name='soallatihan'),
    path('webpembahasan/', views.webpembahasan, name='webpembahasan'),
]