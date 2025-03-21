# Usa la imagen oficial de Nginx
FROM nginx:latest

# Copia los archivos HTML, CSS y JS a la carpeta de Nginx
COPY . /usr/share/nginx/html

# Copia la configuración personalizada de Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Expone el puerto 80 para servir la web
EXPOSE 80
