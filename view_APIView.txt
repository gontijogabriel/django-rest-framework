from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cursos.models import Curso, Avaliacao
from cursos.serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    Cursos
    """
    def get(self, request, pk=None):
        if pk is not None:
            curso = self.get_object(pk)
            serializer = CursoSerializer(curso)
            return Response(serializer.data)
        else:
            cursos = Curso.objects.all()
            serializer = CursoSerializer(cursos, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        curso = self.get_object(pk)
        serializer = CursoSerializer(curso, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        curso = self.get_object(pk)
        curso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_object(self, pk):
        try:
            return Curso.objects.get(pk=pk)
        except Curso.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AvaliacaoAPIView(APIView):
    """
    Avaliações
    """
    def get(self, request, pk=None):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        avaliacao = self.get_object(pk)
        serializer = AvaliacaoSerializer(avaliacao, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        avaliacao = self.get_object(pk)
        avaliacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_object(self, pk):
        try:
            return Avaliacao.objects.get(pk=pk)
        except Avaliacao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)