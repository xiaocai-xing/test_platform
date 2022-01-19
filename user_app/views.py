from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from user_app.models import Project,Module



# Create your views here.
# 主要代码逻辑，数据处理，业务操作

def index(request):
    return render(request,'index.html')

def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        if username == ""or password == "":

            return render(request, 'index.html',
                          {"error":"用户名或者密码为空"}
                          )
        else:
            user = auth.authenticate(
                username = username,password =password
            )
            if user is  not None:
                auth.login(request,user)
                request.session['user1'] = username
                return HttpResponseRedirect("/project_manage/")
            else:

                return render(request, 'index.html',
                              {"error": "用户名或者密码错误"}
                              )


@login_required
def project_manage(request):
    username = request.session.get('user1','')

    project_all = Project.objects.all()
    print(project_all)

    return render(request, 'project_manage.html',
                  {"user":username,
                   "projects":project_all,
                    "type":"list"}
                  )

@login_required
def add_project(request):
    return render(request,"project_manage.html",
                  {
                      "type":"add"
                  }
                  )



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/logout/")