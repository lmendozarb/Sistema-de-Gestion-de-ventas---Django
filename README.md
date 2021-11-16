# VILSOFT

## Comenzando 🚀
_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋

-   Docker 19.03^
-   Docker Compose 1.25^
***

## Instalación 🔧

1. Clonar el repositorio
```
git clone git@github.com:lmendozarb/Sistema-de-Gestion-de-ventas---Django.git
```
ó
```
git clone https://github.com/lmendozarb/Sistema-de-Gestion-de-ventas---Django.git
```

2. Crear copia de variables de entorno
 ```
cp -r .env.example .env
```
3. Build
```
docker-compose build
```
4. Levantar el contenedor
```docker-compose up``` ó ```docker-compose up -d``` para ejecutar el contenedor en segundo plano
5. Verificar la instalacion
```
http://localhost:8000/
```
6. Ejecutar migraciones y carga de datos iniciales
```
make migrate
```
7. Crear un super usuario
```
make superuser
```
8. Entrar al sistema , recordar que se tiene que crear primero los datos generales, como tipo de documentos (DNI) y monedas (SOLES) , luego generar un cliente, productos y luego generar las compras.

> En caso de no poder ver el sitio detener el contenedor y levantarlo nuevamente
***
