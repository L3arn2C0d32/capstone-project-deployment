from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'BasicApp/index.html')

def form_name_view(request):
    return render(request,'BasicApp/form_page.html')

def gad_assessment_view(request):
    return render(request, 'BasicApp/gadassessment.html')
