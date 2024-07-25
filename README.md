# curly-octo-goggles
fastapi games

## Getting started

Set general .env in project folder:

    nano .env
    
example .env file
    
    EVENTS_PORT=5000
    EVENTS_URL=http://events:5000
    ODDS_PORT=5050

Deploy and create tables:
    
    docker-compose up --build -d
    docker exec -it curly-octo-goggles_events_1 bash -c "alembic upgrade head"

- events service swagger: http://0.0.0.0:5000/docs#/
- odds service swagger: http://0.0.0.0:5050/docs#/