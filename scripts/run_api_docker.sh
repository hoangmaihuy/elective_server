echo "Stop tuike_api"
sudo docker container stop tuike_api
echo "Remove tuike_api"
sudo docker container rm tuike_api
echo "Build tuike_api"
sudo docker build -t tuike_api .
echo "Run tuike_api"
sudo docker run -p 8000:8000 --env "PORT=8000" --env-file env.list --name tuike_api -d tuike_api
