from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import CompanyData  # Import your models here

import os
import threading
import pandas as pd
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect

from django.db import connection

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from django.shortcuts import redirect


def truncate_table():
    with connection.cursor() as cursor:
        cursor.execute('TRUNCATE TABLE app_companydata RESTART IDENTITY CASCADE;')

def process_file(file_path):
    # Background file processing (e.g., read CSV and update the database)
    file_full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    truncate_table()
    df = pd.read_csv(file_full_path)

    for index, row in df.iterrows():
        # Handle NaN values for fields expected to be integers
        year_founded = row.get('year founded')
        current_employee_estimate = row.get('current employee estimate')
        total_employee_estimate = row.get('total employee estimate')

        # Convert NaN to None or appropriate default values
        year_founded = int(year_founded) if pd.notna(year_founded) else None
        current_employee_estimate = int(current_employee_estimate) if pd.notna(current_employee_estimate) else None
        total_employee_estimate = int(total_employee_estimate) if pd.notna(total_employee_estimate) else None

        CompanyData.objects.create(
            name=row.get('name'),
            domain=row.get('domain'),
            year_founded=year_founded,
            industry=row.get('industry'),
            size_range=row.get('size range'),
            locality=row.get('locality'),
            country=row.get('country'),
            linkedin_url=row.get('linkedin url'),
            current_employee_estimate=current_employee_estimate,
            total_employee_estimate=total_employee_estimate
        )
    os.remove(file_full_path)



