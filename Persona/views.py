from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets

from Persona import serializers, models

# Create your views here.


class PersonaAPIView(APIView):
    serializer_class = serializers.PersonaSerializer
    """API View de prueba"""
    def get(self, request, format=None):
        """Devuelve lista """
        an_apiview = [
            'Probando metodos get,post,put,patch,delete',
            'Parecido a vista tradicional de django',

        ]    

        return Response({"message":"Hello you are in the GET part of the API",'metodo get':an_apiview})
    
    def post(self, request):
        """Crea un mensaje con nuestro nombre"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} already used a POST method in the API'
        else:
            return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)


        return Response({"message":message})

    def put(self, request, pk=None):
        """Maneja actualizar un objeto"""


        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Maneja actualizacion parcial de un objeto """

        return Response({'method':'PATCH'})
    def delete(self, request, pk=None):
        """Borra un objeto"""

        return Response({'method':'DELETE'})

class PersonaViewSet(viewsets.ViewSet):
    """Persona API View set"""

    serializer_class = serializers.PersonaSerializer

    def list(self, request):
        """Devuelve mensaje de Hola mundo"""

        a_viewset = [
            'Usa acciones (list, create, retrieve, update, partial update',
            'Automaticamente mapea a los URLs usando Routers',
            'Provee mas funcionalidad con menos codigo'
        ]

        return Response({'message': 'Hola!','a_viewset': a_viewset})

    def create(self, request):
        """Crea nuevo mensaje""" 
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hola {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors,
             status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Obtiene un objeto y su ID"""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Actualiza un objeto"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Actualiza un parcialmente un objeto"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Destruye un objeto"""
        return Response ({'http_method':'DELETE'})

class PersonaModelViewSet(viewsets.ModelViewSet):
    """Crea y actualiza personas"""
    serializer_class = serializers.PersonaModelSerializer
    queryset = models.Persona.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

        
   