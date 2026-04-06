This project is a backend ecosystem with FastAPI, i wanted to learn more about modular concepts and created with a databank (SQLITE) for study aplicattion and language models (LLM) with Groq.

Files:

c1banco.py : The base, manage the conection the sqlalchemy databank and create the work sessions.

c2modelos.py : The skeleton, create the databank tables (users, tasks and chat history).

c3moldes.py : The contracts, create the laws about data enter and exit for the API just accepts valids informations.

c4jwt.py : The chest, contain the criptografy logic for the passwords (hash) and the emission/validation of JWT tokens(access keys).

c5IA.py : The brain, engine for take the message context, reclaim the tasks and last messages inside of the data bank and send to LLM model.

c6rotas.py : Control painel, create the API address for register, login and the send of messages.

main.py : The principal file for run the project, he run the server, config the logs and unify all above modules.