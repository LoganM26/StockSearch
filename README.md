# StockSearch
CS361 Individual Project

When making a request to the save and load function of the microservice, the user must first connect to the 
relevant ZeroMQ socket after attaching the necessary context to the socket. This requires the zmq import.
After a successful connection, the user can now use socket to send messages over the API using socket.send().
Then, all the user has to do is call socket.recv() and wait for the server(in this case the microservice) to
respond with the expected result.

Example Request:
![image](https://github.com/LoganM26/StockSearch/assets/148154868/d853be22-cecc-4513-a466-077ff06bf234)

Example Return Value from Microservice:
![image](https://github.com/LoganM26/StockSearch/assets/148154868/6d54147d-75a4-44f7-9415-a1d9c58c1b81)

Example Written Value from Microservice:
![image](https://github.com/LoganM26/StockSearch/assets/148154868/84b1dc14-5afe-43d3-814a-543f14457a4a)
