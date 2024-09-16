from app.models import CompanyData  
from django.contrib.auth.models import User
import pandas as pd

def prepareData():
    data = CompanyData.objects.all().values('country', 'locality', 'year_founded', 'industry')
    df = pd.DataFrame(data)
    df[['city', 'state', 'countryDrop']] = df['locality'].str.split(',', expand=True)
    df.drop(columns=['countryDrop'], inplace=True)
    df['year_founded'] = df['year_founded'].fillna(0).astype(int).astype(str).replace('0', 'none')
    df.fillna('None', inplace=True)
    df['city'] = df['city'].str.strip()
    df['state'] = df['state'].str.strip()
    df['country'] = df['country'].str.strip()
    df['industry'] = df['industry'].str.strip()
    return df

def userData():
    users = User.objects.all().values('id', 'username', 'email', 'is_active')
    user_list = list(users)  
    user_list = [{**dct, 'is_active': 'Active' if dct.get('is_active') else 'inactive'} for dct in user_list]
    context = {
        'users': user_list
    }
    return context