from django.http import HttpResponse
from django.shortcuts import render
import pyrebase

config={
    "apiKey": "AIzaSyAyh5QR9Tzbw8kCS06j5H-uSqP8e_hnhYw",
    "authDomain": "college-kitchen-2441a.firebaseapp.com",
    "projectId": "college-kitchen-2441a",
    "storageBucket": "college-kitchen-2441a.appspot.com",
    "messagingSenderId": "16137420688",
    "databaseURL": "https://college-kitchen-2441a-default-rtdb.asia-southeast1.firebasedatabase.app",
    "appId": "1:16137420688:web:e587c54b986d739176bd15",
    "measurementId": "G-D20D0FZ55F",
}
firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()


def index(request):
    data=database.child('Data').child('Vegetable').get().val()
    list1=list(data.values())
    return render(request,'index.html',{
        "vegetable_list":list1
    })