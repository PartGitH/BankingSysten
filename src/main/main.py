from initialization import setup
from initialization import check
from panels import accounttype
from tools import connection
import time
while True:
    print("1.Continue")
    print("2.Quit")
    a=input("Enter your choice(1,2): ")
    if a == "1":
        if not check.check():
            query,cur=connection.cc()
            accounttype.acctype(query,cur)
            break
        else:
            setup.setup()
    elif a == "2":
        print("Shutting down the program")
        time.sleep(2)
        break
    else:
        print("Wrong input.")
        time.sleep(2)
