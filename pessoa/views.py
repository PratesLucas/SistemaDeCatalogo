from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from pessoa.forms import PessoaForm
from .models import ArquivoPDF, Pessoa

@login_required
def index(request):
    if request.GET:
        dic = {}

        for chave, valor in request.GET.lists():
            dic.update({chave + "__contains": valor[0]})

        pessoas = Pessoa.objects.all().filter(**dic)
    else:
        pessoas = Pessoa.objects.all()

    return render(request, 'pessoa/listagem.html', {'pessoas': pessoas})

@login_required
def details(request, pessoa_id):

    pessoa = Pessoa.objects.get(pk = pessoa_id)

    return render(request, "pessoa/detalhes.html", {'pessoa' : pessoa})

@login_required
def add(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST, request.FILES)
        if form.is_valid():
            pessoa = form.save()
            ArquivoPDF.objects.create(pessoa=pessoa, pdf=form.cleaned_data['pdf'])
            return redirect('/pessoa/', pessoa_id=pessoa.id)
    else:
        form = PessoaForm()
    
    return render(request, 'pessoa/add.html', {'form': form})

@login_required
def edit(request, pessoa_id):

    pessoa = Pessoa.objects.get(pk = pessoa_id)

    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/pessoa/')
    else:
        form = PessoaForm(instance=pessoa)

    return render(request, 'pessoa/edit.html', {'form' : form})

@login_required
def remove(request, pessoa_id):

    Pessoa.objects.get(pk = pessoa_id).delete()

    return HttpResponseRedirect('/pessoa/')