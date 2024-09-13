from django.shortcuts import render, redirect, get_object_or_404
from .models import Text
from django import forms


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['title', 'description']

def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TextForm()

    texts = Text.objects.all()
    return render(request, 'index.html', {'form': form, 'texts': texts})

def edit(request, pk):
    text = get_object_or_404(Text, pk=pk)
    if request.method == 'POST':
        form = TextForm(request.POST, instance=text)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TextForm(instance=text)
    
    return render(request, 'edit.html', {'form': form})
