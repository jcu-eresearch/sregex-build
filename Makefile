all:
	docker-compose up

test:
	docker-compose run centos-8 bash

build:
	docker pull centos:8 && docker pull centos:7
	docker-compose build

rebuild:
	docker-compose up --build

clean:
	docker-compose down --volumes --remove-orphans
	rm -rf build/centos-*/*

.PHONY: all test build clean ci
