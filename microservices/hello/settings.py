from environs import Env
from loguru import logger

log_file_format = "{time:YYYY-MM-DD}.log"
logger.add(f"logging/{log_file_format}", rotation="00:00", retention="7 days", enqueue=True)

env = Env()
logger.info(f"Loading environment variables...")


try:
    NAME_SERVICE = env.str("NAME_SERVICE")
except Exception as e:
    print(f"Error: {e}")


FASTAPI_ENVIRONMENT = env.str("FASTAPI_ENVIRONMENT", default="DEVELOPMENT")

SERVER_IP = env.str("SERVER_IP", default="0.0.0.0")
SERVER_PORT = env.int("SERVER_PORT", default=5005)


MYSQL_HOST = env.str("MYSQL_HOST", default="localhost")
MYSQL_PORT = env.int("MYSQL_PORT", default=3306)
MYSQL_ROOT_PASSWORD = env.str("MYSQL_ROOT_PASSWORD", default="")
MYSQL_DATABASE = env.str("MYSQL_DATABASE", default="database")
MYSQL_USERNAME = env.str("MYSQL_USERNAME", default="root")
MYSQL_PASSWORD = env.str("MYSQL_PASSWORD", default="")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
SQLALCHEMY_DATABASE_URL = env.str("SQLALCHEMY_DATABASE_URL", default=SQLALCHEMY_DATABASE_URL)


ADMIN_DEFAULT_NAME = env.str("ADMIN_DEFAULT_NAME", default="admin_name")
ADMIN_DEFAULT_AGE = env.int("ADMIN_DEFAULT_AGE", default=20)
ADMIN_DEFAULT_USERNAME = env.str("ADMIN_DEFAULT_USERNAME", default="admin_username")
ADMIN_DEFAULT_EMAIL = env.str("ADMIN_DEFAULT_EMAIL", default="admin_email")
ADMIN_DEFAULT_PASSWORD = env.str("ADMIN_DEFAULT_PASSWORD", default="admin_password")


JWT_SECRET = env.str("JWT_SECRET", default="secret")
JWT_ALGORITHM = env.str("JWT_ALGORITHM", default="HS256")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = env.int("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", default=30)
