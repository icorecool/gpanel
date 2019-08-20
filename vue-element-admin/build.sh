# 构建测试环境
# docker exec -it node sh -c 'cd /data;npm run build:stage'

# 构建生产环境
docker exec -it node sh -c 'cd /data;npm run build:prod'