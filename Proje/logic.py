import sqlite3
from config import DATABASE
import os

class DB_Manager:
    def __init__(self, database):
        self.database = database
 

    def __select_data(self, sql, data = tuple()):
            conn = sqlite3.connect(self.database)
            with conn:
                cur = conn.cursor()
                cur.execute(sql, data)
                return cur.fetchall()
            
            
    def Rate(self,x):
         sql="""
        SELECT Name, Rate , Date
        FROM tablo_adi
        WHERE Rate > ? 
        ORDER BY Rate DESC;
    """
         return self.__select_data(sql,(x,))
    

    def Date(self,x):
         sql="""
        SELECT Name,Date
        FROM tablo_adi
        WHERE Date > ?
        ORDER BY Date DESC;
    """
         return self.__select_data(sql,(x,))
         
         
    def Genre(self,x):
         sql="""
        SELECT Name,Genre
        FROM tablo_adi
        WHERE Genre LIKE ?;

    """
         return self.__select_data(sql,(f'%{x}%',))

         
         
    def Type(self,x):
         sql="""
        SELECT Name,Type
        FROM tablo_adi
        WHERE Type = ? 

    """
         return self.__select_data(sql,(x,))
    
    def ep(self,x):
         sql="""
        SELECT Name,Episodes
        FROM tablo_adi
        WHERE Episodes > ? 
        ORDER BY Episodes DESC;

    """
         return self.__select_data(sql,(x,))
    



#Çağırma fonksiyonları
A=DB_Manager("imdb.db")
asd=A.Genre("Drama")
print(asd)

            

    

