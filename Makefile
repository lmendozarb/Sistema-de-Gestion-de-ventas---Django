help: ## Muestra esta ayuda
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

build: ## Crea la imagen del proyecto
	docker-compose -f docker-compose.yml build

up-daemon: ## Inicia contenedores en background
	docker-compose -f docker-compose.yml up -d

up: ## Inicia contenedores en primer plano
	docker-compose -f docker-compose.yml up

start: ## Inicia ejecución contenedores ya existentes
	docker-compose -f docker-compose.yml start

stop: ## Detiene ejecución de contenedores
	docker-compose -f docker-compose.yml stop

down: ## Elimina los contenedores
	docker-compose -f docker-compose.yml down -v

restart: ## Reinicia ejecución de contenedores
	docker-compose -f docker-compose.yml stop && docker-compose -f docker-compose.yml start

migrations: ## Crea migraciones en el proyecto
	docker-compose -f docker-compose.yml exec web /bin/sh -c "python manage.py makemigrations"

migrate: ## Aplica migraciones en el proyecto
	docker-compose -f docker-compose.yml exec web /bin/sh -c "python manage.py migrate"

superuser: ## Crea un super usuario
	docker-compose -f docker-compose.yml exec web /bin/sh -c "python manage.py createsuperuser"

startapp: ## Crea un app de django
	docker-compose -f docker-compose.yml exec web /bin/sh -c "cd apps/;python ../manage.py startapp $(app_name)"

test: ## Ejecuta pruebas unitarias de un app
	docker-compose -f docker-compose.yml exec web /bin/sh -c "python manage.py test $(app_name)"

collectstatic: ## Recolecta archivos estáticos
	docker-compose -f docker-compose.yml exec web /bin/sh -c "python manage.py collectstatic --noinput"

loaddata: ## Carga los fixtures
	docker-compose -f docker-compose.yml exec web /bin/sh -c "python manage.py populate"

clearcache: ## Limpiar caché
	docker-compose -f docker-compose.yml exec web /bin/sh -c "python manage.py clear_cache"

showmigrations: ## Muestra las migraciones de un app
	docker-compose -f docker-compose.yml exec web /bin/sh -c "python manage.py showmigrations $(app_name)"

web-shell: ## Ejecutar shell de web
	docker-compose -f docker-compose.yml exec web /bin/sh -c "python manage.py shell_plus"

shell-web: ## Conectarse al contenedor del proyecto
	docker-compose -f docker-compose.yml exec web /bin/sh

shell-db: ## Conectarse al contenedor de la base de datos
	docker-compose -f docker-compose.yml exec db /bin/sh

log-db: ## Mostrar logs del contenedor de la base de datos
	docker-compose logs db

initial:
	docker-compose -f docker-compose.yml exec web sh -c "python manage.py initialdb"
