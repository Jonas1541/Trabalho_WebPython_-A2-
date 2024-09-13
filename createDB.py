import pymysql
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# Função para criar banco de dados se não existir
def create_database_if_not_exists():
    try:
        # Pegando as configurações do banco de dados do settings
        DB_NAME = settings.DATABASES['default']['NAME']
        DB_USER = settings.DATABASES['default']['USER']
        DB_PASSWORD = settings.DATABASES['default']['PASSWORD']
        DB_HOST = settings.DATABASES['default']['HOST']
        DB_PORT = settings.DATABASES['default']['PORT']

        # Conectando ao MySQL
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=int(DB_PORT)
        )

        # Executando o comando para criar o banco de dados se não existir
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        conn.close()
        print(f"Banco de dados '{DB_NAME}' criado ou já existente.")
    except pymysql.MySQLError as e:
        raise ImproperlyConfigured(f"Erro ao tentar conectar ao MySQL: {e}")
