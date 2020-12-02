import mysql.connector
Mydb=mysql.connector.connect(host="localhost",user="root",passwd="root123",database="credence")

Mycursor=Mydb.cursor()
Mycursor = Mydb.cursor(buffered=True)

Mycursor.execute("SELECT * FROM Picture ")

def Insertblob(FilePath):  #insert image into db code
	with open(FilePath,"rb") as File:
		BinaryData=File.read()
	SqlStmt="INSERT INTO Picture(photo) VALUES (%s)"
	Mycursor.execute(SqlStmt,(BinaryData,))
	Mydb.commit()

def Retrieveblob(ID): #retrieve img
	SqlStmt2="SELECT * FROM Picture WHERE id='{0}'"
	Mycursor.execute(SqlStmt2.format(str(ID)))
	MyRes=Mycursor.fetchone()[1]
	StoreFilePath="ImageOutputs/img{0}.jpg".format(str(ID))
	print(MyRes)
	with open(StoreFilePath,"wb")as File:
		File.write(MyRes)
		File.close()


print("1. Insert image\n2. Read image")
MenuInput=input()
if int(MenuInput)==1:
	UserFilepath=input("Enter file path:")
	Insertblob(UserFilepath)
elif int(MenuInput)==2:
	UserIDchoice= input("Enter id:")
	Retrieveblob(UserIDchoice)
