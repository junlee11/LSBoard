from django.shortcuts import render
from django.http import HttpResponse
import getpass

# Create your views here.
def index(request):
    #return HttpResponse("Main Screen!!!")
    return render(request, 'main/index.html')

#로그인창 처리
def LoginResponse(request):
    username = getpass.getuser()
    print(username)
    
    if username == 'heeyoung':
        return render(request, "category/index.html")
    else:
        return HttpResponse("권한이 없습니다.")