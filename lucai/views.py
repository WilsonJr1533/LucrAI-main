from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .forms import TransacaoForm
from threading import Thread
import pandas as pd
from plotly.io import to_image
import plotly.graph_objs as go
from django.contrib.auth import logout




def home(request):
    return render(request, 'pages/home.html')




from django.http import JsonResponse
import google.generativeai as genai


def index(request):
    # ...


    # Verifica se há uma resposta da IA na variável de sessão
    resposta_ia = request.session.pop('resposta_ia', None)

    return render(request, 'pages/index.html', {'resposta_ia': resposta_ia})


def obter_resposta_ia(mensagem_usuario):
    
    genai.configure(api_key="API")
    
    

    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]

    model = genai.GenerativeModel(
        model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings
    )

    prompt_parts = [
        "vc é um IA",
        mensagem_usuario,
    ]

    response = model.generate_content(prompt_parts)
    return response.text

def obter_resposta_ia_view(request):
    if request.method == 'POST':
        mensagem_usuario = request.POST.get('mensagem_usuario', '')
        print(f'Mensagem do Usuário: {mensagem_usuario}')

        resposta_ia = obter_resposta_ia(mensagem_usuario)
        print(f'Resposta IA: {resposta_ia}')

        return JsonResponse({'resposta_ia': resposta_ia})
    else:
        return JsonResponse({'error': 'Método não permitido'})


def logout_view(request):
    logout(request)
    # Redireciona para a página de login ou para a home após o logout
    return redirect('home')