docker stop node
docker rm node
docker run -d --name node -v $PWD:/data node:alpine sh -c 'while true;do sleep 3600;done'
docker exec -it node sh -c 'apk add git'
docker exec -it node sh -c 'cd /data;npm install'
docker inspect --format='{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq)|grep node
docker exec -it node sh -c 'cd /data;npm run dev'