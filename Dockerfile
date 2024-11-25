FROM node:18.20.5

WORKDIR /app/products

COPY package*.json .

RUN npm install

COPY . .

EXPOSE 8002

CMD ["npm", "start"]