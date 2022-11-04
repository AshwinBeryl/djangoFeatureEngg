# Create your views here.
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os

def describe(request):
    if request.method=="POST":
        uploaded_file=request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        df=pd.read_csv("/config/workspace/media/{}".format(uploaded_file.name))
        print(df.head())
    return render(request, 'describe.html', {})
