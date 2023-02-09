from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.


class Login(APIView):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            return render(request, "login.html")

