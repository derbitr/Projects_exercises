My second API, this API was for fix the learned concepts in the last A.I project, following the clean architecture, i splited the files for security and escalability.

v1banco.py : Manage the connection with the data bank using Sqlalchemy and create sessions.

v2modelos.py : Create the data estructure with 1:N relationships.

v3moldes.py : Data contracts via Pydantic, keep the data and exit information inside a security laws and rules.

v4jwt.py : Implement security with Bcrypt for transform password into a criptografed hash passwords and use JWT (Json web tokens) for autentication and session control.

v5ia.py : The brain, he rescue the pendents tasks and the lasts messages from data bank for create a custom prompt system for the LLM model (Groq).

v6rotas.py : Control Painel, center all API endpoints, implement a "guard" for identify the user.

main.py : The engine for run the project, run the Uvicorn server, config the global logs and confirm automatic creation of tables inside data bank.