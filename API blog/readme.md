I created an API blog with auth for learn about API and autentication concepts splited in seven python files for modularization.

b1database = Created for sqlite configuration with sqlalchemy librarie, he create the databank and start the data engine

b2modelos = Created a physic structure for the databank using sqlalchemy with 2 classes, User and Post, the class User create the username, an variable for putting the email in unique mode (emailstr) and the password hash for list users, by the way, the class Post is to create the publicatins variables with n+1 relationship, he have a foreign key inside in a variable to link each Post for user.

b3listasegura = Is the main file for data validation who enter and quit from the API

b4jwt = Control the critic part for security information using bcrypt to transform the hash password in a criptgrafed password and use the JWT to create acess tokens with key expiration.

b5auth = Create the endpoints for acess and exit with APIrouter

b6authsemlogin = Logic for the blog with a guard system, he take the b3,b4 and b5 files for unify the system for create a ''social media'' for validation the logins and publications

main = the engine for this concept learned project, he start the FastAPI, configure the logging system for catch errors, unify all routers for autentication and posts in an unique interface and run through the uvicorn app in respective port.