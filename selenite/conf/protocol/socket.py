import socket


class SocketConfig:
    """
    Send UDP messages to a socket.
    """

    def __init__(
            self,
            *,
            ip: str,
            port: int
    ):
        self.addr = (ip, port)
        self.socket = None

    def open_socket(self):
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

    def send_msg(self, msg: str) -> None:
        """
        Send message to a socket.
        """
        with socket.socket(
                socket.AF_INET,
                socket.SOCK_DGRAM
        ) as s:
            s.sendto(
                msg.encode(),
                self.addr
            )
