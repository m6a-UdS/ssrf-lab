all: build run

build:
	docker build -t ssrf-basics .

run:
	docker inspect ssrf-basics >/dev/null 2>&1 && docker rm -f ssrf-basics || true
	docker run --name ssrf-basics -p 8080:80 -d -t ssrf-basics