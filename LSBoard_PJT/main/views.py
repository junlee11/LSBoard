from django.shortcuts import render
from django.http import HttpResponse
import getpass

# Create your views here.
def index(request):
    #return HttpResponse("Main Screen!!!")
    return render(request, 'main/index.html')

#로그인창 처리
def CategoryResponse(request):
    username = getpass.getuser()
    print(username)
    
    if username == 'ijung':
        return render(request, "category/category_main.html")
    else:
        return HttpResponse("권한이 없습니다.")

#프로그램 소개     
def ProgramIntroResponse(request):    
    return render(request, "category/ProgramIntroPage.html")

#프로그램 통계
def ProgramMathResponse(request):
    return render(request, "category/ProgramMathPage.html")