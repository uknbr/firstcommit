#!/usr/bin/env sh
docker-compose -p firstcommit up -d --scale app=3
docker tag firstcommit:v2 firstcommit:latest

sleep 3
docker-compose -p firstcommit ps

for attempt in $(seq 1 10) ; do
	echo -e "\n\n === Attempt ${attempt} ==="
	sleep .5
	curl -f -m 5 -H "Host: docker" http://localhost:8080/infra
done

echo -e "\n"