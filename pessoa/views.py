from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from accounts.decorators import has_group
from pessoa.forms import PessoaForm
from .models import ArquivoPDF, Pessoa
from django.db.models import Q
from django.contrib.auth.models import User

@login_required
def index(request):
    if User.objects.all().count() == 1:
        gp, _ = Group.objects.get_or_create(name="SECRETARIO")
        request.user.groups.add(gp)
    
    pessoas = Pessoa.objects.all()
        
    search = request.GET.get("search", None)
    if search is not None:
        if search:
            pessoas = pessoas.filter(
                Q(nome__icontains=search) |
                Q(cpf__icontains=search) |
                Q(pdf__icontains=search)
            )

    return render(request, 'pessoa/listagem.html', {'pessoas': pessoas, 'search': search})

@login_required
def details(request, pessoa_id):

    pessoa = Pessoa.objects.get(pk = pessoa_id)

    return render(request, "pessoa/detalhes.html", {'pessoa' : pessoa})

@has_group("SECRETARIO")
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

@has_group("SECRETARIO")
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

@has_group("SECRETARIO")
def remove(request, pessoa_id):
    Pessoa.objects.get(pk = pessoa_id).delete()

    return HttpResponseRedirect('/pessoa/')