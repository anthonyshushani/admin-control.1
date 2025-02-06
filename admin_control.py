import socket

def check_port(ip_address, port_number):
    try:
        # Create a new socket instance for Internet (INET) using TCP (STREAM)
        socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_connection.settimeout(1)  # Set how long to wait for a response from the server

        # Attempt to connect to the specified IP address and port
        connection_result = socket_connection.connect_ex((ip_address, port_number))
        if connection_result == 0:
            print(f"Port {port_number} is open on {ip_address}.")
        socket_connection.close()  # Close the socket to free up the system resources
    except Exception as error:
        print(f"An error occurred: {error}")

def main():
    ip_to_scan = input("Enter the IP address to scan: ")
    port_range_input = input("Enter the port range to scan (e.g., 20-80): ")
    start_port, end_port = map(int, port_range_input.split('-'))  # Split the input into start and end ports

    # Scan each port in the specified range
    for port in range(start_port, end_port + 1):
        check_port(ip_to_scan, port)

if __name__ == "__main__":
    main()