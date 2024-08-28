from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from ata.forms import AtasForm
from ata.models import ArquivoPDF, Atas
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

@login_required
def ver_arquivos_ata(request, ata_id):
    ata = get_object_or_404(Atas, id=ata_id)
    pdfs = ata.pdfs.all()
    
    return render(request, 'ata/ver_arquivos_ata.html', {'ata': ata, 'pdfs': pdfs})

@login_required
def upload_arquivo_pdf(request, ata_id):
    
    ata = get_object_or_404(Atas, id=ata_id)
    
    if request.method == "POST":
        pdf_file = request.FILES.get('pdf')
        
        if pdf_file:
            ArquivoPDF.objects.create(ata=ata, pdf=pdf_file)
            messages.success(request, 'Arquivo PDF adicionado com sucesso.')
        else:
            messages.error(request, 'Nenhum arquivo selecionado.')
        
        return redirect('ver_arquivos_ata', ata_id=ata_id)
    
    return redirect('ver_arquivos_ata', ata_id=ata_id)