# MicroKit

This is a simple kit for building microservices based on the Event Sourcing and CQRS patterns using the Kafka message broker.

## Features

- **Event Sourcing**: All changes to the application state are stored as a sequence of events.
- **CQRS**: Command Query Responsibility Segregation.
- **Kafka**: A distributed event streaming platform.
- **Docker**: Docker Compose for running the application.

## Getting Started

1. Clone the repository:

```bash
git clone
```

2. Run the application:

```bash
docker-compose up
```

3. Access the application:

- [API Gateway](http://localhost:8800)
- [Product Service](http://localhost:8801)
- [Order Service](http://localhost:8802)

4. Run the API tests:

```bash
docker-compose exec api npm test
```

5. Run the Product Service tests:

```bash
docker-compose exec product npm test
```

6. Run the Order Service tests:

```bash
docker-compose exec order npm test
```

7. Run UI tests (Playwright):

```bash
docker-compose exec ui npm test
```

## Architecture

The application is composed of three services:

- **API Gateway**: The entry point for the application.
- **Product Service**: Manages the products.
- **Order Service**: Manages the orders.

The services communicate with each other using Kafka topics.

## API Gateway

The API Gateway is responsible for routing requests to the appropriate service.

### Endpoints

#### Product Service

- **GET /products**: Get all products.
- **GET /products/{id}**: Get a product by id.
- **POST /products**: Create a product.
- **PUT /products/{id}**: Update a product by id.
- **DELETE /products/{id}**: Delete a product by id.

#### Order Service

- **GET /orders**: Get all orders.
- **GET /orders/{id}**: Get an order by id.
- **POST /orders**: Create an order.
- **PUT /orders/{id}**: Update an order by id.
- **DELETE /orders/{id}**: Delete an order by id.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Event Sourcing and CQRS with Kafka](https://www.confluent.io/blog/event-sourcing-cqrs-stream-processing-apache-kafka-whats-connection/)
- [Event Sourcing Pattern](https://microservices.io/patterns/data/event-sourcing.html)
- [CQRS Pattern](https://microservices.io/patterns/data/cqrs.html)
- [Kafka](https://kafka.apache.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Microservices](https://microservices.io/)