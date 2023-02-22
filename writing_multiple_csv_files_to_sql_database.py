#imports
import pyodbc
import pandas as pd
import sqlalchemy as db
import urllib
import os
import glob
import chardet
from sqlalchemy import create_engine, func
from sqlalchemy import select, insert, update, delete
from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, Session, sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy import text


params = 'Driver={ODBC Driver 17 for SQL};' \
        'Server=Servername;' \
        'Database=Database name;' \
        'UID=User;' \
        'PWD=Password;'

params = urllib.parse.quote_plus(params)

engine = db.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
connection = engine.connect()

os.chdir(Foldername)
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

metadata = db.MetaData()
session = sessionmaker()
my_session = session()
Base = declarative_base()

class finaltable(Base):
    __table__ = 'Users'
    CustomerID=db.Column( "CustomerID",db.String(255), primary_key=True)
    Customer=db.Column("Customer" ,db.String(255))
    Phone = db.Column("Phone",db.String(255))
    Email = db.Column("Email",db.String(255))
    DataSource = db.Column("DataSource",db.String(255))

for i in range(len(all_filenames)):
    with open(all_filenames[i], 'rb') as f:
        result = chardet.detect(f.read())
        df = pd.read_csv(all_filenames[i], encoding=result['encoding'])
        df.to_sql('Users', con=engine, index=False, if_exists='append')
        query = db.update(finaltable).where(finaltable).where(finaltable.DataSource == None).values(DataSource = all_filenames)