echo "Building tuike_api"
docker build -t hoangmaihuy/tuike_api:latest .
echo "Pushing to Dockerhub"
docker push hoangmaihuy/tuike_api:latest