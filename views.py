from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Customer welcome to Tarzen Moterbike Sales")

    def time(request):
        now ="current date and time" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
return HttpResponse(now)
