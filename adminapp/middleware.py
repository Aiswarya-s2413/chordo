from django.shortcuts import redirect
from django.urls import reverse

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        
        if request.path.startswith('/admin/'):
          
            if request.user.is_superuser:
                return self.get_response(request)
            
          
            return redirect(reverse('adminLogin'))
        
        return self.get_response(request)
