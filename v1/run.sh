#!/usr/bin/env sh
docker build -t firstcommit:v1 .
docker tag firstcommit:v1 firstcommit:latest
docker run --rm -dti --name firstcommit -p 1234:1234 firstcommit

sleep 3
docker ps

for attempt in $(seq 1 10) ; do
	echo -e "\n\n === Attempt ${attempt} ==="
	sleep .5
	curl -f -m 5 http://localhost:1234/info
done

echo -e "\n"
