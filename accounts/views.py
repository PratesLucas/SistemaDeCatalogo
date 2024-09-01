from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from accounts.decorators import has_group
from accounts.forms import UsuarioForm
from accounts.models import Usuario


@has_group("SECRETARIO")
def createuser(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            tipo_user = form.cleaned_data['tipo_user']
            group, _ = Group.objects.get_or_create(name=tipo_user)
            user.groups.add(group)
            
            return redirect('list_users')
        else:
            return render(request, "form.html", {"form" : form, 'form_title': 'Cadastrar novo usuário'})
    else:
        form = UsuarioForm()
        return render(request, "form.html", {"form" : form, 'form_title': 'Cadastrar novo usuário'})



@has_group("SECRETARIO")
def listusers(request):
    users = Usuario.objects.all()
    
    return render(request, "registration/listusers.html", {"users" : users})


@has_group("SECRETARIO")
def deleteuser(request, id):
    Usuario.objects.filter(id=id).first().delete()
    
    redirect("list_users")


@has_group("SECRETARIO")
def edituser(request, id):
    user = Usuario.objects.filter(id=id).first()
    
    if not user:
        raise ObjectDoesNotExist
        
    if request.method == 'POST':
        form =  UsuarioForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            
            tipo_user = form.cleaned_data['tipo_user']
            group = Group.objects.get_or_create(name=tipo_user)
            user.groups.add(group)
            
            return HttpResponseRedirect('/pessoa/')
    else:
        form = UsuarioForm()
        return render(request, "form.html", {"form" : form, 'form_title': 'Cadastrar novo usuário'})

