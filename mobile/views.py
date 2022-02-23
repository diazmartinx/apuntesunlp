from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import requests
from io import StringIO

def index(request):
    context = {"titulo":"Apuntes UNLP"}
    return render(request, 'base.html', context)

def materia(request,cod):
    """Hace un query de data.csv segun el CODIGO de la materia"""
    df = pd.read_csv('data.csv') 
    dfquery = df.loc[(df['codigo']==cod)]
    dfquery.reset_index(drop=True, inplace=True)
    print(dfquery)

    if not dfquery.empty:
        titulo = dfquery["nombre_materia"][0]
    else:
        titulo = 'Apuntes UNLP'

    context = {"titulo":titulo, "datos":dfquery}
    return render(request, 'materia.html', context)

def actualizar(request):
    """Basicamente esto cachea la informacion en data.csv para evitar excesivos llamados a la api de google
    y asi evitar que se bloquee"""
    url = 'https://docs.google.com/spreadsheets/d/1chkvChMO_c_oeWhb9SipwtBIomF-Gdt3ymHzQy6yRp8/gviz/tq?tqx=out:csv&gid=0'
    r = requests.get(url).text
    df = pd.read_csv(StringIO(r))
    df.to_csv('data.csv', index=False)
    print(df)
    return render(request,'actualizar.html')
