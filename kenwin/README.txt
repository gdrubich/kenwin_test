kenwin_test
===========

Getting Started
---------------

- Change directory into your newly created project.

    cd kenwin

- Create a Python virtual environment.

    virtualenv -p python3 envname

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its requirements.

    env/bin/pip install -e .
    
- Create PostgreSQL Database.

WARNING!: select a username according to your local system username -- this will come in handy when setting up peer authentication.

postgres=# CREATE USER username WITH PASSWORD 'password';
postgres=# CREATE DATABASE kenwin_test OWNER owner;

- Add next lines to "pg_hba.conf" file.

local   kenwin_test    username                                    peer
host    kenwin_test    username            127.0.0.1               md5


- Initialize and upgrade the database using Alembic. This will create an user with username 'admin_user' and password 'admin'.

    - Generate your first revision.

        env/bin/alembic -c development.ini revision --autogenerate -m "init"

    - Upgrade to that revision.

        env/bin/alembic -c development.ini upgrade head

- Load default data into the database using a script.

    env/bin/initialize_kenwin_db development.ini
    WARNING!: If this step throws an ImportError, try deactivating and activating back the virtual environment.

- Run the project.

    env/bin/pserve development.ini
