from django.http import HttpResponse

class MiddleareLifeCycle:
    def __init__(self,get_response):
        print("INIT METHOD")
        self.get_response = get_response

    def __call__(self, request):
        print('Before the view excited')
        response = self.get_response(request)
        print('After the view Excited')
        return response

class ExceptionHandleMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    
    def process_exception(self,request,exception):
        print(exception.__class__.__name__)
        print(exception)
        return HttpResponse("<b>we are faccing some technical issue.</b>")
      