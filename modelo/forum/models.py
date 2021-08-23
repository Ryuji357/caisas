from django.db import models

# Create your models here.

class usuario(models.Model):
    nome = models.CharField(max_length=200)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class distintivo(models.Model):
    nome = models.CharField(max_length=200)
    img = models.CharField(max_length=200)

class usuario_to_distintivo(models.Model):
    fk_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    fk_distintivo = models.ForeignKey(distintivo, on_delete=models.CASCADE)

class tag(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class thread(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    data_edicao = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(tag)

class tag_to_thread(models.Model):
    fk_tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    fk_thread = models.ForeignKey(thread, on_delete=models.CASCADE)

class artigo(models.Model):
    texto = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    data_edicao = models.DateTimeField(auto_now=True)
    fk_thread = models.ForeignKey(thread, on_delete=models.CASCADE)