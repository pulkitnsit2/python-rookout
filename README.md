# Python Rookout Test

1. Clone the repository
2. cd client_server
3. export ROOKOUT_TOKEN=""
4. python3 server/client_server.py
5. Add a breakpoint at client_server.py:37, with log message: 'request.args: {request.args}, request.url: {request.url}'
6. Execute a GET request by opening: http://localhost:1337/?test=true
7. The log message shows:  
'request.args: \<Missing>, request.url: \<Missing>'  
instead of  
'request.args: {'test': ['true']}, request.url: http://localhost:1337/?test=true'
8. Same log message can be seen printed by python logger due to line client_server.py:34