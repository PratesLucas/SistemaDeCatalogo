from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from accounts.decorators import has_group
from ata.filters import AtasFilter
from ata.forms import ArquivoPDFForm, AtasForm
from ata.models import ArquivoPDF, Atas

@login_required
def atas_view(request):
    atas = Atas.objects.all().order_by('-ano', '-serie', '-turma')

    search = request.GET.get("search", None)
    if search:
        atas = atas.filter(
            Q(ano__icontains=search) |
            Q(serie__icontains=search) |
            Q(turma__icontains=search) |
            Q(pdf__icontains=search)
        )
    
    atas_filter = AtasFilter(request.GET, queryset=atas)
    atas = atas_filter.qs
    
    for ata in atas:
        ata.pdf_url = ata.pdf.url if ata.pdf and ata.pdf.name else None
    
    return render(request, 'ata/atas.html', {'atas': atas, 'filter': atas_filter, 'search': search})

@has_group("SECRETARIO")
def cadastro_ata_view(request):
    if request.method == "POST":
        form = AtasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ata/atas/')
    else:
        form = AtasForm()
    
    return render(request, 'ata/cadastro_ata.html', {'form': form})

@has_group("SECRETARIO")
def edit_ata_view(request, ata_id):
    ata = get_object_or_404(Atas, id=ata_id)
    if request.method == "POST":
        form = AtasForm(request.POST, instance=ata)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ata/atas/')
    else:
        form = AtasForm(instance=ata)
    
    return render(request, 'ata/editar_ata.html', {'form': form})

@has_group("SECRETARIO")
def remove_ata_view(request, ata_id):
    Atas.objects.get(pk=ata_id).delete()
    return HttpResponseRedirect('/ata/atas/')

@login_required
def ver_arquivos_ata(request, ata_id):
    ata = Atas.objects.get(pk=ata_id)
    pdfs = ArquivoPDF.objects.filter(ata=ata)
    return render(request, 'ata/ver_arquivos_ata.html', {'pdfs': pdfs, 'ata': ata})

@has_group("SECRETARIO")
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

@has_group("SECRETARIO")
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

@has_group("SECRETARIO")
def excluir_arquivo_pdf(request, arquivo_pdf_id):
    arquivo_pdf = get_object_or_404(ArquivoPDF, pk=arquivo_pdf_id)
    ata_id = arquivo_pdf.ata.id
    if request.method == 'POST':
        arquivo_pdf.delete()
        return redirect('ver_arquivos_ata', ata_id=ata_id)
    
    return render(request, 'confirmar_exclusao_arquivo_pdf.html', {'arquivo_pdf': arquivo_pdf})
