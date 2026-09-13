from django.db import models


class Contato(models.Model):
    nome = models.CharField("Nome", max_length=120)
    telefone = models.CharField("Telefone", max_length=30)
    email = models.EmailField("E-mail")
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return self.nome
