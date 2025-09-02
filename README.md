# youtube-music-converter (backend)

Backend em FastAPI + SQLAlchemy 2 + Alembic + Postgres.

## Requisitos
- Docker Desktop
- PowerShell (Windows) ou terminal equivalente

## Passos para rodar

### 1. Clonar o projeto
git clone <URL-DO-REPO>
cd youtube-music-converter

### 2. Criar arquivo .env
copie do exemplo:
DATABASE_URL=postgresql+psycopg2://app:app@db:5432/yt2mp3

### 3. Subir containers
docker-compose build
docker-compose up

### 4. Rodar migrations
docker-compose run --rm api python -m alembic revision --autogenerate -m "init schema"
docker-compose run --rm api python -m alembic upgrade head

### 5. Testar com curl
# health
curl http://localhost:8000/health

# criar usuário
curl -X POST "http://localhost:8000/users?email=test@example.com&password_hash=123"

# listar usuários
curl http://localhost:8000/users

## Fluxo de desenvolvimento
- alterou models? gere migration e rode upgrade head
- alterou requirements/Dockerfile? docker-compose build
