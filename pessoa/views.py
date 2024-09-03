from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import has_group
from .forms import PessoaForm, EnderecoForm
from .models import ArquivoPDF, Pessoa, Endereco
from django.db.models import Q
from django.contrib.auth.models import User

@login_required
def index(request, tipo="ALUNO"):
    # Adiciona o grupo SECRETARIO ao primeiro usuário se ele ainda não estiver no grupo
    if User.objects.all().count() == 1:
        gp, _ = Group.objects.get_or_create(name="SECRETARIO")
        request.user.groups.add(gp)
    
    if tipo not in ["ALUNO", "PROFESSOR"]:
        tipo = "ALUNO"
    # Obtém todos os registros de Pessoa e ordena alfabeticamente pelo nome
    pessoas = Pessoa.objects.filter(tipo_pessoa=tipo).order_by('nome')
    
    search = request.GET.get("search", None)
    if search is not None:
        if search:
            pessoas = pessoas.filter(
                Q(nome__icontains=search) |
                Q(cpf__icontains=search) |
                Q(pdf__icontains=search)
            )

    return render(request, 'pessoa/listagem.html', {'pessoas': pessoas, 'search': search, 'tipo': Pessoa.TIPOS_PESSOAS_DICT[tipo]})


@has_group("SECRETARIO")
def add_endereco(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)

    if request.method == "POST":
        form = EnderecoForm(request.POST)
        if form.is_valid():
            endereco = form.save()
            pessoa.endereco = endereco
            pessoa.save()
            return redirect('details', pessoa.id)
    else:
        form = EnderecoForm()

    context = {
        'form': form,
        'pessoa': pessoa,
    }
    return render(request, 'form.html', context)
    
    
@has_group("SECRETARIO")
def edit_endereco(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)

    if request.method == "POST":
        form = EnderecoForm(request.POST, instance=pessoa.endereco)
        if form.is_valid():
            endereco = form.save()
            pessoa.endereco = endereco
            pessoa.save()
            return redirect('details', pessoa.id)
    else:
        form = EnderecoForm(instance=pessoa.endereco)

    context = {
        'form': form,
        'pessoa': pessoa,
    }
    return render(request, 'form.html', context)
    
    
@has_group("SECRETARIO")
def remove_endereco(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    
    if pessoa.endereco:
        pessoa.endereco.delete()
        pessoa.endereco = None
        pessoa.save()

    return redirect('details', pessoa.id)


@login_required
def details(request, pessoa_id):
    pessoa = Pessoa.objects.get(pk=pessoa_id)
    return render(request, "pessoa/detalhes.html", {'pessoa': pessoa})


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
    pessoa = Pessoa.objects.get(pk=pessoa_id)

    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pessoa/')
    else:
        form = PessoaForm(instance=pessoa)

    return render(request, 'pessoa/edit.html', {'form': form, "pessoa": pessoa})


@has_group("SECRETARIO")
def remove(request, pessoa_id):
    Pessoa.objects.get(pk=pessoa_id).delete()
    return HttpResponseRedirect('/pessoa/')
