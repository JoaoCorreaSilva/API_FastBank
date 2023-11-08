from rest_framework import serializers
from App_Fast_Bank import models

class TransacaoSerializer(serializers.ModelSerializer):

    conta_cliente = serializers.CharField()

    class Meta:  # Classe interna
        model = models.Transacao
        fields = '__all__'

    def create(self, validated_data):
        conta_cli = validated_data.pop('conta_cliente')
        cliente_instance, created = models.Cliente.objects.get_or_create(conta=conta_cli)
        transacao_instance = models.Transacao.objects.create(**validated_data, conta_cliente=cliente_instance)
        return transacao_instance


class ClienteSerializer(serializers.ModelSerializer):

      class Meta:  # Classe interna
            model = models.Cliente
            fields = '__all__'

#Validações de entrada nos campos podem ser consultadas em Validators
# https://django-rest-framework.org/api-guide/validators/