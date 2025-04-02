import cx_Oracle
import os

def conectar():
    try:
        
        try:
            return cx_Oracle.connect(
                user=os.getenv('ORACLE_USER'),
                password=os.getenv('ORACLE_PASSWORD'),
                dsn=os.getenv('ORACLE_DSN')
            )
        except cx_Oracle.DatabaseError:
            
            return cx_Oracle.connect(
                user="c##prata25",
                password="sua_senha",
                dsn=cx_Oracle.makedsn("localhost", "1521", service_name="XE")
            )
    except Exception as e:
        print("Execute estes comandos de verificação:")
        print("1. lsnrctl services")
        print("2. tnsping XE")
        print("3. sqlplus c##prata25/sua_senha@XE")
        raise