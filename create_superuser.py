from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

def create_superuser():
    User = get_user_model()

    # Defina as credenciais básicas do superusuário
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin123'

    # Verifique se o superusuário já existe
    if not User.objects.filter(username=username).exists():
        try:
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f'Superusuário criado com sucesso: {username} / {email}')
        except IntegrityError:
            print('Erro: não foi possível criar o superusuário, ele já existe.')
    else:
        print('Superusuário já existe.')
