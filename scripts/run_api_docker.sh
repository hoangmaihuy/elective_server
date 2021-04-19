echo "Stop tuike_api"
docker container stop tuike_api
echo "Remove tuike_api"
docker container rm tuike_api
echo "Run tuike_api"
docker run -p 8000:8000 --env "PORT=8000" --env-file env.list --name tuike_api -d tuike_api
