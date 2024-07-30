from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Homework
from .forms import HomeworkForm

def home(request):
    return render(request, 'index.html')

def sign_in(request):
    return render(request, 'view/sign-in.html')
def sign_up(request):
    return render(request, 'view/sign-up.html')

def index_logined(request):
    return render(request, 'view/index-logined.html')

def view_homework(request):
    #finishedがFalseのHomeworkのみをデータベースから持ってくる
    homework_list = Homework.objects.filter(finished=False)
    context = { 'homework_list':homework_list }
    return render(request, 'view/view-homework.html', context)

def add_homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_homework')
    else:
        form = HomeworkForm()
    return render(request, 'view/add-homework.html', {'form': form})

def homework_details(request, id):
    homework = get_object_or_404(Homework, id=id)
    context = {'homework':homework}
    return render(request, 'view/homework-details.html', context)

def finished_homework(request):
    #finishedがTrueのHomeworkのみをデータベースから持ってくる
    finished_list = Homework.objects.filter(finished=True)
    context = { 'finished_list':finished_list }
    return render(request, 'view/finished-homework.html', context)