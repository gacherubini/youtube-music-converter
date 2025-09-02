from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from logging.config import fileConfig


from app.db import Base
import app.models  
config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata
