# For project
build:
	docker compose build
	
dev:
	docker compose up

start:
	docker compose up -d

stop:
	docker compose down

restart:
	docker compose down
	docker compose up -d

logs:
	docker compose logs -f


clean:
	docker compose down -v

# For services
start-service:
	docker compose up -d catalog