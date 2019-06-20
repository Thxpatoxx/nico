from django.shortcuts import render, get_object_or_404
from .models import Diagnostico
from .forms import DiagnosticoForm
from django.shortcuts import redirect

def post_list(request):
    Diagnosticos = Diagnostico.objects.order_by('author')
    return render(request, 'blog/post_list.html', {'Diagnosticos': Diagnosticos})

def post_detail(request, pk):
    Diagnosticos = get_object_or_404(Diagnostico, pk=pk)
    return render(request, 'blog/post_detail.html', {'Diagnosticos': Diagnosticos})

def post_new(request):
    if request.method == "POST":
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            Diagnostico = form.save(commit=False)
            Diagnostico.author = request.user
            Diagnostico.save()
            return redirect('post_detail', pk=Diagnostico.pk)
    else:
        form = DiagnosticoForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    Diagnosticos = get_object_or_404(Diagnostico, pk=pk)
    if request.method == "POST":
        form = DiagnosticoForm(request.POST, instance=Diagnosticos)
        if form.is_valid():
            Diagnosticos = form.save(commit=False)
            Diagnosticos.author = request.user
            Diagnosticos.save()
            return redirect('post_detail', pk=Diagnosticos.pk)
    else:
        form = DiagnosticoForm(instance=Diagnosticos)
    return render(request, 'blog/post_edit.html', {'form': form})