python --version

python -m venv venv

venv/Scripts/activate

python -m pip install fastapi uvicorn celery redis flower python-jose[cryptography]

python -m pip install --upgrade pip

python -m pip install fastapi uvicorn python-multipart

python -m pip install python-dotenv

python -m pip install sqlalchemy pymysql

python -m pip --version

python -m ensurepip --upgrade

python -m pip install python-jose[cryptography]


python -m uvicorn main:app --reload (To start fastApi server )

python -m uvicorn server:app --reload


###### SQLAlchemy migration tool ########

pip install alembic
alembic init migrations

## Create Table Using migration
alembic upgrade head

## Remove All & do fresh:
alembic downgrade base
alembic upgrade head


### Token Generation
pip install python-jose passlib[bcrypt]


########### Swagger #############################################################
http://127.0.0.1:8000/swagger
http://127.0.0.1:8000/redoc-swagger
http://127.0.0.1:8000/swagger.json
#################################################################################


#### Redis install ##############################################################
pip install redis
python -m pip install redis
#################################################################################

############ set path in windows environment then run below command #############
- install redis from https://github.com/tporadowski/redis/releases
- redis-server
#################################################################################

############ install Celery #####################################################
pip install celery
#################################################################################

######## Start Worker ############################################################
python -m celery -A celery_worker.celery worker --loglevel=info
python -m celery -A celery_worker.celery worker --loglevel=info --pool=solo
##################################################################################

##################################################################################
pip install flower
python -m celery -A celery_worker.celery flower
    - http://localhost:5555
##################################################################################