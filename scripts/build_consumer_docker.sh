echo "Building tuike_consumer"
docker build -t hoangmaihuy/tuike_consumer:latest . -f tuike_consumer/Dockerfile
echo "Pushing to Dockerhub"
docker push hoangmaihuy/tuike_consumer:latest