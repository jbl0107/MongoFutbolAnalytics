from django.shortcuts import render




def index(request):
    return render(request, 'index.html')

def teams(request):
    return render(request, 'teams.html')

def players(request):
    return render(request, 'players.html')

def titles(request):
    return render(request, 'titles.html')

def goals(request):
    return render(request, 'goals.html')