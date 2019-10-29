from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
def rmt_redirect_view(request, *args, **kwargs):
    return HttpResponse("Hello world")

class RmtRedirectedView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello again FB")