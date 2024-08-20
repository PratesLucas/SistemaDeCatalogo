from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ata.forms import AtasForm
from ata.models import Atas
from django.contrib.auth.decorators import login_required

@login_required
def atas_view(request):
    if request.GET:
        dic = {}
        for chave, valor in request.GET.lists():
            dic.update({chave + "__contains": valor[0]})
        atas = Atas.objects.all().filter(**dic)
    else:
        atas = Atas.objects.all()

    template = loader.get_template('ata/atas.html')
    context = {'atas': atas}

    return HttpResponse(template.render(context, request))

@login_required
def cadastro_ata_view(request):

    if request.method == "POST":
        form = AtasForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/ata/')
    else:
        form = AtasForm()
    
    template = loader.get_template('ata/cadastro_ata.html')
    context = {'form': form}

    return HttpResponse(template.render(context, request))
