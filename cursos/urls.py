from django.urls import path
from cursos.views import CursoAPIView, AvaliacaoAPIView

urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]