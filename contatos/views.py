from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContatoForm
from .models import Contato


def lista_contatos(request):
    q = request.GET.get("q", "").strip()
    contatos = Contato.objects.all()
    if q:
        contatos = contatos.filter(
            Q(nome__icontains=q) | Q(telefone__icontains=q) | Q(email__icontains=q)
        )
    return render(request, "contatos/lista.html", {"contatos": contatos, "q": q})


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


def editar_contato(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            messages.success(request, "Contato atualizado com sucesso.")
            return redirect("lista_contatos")
    else:
        form = ContatoForm(instance=contato)

    return render(
        request, "contatos/editar.html", {"form": form, "contato": contato}
    )


def excluir_contato(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    if request.method == "POST":
        contato.delete()
        messages.success(request, "Contato excluído com sucesso.")
        return redirect("lista_contatos")

    return render(request, "contatos/excluir.html", {"contato": contato})
