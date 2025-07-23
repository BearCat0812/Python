from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("안녕하세요 파이보입니다.")
    return render(request, 'test.html')

def dashboard(request):
    # 여기에 대시보드에 표시할 데이터를 준비합니다
    context = {
        'total_visitors': 0,
        'today_visitors': 0,
        'total_posts': 0,
    }
    return render(request, 'dashboard.html', context)