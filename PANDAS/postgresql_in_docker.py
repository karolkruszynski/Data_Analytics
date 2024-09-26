# IMPORTS
import pandas as pd
import numpy as np

# how to pull postgres after install docker
# docker pull postgres - in cmd

# how to acitivate postgresql
# docker run --name postgresql -e POSTGRES_USER=username -e POSTGRES_PASSWORD=mypass -p 5432:5432 -v /data:/var/lib/postgresql/data -d postgres

# how to install pgadmin
# docker pull dpage/pgadmin4:latest

# how to activate pgadmin
# docker run --name "pgadmin4" -p 8082:80 -e "PGADMIN_DEFAULT_EMAIL=email@domain.com" -e "PGADMIN_DEFAULT_PASSWORD=mypasswrd" -d dpage/pgadmin4

# enter the local host of pgadmin4
# install the library to establish connection with db
# pip install psycopg2

# PREP for conn with db
import psycopg2
from sqlalchemy import create_engine
dbhost = 'karol:Klass535docker@localhost'
port = '5432'
conn_str='postgresql+psycopg2://'+str(dbhost)+':' + str(port) + '/postgres'
engine = create_engine("postgresql://karol:Klass535docker@localhost:5432/karol")
frame = pd.DataFrame(np.random.random((4,4)),
                     index=['exp1','exp2','exp3','exp4'],
                     columns=['feb','mar','apr','may'])
# transfer df to table
frame.to_sql("dataframe", conn_str, method='multi')

# or
# use a psql sesion
# open cmd
# docker login
# docker ps
# docker exec -it postgresql bash
# psql -h localhost -U karol
# \c postgres - connectiong to db

