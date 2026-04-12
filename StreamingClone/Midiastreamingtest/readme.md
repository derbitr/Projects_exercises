For learning more API concepts i made a mini project for midia optimize.

a1motor.py: low level engine, read the video in chunks with yields generators for optimize memory.

a2rotas.py: HTTP protocol translator, catch the requests, calc the limits and config the status.

main.py: Engine for unify these 2 files for run the project in api using uvicorn.