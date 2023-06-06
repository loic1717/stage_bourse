from django.shortcuts import render, redirect
from .forms import UtilisateurCreationForm
from .models import UtilisateurModel
#login,logout,authentificate sont fournie par Django
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

def ajout_utilisateur(request):
    form = UtilisateurCreationForm()
    if request.method == 'POST':
        form = UtilisateurCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user/login')  # Remplacez "nom_de_l_url_de_redirection" par le nom de l'URL de redirection après l'ajout réussi de l'utilisateur
    return render(request, 'user/ajout_utilisateur.html', {'form': form})



# def login_view(request):
#     if request.method == 'POST':
#         form = UtilisateurCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('user/login.html')  # Redirige vers la page souhaitée après la connexion réussie
#     else:
#         form = UtilisateurCreationForm()

#     return render(request, 'user/connexion.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/')  # Redirige vers la page souhaitée après la connexion réussie
        else:
            error_message = "Invalid username or password."
    else:
        error_message = None

    return render(request, 'user/connexion.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('/')  # Redirige vers la page de connexion après la déconnexion réussie
