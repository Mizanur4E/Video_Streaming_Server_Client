import socket
import struct
import time

import cv2
import pickle

class client:
    def __init__(self, server_ip, server_port) -> None:
        # Initilization code
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_ip = server_ip
        self.server_port = server_port

    def connect_to_server(self) -> None:
        # Code to connect to server
        self.client_socket.connect((self.server_ip,self.server_port))


    def receive_video_data(self) -> None:
        data = b""
        try:
            payload_size = struct.calcsize("Q")
            #print(payload_size)
            while True:
                print('counting..1')
                # Code to receive messages chunk by chunk 
                # and constitute them into full message

                while len(data) < payload_size:
                    packet = self.client_socket.recv(4*1024)
                    if not packet:
                        break
                    print(packet)
                    data += packet

                print('counting..2')
                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                print(packed_msg_size)
                msg_size = struct.unpack("Q",packed_msg_size)[0]
                
                while len(data) < msg_size:
                    data += self.client_socket.recv(4*1024)
                frame_data = data[:msg_size]
                data = data[msg_size:]
                frame = pickle.loads(frame_data)
                cv2.imshow("RECEIVING VIDEO",frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                #time.sleep(1)
                print('counting..3')
            cv2.destroyAllWindows()
            self.client_socket.close()
        except KeyboardInterrupt:
            self.client_socket.close()