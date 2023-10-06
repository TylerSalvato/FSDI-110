import pymongo
import certifi

developer = {
    "first": "Tyler",
    "last": "Salvato",
    "age": 28,
    "email": "tylersalvato727@gmail.com",
    "hobbies": ["code", "music"],
    "address": {
        "num": 1017,
        "street": "athens",
        "city": "raleigh"
    }
}




con_str = "mongodb+srv://tylersalvato727:monGodb_ch40@cluster0.lfizo41.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("loadingfocus")

