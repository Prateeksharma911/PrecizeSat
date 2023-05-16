from django.shortcuts import render, redirect
from .models import Candidate

def home(request):
    return render(request, 'sat_results/home.html')

def insert_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        country = request.POST['country']
        pincode = request.POST['pincode']
        sat_score = float(request.POST['sat_score'])
        
        candidate = Candidate(name=name, city=city, country=country, pincode=pincode, sat_score=sat_score)
        candidate.save()
        
        return redirect('view_all_data')
    
    return render(request, 'sat_results/insert_data.html')

def view_all_data(request):
    candidates = Candidate.objects.all()
    return render(request, 'sat_results/view_all_data.html', {'candidates': candidates})

def get_rank(request):
    if request.method == 'POST':
        name = request.POST['name']
        
        try:
            candidate = Candidate.objects.get(name=name)
            candidates = Candidate.objects.order_by('-sat_score')
            rank = list(candidates).index(candidate) + 1
        except Candidate.DoesNotExist:
            rank = None
        
        return render(request, 'sat_results/get_rank.html', {'name': name, 'rank': rank})
    
    return render(request, 'sat_results/get_rank.html')

def update_score(request):
    if request.method == 'POST':
        name = request.POST['name']
        new_score = float(request.POST['new_score'])
        
        try:
            candidate = Candidate.objects.get(name=name)
            candidate.sat_score = new_score
            candidate.save()
        except Candidate.DoesNotExist:
            pass
        
        return redirect('view_all_data')
    
    return render(request, 'sat_results/update_score.html')

def delete_record(request):
    if request.method == 'POST':
        name = request.POST['name']
        
        try:
            candidate = Candidate.objects.get(name=name)
            candidate.delete()
        except Candidate.DoesNotExist:
            pass
        
        return redirect('view_all_data')
    
    return render(request, 'sat_results/delete_record.html')
