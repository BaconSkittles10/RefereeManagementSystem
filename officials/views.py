from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'officials/home.html',
                 {
                     "official": request.user.official
                 })

def assignor_home(request):
    org_index = int(request.GET.get("org", 0))
    organization = request.user.assignor.organizations[org_index]
    
    return render(request, 'officials/assignor_home.html',
     {
         "assignor": request.user.assignor,
         "active_org": organization,
         "officials_sort": "last_first"
     })
    