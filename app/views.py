
from django.contrib.auth.decorators import login_required
from .models import CompanyData  
import threading
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from app.forms import UploadFileForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from allauth.account.forms import SignupForm
from django.views.decorators.csrf import csrf_exempt

from models.processFile import process_file
from models.query import prepareData, userData
import re

@csrf_exempt
def custom_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save(request)  
            context = {'status': 'success', 'message': 'User created successfully'}
            redirect('custom_login')
        else:
            return render(request, 'signup.html', {'status': 'error', 'message': form.errors})
    return render(request, 'signup.html')


@csrf_exempt
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            # return JsonResponse({'status': 'success', 'message': 'Logged in successfully'})
            context = {'status': 'success', 'message': 'Logged in successfully'}
            redirect('upload_data')
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=400)
    return render(request, 'login.html')


@csrf_exempt
@login_required
def custom_logout(request):
    if request.method == 'POST':
        logout(request)  # Log the user out
        return JsonResponse({'status': 'success', 'message': 'Logged out successfully'})
    return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def upload_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_path = default_storage.save(f'uploads/{uploaded_file.name}', uploaded_file)
            file_instance = CompanyData()
            file_instance.save()
            threading.Thread(target=process_file, args=(file_path,)).start()
            return render(request, 'upload_data.html', {'status': 'success', 'message': 'File uploaded successfully! Background data inserting into DB'})
        else:
            return render(request, 'upload_data.html', {'status': 'error', 'message': 'Invalid form submission!'})
    return render(request, 'upload_data.html')

@csrf_exempt
@login_required
def get_users(request):
    if request.method == 'GET':
        context = userData()
        return render(request, 'user_data.html', context)

@csrf_exempt
@login_required
def add_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save(request)  
            context = userData()
            context = {**context, **{'status': 'success', 'message': 'User added successfully'}}
            return render(request, 'user_data.html', context)
        else:
            return render(request, 'add_user.html', {'status': 'error', 'message': form.errors})
    return render(request, 'add_user.html')


@csrf_exempt
@login_required
def delete_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if not user_id:
            context = userData()
            context = {**context, **{'status': 'error', 'message': 'User ID is required'}}
            return render(request, 'user_data.html', context)
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            context = userData()
            context = {**context, **{'status': 'success', 'message': f'User with ID {user_id} deleted successfully'}}
            return render(request, 'user_data.html', context)
        except User.DoesNotExist:
            context = userData()
            context = {**context, **{'status': 'error', 'message': 'User not found'}}
            return render(request, 'user_data.html', context)


@csrf_exempt
@login_required
def query_builder(request):
    df = prepareData()
    data = {
        "industry": list(df['industry'].unique()),
        "year_founded": list(df['year_founded'].unique()),
        "city": list(df['city'].unique()),
        "state": list(df['state'].unique()),
        "country": list(df['country'].unique()),
    }
    context = {
        'data': data
    }
    if request.method == 'GET':
        return render(request, 'query_builder.html', context)
    elif request.method == 'POST':
        keyword = request.POST.get('keyword')
        industry = [item.strip() for item in request.POST.get('industry', '').split(',') if item]
        year_founded = [item.strip() for item in request.POST.get('year_founded', '').split(',') if item]
        city = [item.strip() for item in request.POST.get('city', '').split(',') if item]
        state = [item.strip() for item in request.POST.get('state', '').split(',') if item]
        country = [item.strip() for item in request.POST.get('country', '').split(',') if item]
        df = prepareData()
        if keyword:
            pattern = re.compile(keyword, re.IGNORECASE)
            df = df[df.apply(lambda row: row.astype(str).str.contains(pattern).any(), axis=1)]
        if industry:
            df = df[df['industry'].isin(industry)]
        if year_founded:
            df = df[df['year_founded'].isin(year_founded)]
        if city:
            df = df[df['city'].isin(city)]
        if state:
            df = df[df['state'].isin(state)]
        if country:
            df = df[df['country'].isin(country)]
        context = {**context, **{'status': 'success', 'message': f'{len(df)} records found for the query'}}
        return render(request, 'query_builder.html', context)
    else:
        return render(request, 'query_builder.html', context)
