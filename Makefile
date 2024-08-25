up:
	docker compose -f build/dev/docker-compose.yaml up

down:
	docker compose -f build/dev/docker-compose.yaml down

rebuild:
	docker compose -f build/dev/docker-compose.yaml up --build

logs:
	docker compose -f build/dev/docker-compose.yaml logs -f
