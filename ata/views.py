from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ata.forms import AtasForm
from ata.models import Atas
from django.contrib.auth.decorators import login_required

@login_required
def atas_view(request):
    atas = Atas.objects.all()
    for ata in atas:
        if not ata.pdf or not ata.pdf.name:
            ata.pdf_url = None
        else:
            ata.pdf_url = ata.pdf.url
    return render(request, 'ata/atas.html', {'atas': atas})

@login_required
def cadastro_ata_view(request):

    if request.method == "POST":
        form = AtasForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/ata/atas/')
    else:
        form = AtasForm()
    
    template = loader.get_template('ata/cadastro_ata.html')
    context = {'form': form}

    return HttpResponse(template.render(context, request))

@login_required
def edit_ata_view(request, ata_id):

    ata = Atas.objects.get(pk=ata_id)

    if request.method == "POST":
        form = AtasForm(request.POST, instance=ata)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/ata/atas/')
    else:
        form = AtasForm(instance=ata)

    return render(request, 'ata/cadastro_ata.html', {'form': form})


@login_required
def remove_ata_view(request, ata_id):

    ata = Atas.objects.get(pk = ata_id)
    ata.delete()

    return HttpResponseRedirect('/ata/atas/')
