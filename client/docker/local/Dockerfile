ARG NODE_VERSION=16.14-alpine

FROM node:${NODE_VERSION} as node

FROM node as client-local-build

ARG APP_HOME=/app

WORKDIR ${APP_HOME}

# Adicionando `/app/node_modules/.bin` para o $PATH
ENV PATH /app/node_modules/.bin:$PATH

COPY ./package*.json ./

# To Fix Permissions for Packages
RUN npm install 
# RUN npm install react-scripts@3.3.1 -g


COPY . ${APP_HOME}

CMD ["npm", "start"]
