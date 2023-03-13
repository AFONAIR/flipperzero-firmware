#!/usr/bin/env python3

import os
import sys
import time

import serial

from flipperzero_protobuf_py.flipperzero_protobuf.flipper_base import \
    FlipperProtoException
from flipperzero_protobuf_py.flipperzero_protobuf.flipper_proto import \
    FlipperProto
from flippigator.flippigator import Gator, Navigator, FlipperTextKeyboard, FlipperHEXKeyboard


def main():
    print("Let's go!")
    port = "COM4"

    flipper = serial.Serial(port, timeout=1)
    flipper.baudrate = 2304000
    flipper.flushOutput()
    flipper.flushInput()
    flipper.timeout = None

    proto = FlipperProto(serial_port=flipper, debug=True)

    print("Request RPC session")
    proto.start_rpc_session()
    print("RPC session started")

    nav = Navigator(proto)
    nav.update_screen()

    key = FlipperHEXKeyboard(nav)
    key.send("0000123456")

    key = FlipperTextKeyboard(nav)
    key.send("KeyboardTest")

if __name__ == "__main__":
    main()
