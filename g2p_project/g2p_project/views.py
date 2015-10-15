from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/downloadData')
