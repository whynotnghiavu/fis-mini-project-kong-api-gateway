from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from environs import Env
from database import Base
from app.auth.models.user import User

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata
# target_metadata = None


env = Env()
MYSQL_HOST = env.str("MYSQL_HOST", default="localhost")
MYSQL_PORT = env.int("MYSQL_PORT", default=3306)
MYSQL_ROOT_PASSWORD = env.str("MYSQL_ROOT_PASSWORD", default="")
MYSQL_DATABASE = env.str("MYSQL_DATABASE", default="database")
MYSQL_USERNAME = env.str("MYSQL_USERNAME", default="root")
MYSQL_PASSWORD = env.str("MYSQL_PASSWORD", default="")

SQLALCHEMY_DATABASE_URL = f"mysql+aiomysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
SQLALCHEMY_DATABASE_URL = env.str("SQLALCHEMY_DATABASE_URL", default=SQLALCHEMY_DATABASE_URL)
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()