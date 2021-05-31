echo "Stop tuike_api"
docker container stop tuike_api
echo "Remove tuike_api"
docker container rm tuike_api
echo "Pull tuike_api"
docker pull hoangmaihuy/tuike_api
echo "Run tuike_api on port 3002"
docker run -p 3002:8000 --env "PORT=8000" --env-file env.list --name tuike_api -d hoangmaihuy/tuike_api
