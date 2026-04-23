Modular system for processing payments in second plane

x1 = Infra, generate and start the redis system

x2 = Data contract, create the format for tasks and requests

x3 = Worker, consume the queue and send to services

x4 = routes, API endpoints and stripe webhook

x5 = financial logic, real integration with api 

x6 = The engine, start point for ON the uvicorn