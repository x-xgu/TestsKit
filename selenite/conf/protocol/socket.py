import socket


class SocketConfig:
    """
    A class for sending UDP messages to a socket.

    Args:
        ip (str): The IP address of the socket.
        port (int): The port number of the socket.

    Example:
        To create a SocketConfig object and send a message to a socket:

        >>> socket_config = SocketConfig(ip='127.0.0.1', port=5000)
        >>> socket_config.send_msg('Hello, world!')
    """

    def __init__(
            self,
            *,
            ip: str,
            port: int
    ) -> None:
        self.addr = (ip, port)
        self.socket = None

    def open_socket(self) -> None:
        """
        Open a socket connection.

        Returns:
            None

        Example:
            To open a socket connection:

            >>> socket_config = SocketConfig(ip='127.0.0.1', port=5000)
            >>> socket_config.open_socket()
        """
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

    def close_socket(self) -> None:
        """
        Close a socket connection.

        Returns:
            None

        Example:
            To close a socket connection:

            >>> socket_config = SocketConfig(ip='127.0.0.1', port=5000)
            >>> socket_config.open_socket()
            >>> socket_config.close_socket()
        """
        self.socket.close()

    def send_msg(self, msg: str) -> None:
        """
        Send a message to a socket.

        Args:
            msg (str): The message to be sent.

        Returns:
            None

        Example:
            To send a message to a socket:

            >>> socket_config = SocketConfig(ip='127.0.0.1', port=5000)
            >>> socket_config.send_msg('Hello, world!')
        """
        with socket.socket(
                socket.AF_INET,
                socket.SOCK_DGRAM
        ) as s:
            s.sendto(
                msg.encode(),
                self.addr
            )
