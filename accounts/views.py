from django.http import HttpResponseRedirect
from django.shortcuts import render
from accounts.forms import UsuarioForm
from django.contrib.auth.models import Group

def isProfessor(user):
    return user.groups.filter(name='Professores').exists()

def isAluno(user):
    return user.groups.filter(name='Alunos').exists()

def createuser(request):
    
    if request.method == 'POST':
        form =  UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            user.save()
            
            alunos_group = Group.objects.get(name='Alunos')
            user.groups.add(alunos_group)
            
            user.save()
            
            return HttpResponseRedirect('/pessoa/')
            
    else:
        form = UsuarioForm()
        return render(request, "accounts/form.html", {"form" : form})
