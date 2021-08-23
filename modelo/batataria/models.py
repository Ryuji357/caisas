from django.db import models

# Create your models here.

class cliente(models.Model):
    nome = models.CharField(max_length=200)

class produto(models.Model):
    codigo = models.CharField(max_length=5)
    descricao = models.CharField(max_length=200)

class pedido(models.Model):
    fk_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)

class produto_to_pedido(models.Model):
    fk_pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    fk_produto = models.ForeignKey(produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2)