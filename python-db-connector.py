import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root123",database="credence")

mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM imageblob")

def Insertblob(FilePath):  #insert image into db code
	with open(FilePath,"rb") as File:
		BinaryData=File.read()
	SqlStmt="INSERT INTO imageblob (image) VALUES (%s)"
	mycursor.execute(SqlStmt,(BinaryData))
	mydb.commit()

def Retrieveblob(ID):
	SqlStmt2="SELECT * FROM imageblob WHERE id='{0}'"
	mycursor.execute(SqlStmt2.format(str(ID)))
	MyRes=mycursor.fetchone()[1]
	StoreFilePath="ImageOutputs/img{0}.jpg".format(str(ID))
	print(MyRes)
	with open(StoreFilePath,"wb")as File:
		File.write(MyRes)
		File.close()


print("1. Insert image \n 2.Read image")
MenuInput=input()
if int(MenuInput) ==1:
	UserFilepath==input("Enter file path:")
elif int(MenuInput)==2:
	UserIDchoice= input("Enter id:")
	Retrieveblob(UserIDchoice)