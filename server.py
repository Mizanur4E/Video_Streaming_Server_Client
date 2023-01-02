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


    def client_handler(self, client_socket):

        if client_socket is None:
            return
        #path_to_video_file = "/home/nayan/Videos/Webcam/amk.mp4"

        path_to_video_file = "/home/nayan/Gulshan-02-New/Gulshan 02 New DVR-02_ch5_20221111075758_20221111180644.avi"


        vid = cv2.VideoCapture(path_to_video_file)


        try:
            while vid.isOpened():
                img, frame = vid.read()
                #print('Sending data for:', client_socket)
                frame = cv2.resize(frame, self.video_dim, fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
                a = pickle.dumps(frame)
                message = struct.pack("Q", len(a)) + a
                client_socket.sendall(message)
                #cv2.imshow('Sending...', frame)
                key = cv2.waitKey(10) & 0xFF
                if key == ord("q"):
                    client_socket.close()
        except:
            pass

    
    def serve(self) -> None:
        try:
            while True:
                Client, address = self.server_socket.accept()
                print('Connected to: ' + address[0] + ':' + str(address[1]))
                threading.Thread(target=self.client_handler, args=(Client,)).start()

        except KeyboardInterrupt:
            self.server_socket.close()
