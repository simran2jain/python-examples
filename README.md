# python-examples

## this repository has code samples for following client/server scenarios:
### In general, client request data using "send data" then server reads the input file and sends each string in it to client. Sleep has been introduced in process_request function by client to simulate CPU operation.

CASE1: Single thread client and single threaded server
Instructions - Run server/server-single_thread.py in one window then client/client.py in another

![client](https://github.com/simran2jain/python-examples/assets/8279640/4d313f67-4b0c-47ac-98df-40d064440035)


CASE2: Multiple client(simulated via multithreaded client) and multithreaded  server
Instructions - Run server/server-multiple_threads.py in one window then client/client-multithreaded.py in another

![multithreaded](https://github.com/simran2jain/python-examples/assets/8279640/76291965-6f66-4a91-b17d-05dd31c93b16)


CASE3: Multiple client(simulated via multithreaded client) and multiprocessing server
Instructions - Run server/server-multiple_processes.py in one window then client/client-multithreaded.py in another

![cs_multiprocessor](https://github.com/simran2jain/python-examples/assets/8279640/1745fe3a-a8d9-4827-abfc-5ceb4b42d4e1)

General Intructions:
1. Update client-multithreaded.py LineNo#35 to change number of client to be simulated
2. Update input data file(data/myfile.txt) using data/manage-data.py
