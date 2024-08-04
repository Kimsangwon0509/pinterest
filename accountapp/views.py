from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import HelloWorld


# Create your views here.



def hello_world (request):
    if request.method =="POST" :
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/helloworld.html', context={'hello_world_list' : hello_world_list})

    def list_creator (tag):
        def text_wrapper(msg) :
            print('{0} {1}'.format(tag, msg))
        return text_wrapper

    data_list_minus = list_creator('-')
    data_list_minus('얀녕')

