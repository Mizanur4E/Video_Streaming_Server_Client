from server import tcp_streaming_server 

server = tcp_streaming_server('127.0.0.1', 1024)
server.bind_socket()
server.listen()
server.client_handler()
server.serve()