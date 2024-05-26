# python-examples
## this repository has code samples for following client/server scenarios:
CASE1: Single thread client and single threaded server
Instructions - Run server/server-single_thread.py in one window then client/client.py in another

CASE2: Multiple client(simulated via multithreaded client) and multithreaded  server
Instructions - Run server/server-multiple_threads.py in one window then client/client-multithreaded.py in another

CASE2: Multiple client(simulated via multithreaded client) and multiprocessing server
Instructions - Run server/server-multiple_processes.py in one window then client/client-multithreaded.py in another

General Intructions:
1. Update client-multithreaded.py LineNo#35 to change number of client to be simulated
2. Update input data file(data/myfile.txt) using data/manage-data.py
