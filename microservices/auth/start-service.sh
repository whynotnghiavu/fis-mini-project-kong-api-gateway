#!/bin/bash
bash /services/wait-for-it.sh microservices_mysql:3306 -- echo ">>> microservices_mysql:3306 <<<"
cd /services
alembic upgrade head
python main.py
