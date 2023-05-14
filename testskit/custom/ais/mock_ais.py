from typing import Any

from pyais import encode_dict

from testskit.conf.protocol.socket import SocketConfig


class ShipAIS:
    """
    Mock sending AIS messages to a socket.
    """
    mmsi: int = None
    course: float = None
    speed: float = None
    position: tuple = None

    def __init__(
            self,
            config: SocketConfig
    ):
        self._socket = config

    def encode_msg(
            self
    ) -> Any:
        lon, lat = self.position
        msg = {
            'mmsi': self.mmsi,
            'type': 1,
            'course': self.course,
            'speed': self.speed,
            'lon': lon,
            'lat': lat
        }
        return encode_dict(
            msg,
            talker_id='AIVDM'
        )[0]

    def send_ais_msg(
            self
    ) -> None:
        self._socket.send_msg(
            self.encode_msg()
        )
