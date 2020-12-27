# File-based-key-value-data-store-with-basic-CRD
File-based key-value data store that supports the basic CRD (create, read, and delete) operations. This data store is meant to be used as a local storage for one single process on one laptop. The data store will be exposed as a library to clients and that can instantiate a class and can work with data store.

Usage:
NOTE:- you should import from the directory where the folder of datafilestore is located 
       If you import from inside the folder datafilestore then it'll print message of module not found.

>>> from datafilestore import datastore_invoke 

General Instructions:

>>> print(datastore_invoke(0))
Operation Not Found  
1 for Create (--client --key  --ttl(optional) --value --filepath(optional)) 
2 for Read (--client --key --filepath(optional)) 
3 for Delete (--client --key --filepath(optional)) 
4 for Reset (--client --filepath(optional))

Create Operation with file path

>>> print(datastore_invoke(1, client = "raw" , key = "student_data", value = '{"student":"sultan"}', filepath = "/Users/jeysu/Desktop/"))
Create Operation Done

Create Operation

>>> print(datastore_invoke(1, client = "raw" , key = "student_data", value = '{"student":"sultan"}'))
Create Operation Done

Create Operation with Time to Live feature

>>> print(datastore_invoke(1, client = "raw" , key = "student_data_temp", value = '{"student":"mahin"}', ttl = 30 ))
Create Operation Done

Read Operation

>>> print(datastore_invoke(2, client = "raw" , key = "student_data"))
For key | student_data | value  - {'student': 'sultan'} 

Read Operation TTL Expired

>>> print(datastore_invoke(2, client = "raw" , key = "student_data_temp"))
Error Status : TTL Value for the Key - student_data_temp expired for the client - raw

Delete Operation

>>> print(datastore_invoke(3, client = "raw" , key = "student_data"))
Error Status : For key | student _data | value - is deleted

Delete Operation TTL Expired

>>> print(datastore_invoke(3, client = "raw" , key = "student_data_temp"))
Error Status : TTL Value for the Key - student_data_temp expired for the client - raw

    Note: After Delete Option if the client storage file is empty, A forced reset operation is performed

Reset Operation - Delete Entire file

>>> print(datastore_invoke(4, client = "raw" ))
File removed!!!! - raw

TEST OUTPUT:-
python mock_unit.py

######## General Test ########



*************** Create mode mock test units ***************


Create Operation Done

Error Status : Key's datatype should be String

Error Status : Key | mock_test | already exist , value - {'employee': 'sultan', 'status': 'fresher', 'role': 'software_engineer'}

Error Status : Character limit for Key is 32, But it has 34

Error Status : Key's datatype should be String

Error Status : Value's datatype should be JSON object (Dict)

Create Operation Done



*************** Read mode mock test units ***************


For key | mock_test | value  - {'employee': 'sultan', 'status': 'fresher', 'role': 'software_engineer'}

Key | 12 | not found for client - raw

Error Status : Behire - Client_file_doesnot_exist

For key | Executive | value  - {'Registered_firm': {'firm': 'sultan', 'location': 'guwahati', 'products': {'Product-1': 'migrate', 'Product-2': 'hover_page', 'Product-3': 'ground_truth'}}}


Sleeping mode...

Error Status : TTL Value for the Key - Executive expired for the client - raw



*************** Delete mode mock test units ***************


Error Status : For key | mock_test | value - is deleted

Key | Reamsochung Chongapipa Aiill CFCS6 | not found for client - raw

Error Status : Special24 - Client_file_doesnot_exist

Error Status : TTL Value for the Key - Executive expired for the client - raw



*************** Reset mode mock test units ***************


File removed!!!! - raw
87Lane - Client_file_doesnot_exist

######## Thread-Safe Code Test ########

Create Operation Done

Error Status : Key | mock_test | already exist , value - {'employee': 'sultan', 'status': 'fresher', 'role': 'software_engineer'}

Error Status : Delete Operation Failed - Data Dumping failed

Thread-safe Testing done
