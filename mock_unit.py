from datafilestore import main
from time import sleep
import threading

class mock_unit:
	client = "raw"
	key = "mock_test"
	key_int = 12
	key_more_than_32 = "Reamsochung Chongapipa Aiill CFCS6"
	value_dict = {"Registered_firm" : 
	{ 
   "firm":"sultan",
   "location":"guwahati",
   "products":{ 
      "Product-1":"migrate",
      "Product-2":"hover_page",
      "Product-3":"ground_truth"
   }
   }
   }
	value_json_type = { "employee":"sultan", "status":"fresher", "role":"software_engineer" }
	value_string = "Bommanhalli, Madiwala"
	ttl_value = 10


def create(mock):
	print(main.create(mock.client, mock.key, mock.value_json_type)+"\n")			#Expect Success
	print(main.create(mock.client, mock.key_int, mock.value_json_type)+"\n")		#Expect Key error	
	print(main.create(mock.client, mock.key, mock.value_dict)+"\n")				#Expect Key already present
	print(main.create(mock.client, mock.key_more_than_32, mock.value_json_type)+"\n")#Expect Key error
	print(main.create("87Lane", mock.key_int, mock.value_dict)+"\n")				#Expect key error
	print(main.create(mock.client, "Employer", mock.value_string)+"\n")			#Expect value error
	print(main.create(mock.client, "Executive", mock.value_dict, ttl = mock.ttl_value)+"\n")	#Expect Success


def read(mock):
	print(main.read(mock.client, mock.key)+"\n")									#Expect Success
	print(main.read(mock.client, mock.key_int)+"\n")								#Expect Key error
	print(main.read("Behire", mock.key)+"\n")										#Expect Client not found error
	print(main.read(mock.client, "Executive")+"\n")								#Expect Success since TTL is still intact
	print("\nSleeping mode...\n")
	sleep(31)
	print(main.read(mock.client, "Executive")+"\n")								#Expect TTL error


def delete(mock):
	print(main.delete(mock.client, mock.key)+"\n")									#Expect Success
	print(main.delete(mock.client, mock.key_more_than_32)+"\n")					#Expect Key not exists
	print(main.delete("Special24", mock.key)+"\n")									#Expect Client not found error
	print(main.delete(mock.client, "Executive")+"\n")								#Expect TTL error


def create_2(mock):
	print(main.create("sherlock", mock.key, mock.value_json_type)+"\n")


def append_2(mock):
	print(main.create("sherlock", mock.key, mock.value_dict)+"\n")
	print(main.delete("sherlock", mock.key)+"\n")


def mock_unit_begin(mock):
	
	print( "\n\n*************** Create mode mock test units ***************\n\n")
	create(mock)
	print( "\n\n*************** Read mode mock test units ***************\n\n")
	read(mock)
	print( "\n\n*************** Delete mode mock test units ***************\n\n")
	delete(mock)
	print( "\n\n*************** Reset mode mock test units ***************\n\n")
	print(main.reset(mock.client))
	print(main.reset("87Lane"))

if __name__ == "__main__": 
    
    print("\n######## General Test ########\n")
    mock = mock_unit()
    mock_unit_begin(mock)

    print("\n######## Thread-Safe Code Test ########\n")
    # creating thread 
    t1 = threading.Thread(target=create_2, args=(mock,)) 
    t2 = threading.Thread(target=append_2, args=(mock,)) 
  
    t1.start() 
    t2.start() 
   
    t1.join() 
    t2.join() 
  
    # both threads completely executed 
    print("Thread-safe Testing done")