# CUIDADO
Cambiar el formato de salto de linea de "entrypoint.sh" de CRLF (Windows) a LF (Unix). Se puede hacer en VS.
![image](https://github.com/user-attachments/assets/c744943e-2bd6-4bbe-8e5e-9c9ed369a584)
Esto se hace porque sino Docker tira error al hacer compose up --build.

# PASOS
1) Clonar el repo en alguna carpeta con git clone https://github.com/AgustinMohr/gestion-campo.git
2) Ejecutar docker desktop en la pc
3) Abrir una terminal en la direccion /gestion-campo/ruralia
4) Ejecutar 'docker compose down' -v y luego 'docker compose up --build'
5) Ir a localhost:8000/ en el navegador
6) DISFRUTAR
