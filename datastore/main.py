from threading import*
import time

data = {}  # where we'll store the data in a dictionary

# create operation,
# use syntax "create(key_name,value)" you can use timeout value also."""


def create(key, value, timeout=0):
    if key in data:
        print("Error: This key is alredy registered")
    else:
        if(key.isalpha()):
            if len(data)<(1024*1020*1024) and value <= (16*1024*1024):
                if timeout == 0:
                    l = [value, timeout]
                else:
                    l = [value, time.time()+timeout]
                if len(key) <= 32:
                    data[key] = l
            else:
                print("Error: Memory limit reached")
        else:
            print("Error: Invalid key_name! key_name must contain only alphabets")

# for read operation "read(key_name)"


def read(key):
    if key not in data:
        print("Error: Key is not exist . please enter correct Key")
    else:
        b = data[key]
        if b[1] != 0:
            if time.time() < b[1]:
                # to return the value in the format of JasonObject i.e.,"key_name:value"
                show = str(key)+":"+str(b[0])
                return show
            else:
                print("Error: ", key, "is Expired")
        else:
            show = str(key)+":"+str(b[0])
            return show

# for delete operation


def delete(key):
    if key not in data:
        print("Error: key is not available")
    else:
        b = data[key]
        if b[1] != 0:
            if time.time() <b[1]:
                del data[key]
                print("Key is successfully deleted")
            else:
                print("Error:",key, "is Expired")
        else:
            del data[key]
            print("key is successfully deleted")
