import socket

def start_client():
    # Set up UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)  # Server address (same as server's address)
    
    while True:
        # Get user input and send to server
        message = input("Enter message to send (or 'exit' to quit): ")
        if message.lower() == 'exit':
            print("Exiting...")
            break
        
        # Send message to server
        client_socket.sendto(message.encode(), server_address)
        
        # Receive the echoed message from the server
        response, _ = client_socket.recvfrom(4096)
        print(f"Received from server: {response.decode()}")

    # Close the socket after exiting the loop
    client_socket.close()

if __name__ == "__main__":
    start_client()
