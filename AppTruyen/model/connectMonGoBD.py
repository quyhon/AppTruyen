from pymongo import MongoClient

def registe(data):
    """Insert Data to DB"""
    client = MongoClient('mongodb+srv://an2623:An.tuan0508@cluster0-37bn2.mongodb.net/an2623?retryWrites=true&w=majority')
    mydb = client['PTPM']
    mycol = mydb["user"]
    try:
        mydict = { "_id": data[0], "user": data[0], "pass": data[1], "name" : data[2], "sex" : data[3]}
        x = mycol.insert_one(mydict)
        return 1
    except:
        return 0

def checkUser(user,password):
    """Find user in DB"""
    client = MongoClient('mongodb+srv://an2623:An.tuan0508@cluster0-37bn2.mongodb.net/an2623?retryWrites=true&w=majority')
    mydb = client['PTPM']
    mycol = mydb["user"]
    try:
        check = mycol.find({'_id':user})[0]
        if check['pass'] == password:
            return 1
        else:
            return 0
    except:
        return 0