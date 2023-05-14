import socket


class SocketConfig:
    """
    Send UDP messages to a socket.
    """

    def __init__(self, ip: str, port: int):
        self._ip = ip
        self._port = port

    def send_msg(self, msg) -> None:
        addr = (self._ip, self._port)
        with socket.socket(
                socket.AF_INET,
                socket.SOCK_DGRAM
        ) as s:
            s.sendto(msg.encode(), addr)
