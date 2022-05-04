import socket

ADDRESS = "djxmmx.net"


def get_quote():
    addr = (ADDRESS, 17)
    conn = socket.create_connection(addr)
    quote = conn.recv(4096)

    return quote.decode("utf-8")
