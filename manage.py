#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from createDB import create_database_if_not_exists
from create_superuser import create_superuser

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gerenciador_tarefas.settings')
    try:
        from django.core.management import execute_from_command_line

        # Executar o comando Django
        execute_from_command_line(sys.argv)

        # Executar o script de criação de banco de dados e criação de superusuário
        if 'makemigrations' in sys.argv:
            create_database_if_not_exists()
        if 'migrate' in sys.argv:
            create_superuser()
            
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


if __name__ == '__main__':
    main()
