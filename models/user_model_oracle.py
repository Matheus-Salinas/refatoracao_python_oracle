from database.db import conectar
from dotenv import load_dotenv
import os

try:
    load_dotenv(encoding='utf-8')
except:
    pass  

class UserModelOracle:
    @staticmethod
    def criar_tabela():
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("""
                BEGIN
                    EXECUTE IMMEDIATE 'CREATE TABLE usuarios (
                        id NUMBER GENERATED ALWAYS AS IDENTITY,
                        nome VARCHAR2(100) NOT NULL,
                        email VARCHAR2(100) NOT NULL UNIQUE
                    )';
                EXCEPTION
                    WHEN OTHERS THEN
                        IF SQLCODE != -955 THEN
                            RAISE;
                        END IF;
                END;
            """)
            conn.commit()
        finally:
            if conn:
                conn.close()