# python-examples

## this repository has code samples for following client/server scenarios:
### In general, client request data using "send data" then server reads the input file and sends each string int it to server. Sleep has been introduced in process_request function by client to simulate CPU operation.

CASE1: Single thread client and single threaded server
Instructions - Run server/server-single_thread.py in one window then client/client.py in another

CASE2: Multiple client(simulated via multithreaded client) and multithreaded  server
Instructions - Run server/server-multiple_threads.py in one window then client/client-multithreaded.py in another

CASE3: Multiple client(simulated via multithreaded client) and multiprocessing server
Instructions - Run server/server-multiple_processes.py in one window then client/client-multithreaded.py in another

General Intructions:
1. Update client-multithreaded.py LineNo#35 to change number of client to be simulated
2. Update input data file(data/myfile.txt) using data/manage-data.py
