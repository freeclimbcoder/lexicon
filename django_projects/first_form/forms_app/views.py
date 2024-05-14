from django.shortcuts import render

# Create your views here.
from forms_app import forms

def index(request):
    return render(request, 'basic_app/index.html')

def other(request):
    return render(request, 'basic_app/other.html')

def base(request):
    return render(request, 'basic_app/base.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
    
def form_name_view(request):
    form = forms.FormsName()

    if request.method == 'POST':
        form = forms.FormsName(request.POST)

        if form.is_valid():
            print('Validation success!')
            print('Name = ' + form.cleaned_data['name'])
            print('Email = ' + form.cleaned_data['email'])
            print('Text = ' + form.cleaned_data['text'])
    return render(request, 'forms_app/form.html', {'form':form} )
