all: build run

build:
	docker build -t ssrf-adv2 .

run:
	docker inspect ssrf-adv2 >/dev/null 2>&1 && docker rm -f ssrf-adv2 || true
	docker run --name ssrf-adv2 -p 8080:80 -d -t ssrf-adv2
