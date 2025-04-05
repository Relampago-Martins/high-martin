# FROM nginx:stable
FROM arm64v8/nginx:stable

# Remove default sites
RUN rm -rf /usr/share/nginx/html/*

# Instalar dependências necessárias
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    libaugeas0 \
    && rm -rf /var/lib/apt/lists/*

# Criar ambiente virtual para o Certbot
RUN python3 -m venv /opt/certbot/ && \
    /opt/certbot/bin/pip install --upgrade pip && \
    /opt/certbot/bin/pip install certbot certbot-nginx

# Criar um symlink para facilitar a execução do Certbot
RUN ln -s /opt/certbot/bin/certbot /usr/bin/certbot

# Criar diretório para os certificados SSL
RUN mkdir -p /etc/letsencrypt/live && \
    mkdir -p /var/www/certbot

# setar arquivo de configuração do Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Expor portas necessárias
EXPOSE 80 443

# Comando padrão para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]
