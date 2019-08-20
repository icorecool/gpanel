docker start node
docker inspect --format='{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq)|grep node
docker exec -it node sh -c 'cd /data;npm run dev'