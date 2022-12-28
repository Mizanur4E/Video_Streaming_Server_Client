from client import client

client = client('192.168.21.65', 10050)
client.connect_to_server()

client.receive_video_data()