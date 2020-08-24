import mysql.connector

def DataUpdate(travel_date,travel_period,trip_type,adults,child,budget,Name,email,phno):
   mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="",
     database="travel_agency_chatbot1"
   )

   mycursor = mydb.cursor()

   #sql = "CREATE TABLE clients (travel_date VARCHAR(20),travel_period VARCHAR(20),trip_type VARCHAR(30),adults VARCHAR(20), child VARCHAR(30),budget VARCHAR(20),Name VARCHAR(30),email VARCHAR(20),phno VARCHAR(10));"
   sql='INSERT INTO clients (travel_date,travel_period,trip_type,adults,child,budget,Name,email,phno) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}");'.format(travel_date,travel_period,trip_type,adults,child,budget,Name,email,phno)

   mycursor.execute(sql)

   mydb.commit()

   print(mycursor.rowcount,"record inserted.")

if __name__ =="__main__" :
   DataUpdate("19August","10days","adventure","3+", "none","$3990","Mayur","mayur@gmail.com","987654321")