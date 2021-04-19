echo "Stop tuike_consumer"
docker container stop tuike_consumer
echo "Remove tuike_consumer"
docker container rm tuike_consumer
echo "Run tuike_consumer"
docker run --env-file env.list --name tuike_consumer -d hoangmaihuy/tuike_consumer
