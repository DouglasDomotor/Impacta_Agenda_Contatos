from django.test import TestCase
from django.urls import reverse

from .models import Contato


class ContatoCrudTests(TestCase):
    def setUp(self):
        self.ana = Contato.objects.create(
            nome="Ana Lima",
            telefone="11999990000",
            email="ana@exemplo.com",
        )
        Contato.objects.create(
            nome="Bruno Costa",
            telefone="11888880000",
            email="bruno@exemplo.com",
        )

    def test_busca_por_nome(self):
        response = self.client.get(reverse("lista_contatos"), {"q": "ana"})
        self.assertContains(response, "Ana Lima")
        self.assertNotContains(response, "Bruno Costa")

    def test_busca_sem_resultado(self):
        response = self.client.get(reverse("lista_contatos"), {"q": "zzzz"})
        self.assertContains(response, "Nenhum contato encontrado")

    def test_editar_contato(self):
        response = self.client.post(
            reverse("editar_contato", args=[self.ana.pk]),
            {
                "nome": "Ana Souza",
                "telefone": "11999990000",
                "email": "ana@exemplo.com",
            },
        )
        self.assertRedirects(response, reverse("lista_contatos"))
        self.ana.refresh_from_db()
        self.assertEqual(self.ana.nome, "Ana Souza")

    def test_excluir_contato(self):
        response = self.client.post(reverse("excluir_contato", args=[self.ana.pk]))
        self.assertRedirects(response, reverse("lista_contatos"))
        self.assertFalse(Contato.objects.filter(pk=self.ana.pk).exists())

    def test_excluir_exige_confirmacao(self):
        response = self.client.get(reverse("excluir_contato", args=[self.ana.pk]))
        self.assertContains(response, "Ana Lima")
        self.assertTrue(Contato.objects.filter(pk=self.ana.pk).exists())
