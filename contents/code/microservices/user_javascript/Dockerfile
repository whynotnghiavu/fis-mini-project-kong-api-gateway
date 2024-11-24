FROM node:18

WORKDIR /services

COPY package*.json ./

RUN npm install

COPY . /services
CMD ["bash", "/services/start-service.sh"]
