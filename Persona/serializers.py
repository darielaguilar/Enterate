from rest_framework import serializers
from Persona import models

class PersonaSerializer(serializers.Serializer):
    """Serializa un campo para probar luego se utiliza en un metodo post"""

    name = serializers.CharField(max_length=10)

class PersonaModelSerializer(serializers.ModelSerializer):
    """Serializa objetos de Persona"""

    class Meta:
        
        model = models.Persona
        fields = ('name','email','ip','avatar')

    def create(self, validated_data):
        """Crea y devuelve nueva Persona"""
        persona = models.Persona.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            ip=validated_data['ip'],
            avatar=validated_data['avatar'])

        return persona
    
    def update(self, instance, validated_data):
        """Actualiza y devuelve una instancia de Persona , dada la informacion validada"""
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance