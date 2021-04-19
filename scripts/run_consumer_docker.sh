echo "Stop tuike_consumer"
sudo docker container stop tuike_consumer
echo "Remove tuike_consumer"
sudo docker container rm tuike_consumer
echo "Buld tuike_consumer"
sudo docker build -t tuike_consumer . -f tuike_consumer/Dockerfile
echo "Run tuike_consumer"
sudo docker run --env-file env.list --name tuike_consumer -d tuike_consumer
