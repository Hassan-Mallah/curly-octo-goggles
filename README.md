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
    docker exec -it <events container> bash -c "alembic upgrade head"