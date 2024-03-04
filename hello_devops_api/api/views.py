from rest_framework.response import Response
from rest_framework.decorators import api_view

from socket import gethostname, gethostbyname_ex # test

@api_view(['GET'])
def getHelloDevOps(request):
    print("gethostname: " + gethostname()) # test
    print("IP range: " + list(set(gethostbyname_ex(gethostname())[2]))) # test
    return Response("Hello DevOps")

@api_view(['GET'])
def getHealth(request):
    #TODO
    return Response("health") 