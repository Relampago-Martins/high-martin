# FROM nginx:stable
FROM arm64v8/nginx:stable

# Remove default sites
RUN rm -rf /usr/share/nginx/html/*

# Set our working directory
COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]