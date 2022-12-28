import socket
import pickle
import cv2
import struct
import threading
import time

class tcp_streaming_server:
    def __init__(self, ip, port) -> None:
        # Write Initialization Code Here
        self.video_dim = (800, 600)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)
        print('HOST IP:', self.host_ip)
        self.port = 10050
        self.socket_address = (self.host_ip,self.port)
        print('Socket created')

    def bind_socket(self) -> None:
        # Complete this
        self.server_socket.bind(self.socket_address)
        print("Completed: bind_socket..!")


    def listen(self) -> None:
        # Complete this
        self.server_socket.listen(5)
        print("Socket is listening..!")


    def client_handler(self):
        # if client_socket is None:
        #     return
        #path_to_video_file = "/home/nayan/Videos/Webcam/amk.mp4"

        path_to_video_file = "/home/nayan/Gulshan-02-New/Gulshan 02 New DVR-02_ch5_20221111075758_20221111180644.avi"
        while True:
            client_socket, addr = self.server_socket.accept()
            print('Connection from:', addr)
            if client_socket:
                vid = cv2.VideoCapture(path_to_video_file)
                while (vid.isOpened()):
                    img, frame = vid.read()
                    frame = cv2.resize(frame, self.video_dim, fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
                    a = pickle.dumps(frame)
                    message = struct.pack("Q", len(a)) + a
                    client_socket.sendall(message)
                    cv2.imshow('Sending...', frame)
                    key = cv2.waitKey(10) & 0xFF
                    if key == ord("q"):
                        client_socket.close()
        #
        # while vid.isOpened():
        #     print('In the loop...')
        #     client_socket, addr = self.server_socket.accept()
        #     print('Connection from:', addr)
        #     _, frame = vid.read()
        #     frame = cv2.resize(frame, self.video_dim, fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        #     a = pickle.dumps(frame)
        #     message = struct.pack("Q", len(a)) + a
        #     # Write Code to send Message
        #     client_socket.send(message)
        #
        #     cv2.imshow('From server:', frame)
        #     key = cv2.waitKey(1) & 0xFF
        #     if key == ord('q'):
        #         client_socket.close()
        #         break
        # cv2.destroyAllWindows()
        # print(vid.isOpened, ' exiting while...')


    
    def serve(self) -> None:
        try:
            # Code for multithreaded service
            pass
        except KeyboardInterrupt:
            self.server_socket.close()