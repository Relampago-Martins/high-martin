# high-martin

Este é um repositório para os contêineres que rodaram no balenaOS do meu raspberry pi 4

## Como rodar os contêineres

```shell
# para rodar os contêineres
docker compose up -d --build

# para parar os contêineres
docker compose down

# para entrar no shell do contêiner do compose
docker compose exec <nome-do-serviço> sh

```

## Como fazer o deploy no balenaOS

```shell

# para listar os dispositivos conectados
balena fleets

# para fazer o deploy no balenaOS
balena push <nome-do-app> -c
```
