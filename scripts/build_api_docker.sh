echo "Building tuike_api..."
docker build -t hoangmaihuy/tuike_api . --build-arg ENVIRONMENT=LIVE
echo "Pushing tuike_api to docker hub"
docker push hoangmaihuy/tuike_api:latest