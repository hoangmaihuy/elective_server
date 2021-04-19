sudo docker run --env-file env.list --name tuike_consumer -d tuike_consumer

sudo docker run -p 8000:8000 --env "PORT=8000" --env-file env.list --name tuike_api -d tuike_api
