<!-- Hướng dẫn -->

Cách git clone

cp env

docker-compose -f docker-compose.yml up -d

<!-- Hướng dẫn -->

docker-compose.yml
mysql
python
FastAPI
sqlalchemy
Bảng SQL User
Các thư viện khác jwt
alembic

<!-- python-multipart==0.0.9 -->
<!-- SQLAlchemy==2.0.32 -->
<!-- sqlmodel -->
<!-- alembic==1.13.2 -->
<!-- PyJWT==2.9.0 -->
<!-- bcrypt==4.2.0 -->
<!-- PyMySQL==1.1.1 -->

cryptography==43.0.1
pyotp==2.9.0
qrcode==7.4.2
rsa==4.9
passlib==1.7.4

<!--  -->



<!-- https://localhost:1337 -->
<!-- http://kong_api_gateway:8001 -->

start Chrome https://localhost:8443/api/microservices_auth/docs
start Chrome https://localhost:8443/api/microservices_auth/openapi.json

start Chrome https://localhost:8443/api/microservices_hello/docs
start Chrome https://localhost:8443/api/microservices_hello/openapi.json

start Chrome https://localhost:8443/api/microservices_user_python/docs
start Chrome https://localhost:8443/api/microservices_user_python/openapi.json

start Chrome https://localhost:8443/api/microservices_user_javascript/docs
start Chrome https://localhost:8443/api/microservices_user_javascript/openapi.json

start Chrome https://localhost:8443/api/microservices_user
start Chrome https://localhost:8443/api/microservices_user/api/microservices_user_javascript/docs
start Chrome https://localhost:8443/api/microservices_user/docs
<!-- alembic init migrations -->
<!-- alembic downgrade base -->

<!-- alembic upgrade head -->

alembic downgrade -1

<!-- alembic upgrade +1 -->
<!-- alembic revision --autogenerate -m "init migration" -->
<!-- alembic revision --autogenerate -m "create first user table: id, username, password" -->
<!-- alembic revision --autogenerate -m "add is_admin column to user table" -->
<!-- alembic revision --autogenerate -m "add name, age, email, created_at column to user table" -->

<!-- !xem lại regex -->
<!-- !xem lại comment -->
<!-- !xem lại ai docs -->
<!-- !xem lại ai log -->

<!-- Kong api gateway  -->

<!-- microservices: -->
<!-- auth services: Đăng ký, Đăng nhập -->
<!-- user services: python User py + javascript User js => thông tin user (curent user) Return current user -->
<!-- hello services: python hello + name Return hello + NAME -->

<!-- 10 lần request  -->

<!-- !MIXIN -->

<!-- Code lại lua auth -->
<!-- Xóa kangA -->
<!-- Tạo file .sh -->

<!-- request xem cân bằng tải -->
<!-- request   rate limit -->
# http://localhost:8001/upstreams
# http://localhost:8001/services
# http://localhost:8001/plugins
