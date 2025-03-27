import os
import django

# Configurar Django si es necesario
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Datos del superusuario (puedes cambiar estos valores o usar variables de entorno)
USERNAME = "admin"
EMAIL = "admin@example.com"
PASSWORD = "admin"

# Verificar si el superusuario ya existe
if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print(f"Superusuario '{USERNAME}' creado exitosamente.")
else:
    print(f"El superusuario '{USERNAME}' ya existe.")

User = get_user_model()
user = User.objects.create(username="admin2", email="admin1@example.com", is_superuser=True, is_staff=True, is_active=True)
user.set_password("pass2")  # Encripta la contraseña correctamente
print(f"Usuario 'admin2' creado exitosamente.")
user.save()