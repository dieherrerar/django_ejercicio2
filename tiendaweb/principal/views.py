from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    try: 
        if request.method == 'POST':
            usuario = 'diego@gmail.com'
            password = 'diego123'
            correo = request.POST.get('correo')
            contraseña = request.POST.get('contraseña')
            if correo == usuario and contraseña == password:
                mensaje = 'Bienvenido'
                return render(request,'index.html', {'mensaje': mensaje })
            else:
                mensaje = 'Usuario o contraseña incorrecto'
                return render(request,'index.html', {'mensaje': mensaje })

        elif request.method == 'GET':
            return render(request , 'index.html')
    except Exception as error: 
        print(error)