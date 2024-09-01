from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from ata.forms import ArquivoPDFForm, AtasForm
from ata.models import ArquivoPDF, Atas
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def atas_view(request):
    atas = Atas.objects.all()
    
    search = request.GET.get("search", None)
    if search is not None:
        if search:
            atas = atas.filter(
                Q(ano__icontains=search) |
                Q(serie__icontains=search) |
                Q(turma__icontains=search) |
                Q(pdf__icontains=search)
            )
    
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
    ata = get_object_or_404(Atas, id=ata_id)

    if request.method == "POST":
        form = AtasForm(request.POST, instance=ata)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ata/atas/')
    else:
        form = AtasForm(instance=ata)
    
    template = loader.get_template('ata/editar_ata.html')
    context = {'form': form}

    return HttpResponse(template.render(context, request))



@login_required
def remove_ata_view(request, ata_id):

    ata = Atas.objects.get(pk = ata_id)
    ata.delete()

    return HttpResponseRedirect('/ata/atas/')

@login_required
def ver_arquivos_ata(request, ata_id):
    ata = Atas.objects.get(pk=ata_id)
    pdfs = ArquivoPDF.objects.filter(ata=ata)
    return render(request, 'ata/ver_arquivos_ata.html', {'pdfs': pdfs, 'ata': ata})


@login_required
def upload_arquivo_pdf(request, ata_id):
    ata = Atas.objects.get(pk=ata_id)
    if request.method == 'POST':
        form = ArquivoPDFForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo_pdf = form.save(commit=False)
            arquivo_pdf.ata = ata
            arquivo_pdf.save()
            return redirect('ver_arquivos_ata', ata_id=ata.id)
    else:
        form = ArquivoPDFForm()
    return render(request, 'ata/ver_arquivos_ata.html', {'form': form, 'ata': ata})

@login_required
def editar_arquivo_pdf(request, arquivo_pdf_id):
    arquivo_pdf = get_object_or_404(ArquivoPDF, pk=arquivo_pdf_id)
    if request.method == 'POST':
        form = ArquivoPDFForm(request.POST, request.FILES, instance=arquivo_pdf)
        if form.is_valid():
            form.save()
            return redirect('ver_arquivos_ata', ata_id=arquivo_pdf.ata.id)
    else:
        form = ArquivoPDFForm(instance=arquivo_pdf)
    return render(request, 'ata/arquivo/editar_arquivo_pdf.html', {'form': form, 'arquivo_pdf': arquivo_pdf})

@login_required
def excluir_arquivo_pdf(request, arquivo_pdf_id):
    arquivo_pdf = get_object_or_404(ArquivoPDF, pk=arquivo_pdf_id)
    ata_id = arquivo_pdf.ata.id
    if request.method == 'POST':
        arquivo_pdf.delete()
        return redirect('ver_arquivos_ata', ata_id=ata_id)
    return render(request, 'confirmar_exclusao_arquivo_pdf.html', {'arquivo_pdf': arquivo_pdf})
