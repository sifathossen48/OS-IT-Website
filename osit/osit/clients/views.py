from django.shortcuts import render, get_object_or_404, redirect
from .models import Clients
from .forms import NewClientForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

"""clients view"""

def clients(request):
    clients = Clients.objects.all()
    return render(request, 'clients.html', {'clients': clients})



"""new_client view"""

def new_client(request):
    if request.method == 'POST':
        form = NewClientForm(request.POST, request.FILES)
        if form.is_valid():
            clients = form.save(commit=False)
            clients.save()
            return redirect('clients')
    else:
        form = NewClientForm()

    return render(request, 'new_client.html', {'form': form})


"""delete_client view"""

def delete_client(request):
    if request.method == 'POST':
        selected_clients = request.POST.getlist('selected_clients[]')
        Clients.objects.filter(pk__in=selected_clients).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Method not allowed'}, status=405)