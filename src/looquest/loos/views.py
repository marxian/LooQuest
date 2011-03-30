from django.shortcuts import redirect

# Serve the js UI
def index(request):
    return redirect('/ui/looquest.html')
    