from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import ContatoForm
from .models import Contato


def lista_contatos(request):
    contatos = Contato.objects.all()
    return render(request, "contatos/lista.html", {"contatos": contatos})


def novo_contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contato cadastrado com sucesso.")
            return redirect("lista_contatos")
    else:
        form = ContatoForm()

    return render(request, "contatos/novo.html", {"form": form})
