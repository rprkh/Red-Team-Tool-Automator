#!/bin/bash

# Function to check if running on Windows
is_windows() {
    case "$(uname -s)" in
        CYGWIN*|MINGW32*|MSYS*|MINGW*)
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

# Check if the script is being run with sudo (only if not on Windows)
if ! is_windows && [[ $EUID -ne 0 ]]; then
    echo "Please run this script with sudo."
    exit 1
fi

# Check if Git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install Git and try again."
    exit 1
fi

# Function to install dependencies on Linux
install_package() {
    local package=$1

    case $OS in
        ubuntu|debian|kali)
            apt-get install -y "$package" || { echo "Failed to install $package. Please try again."; exit 1; }
            ;;
        centos|rhel|fedora)
            yum install -y "$package" || { echo "Failed to install $package. Please try again."; exit 1; }
            ;;
        arch)
            pacman -Sy --noconfirm "$package" || { echo "Failed to install $package. Please try again."; exit 1; }
            ;;
        *)
            echo "Unsupported Linux distribution: $OS"
            exit 1
            ;;
    esac
}

# Install dependencies based on the detected OS
if is_windows; then
    # Assuming Python and pip are already installed on Windows
    echo "Running on Windows..."
else
    # Detect Linux distribution
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        OS=$ID
    elif type lsb_release >/dev/null 2>&1; then
        OS=$(lsb_release -si | tr '[:upper:]' '[:lower:]')
    elif [ -f /etc/lsb-release ]; then
        . /etc/lsb-release
        OS=$DISTRIB_ID
    elif [ -f /etc/debian_version ]; then
        OS=debian
    elif [ -f /etc/fedora-release ]; then
        OS=fedora
    elif [ -f /etc/redhat-release ]; then
        if grep -q "CentOS" /etc/redhat-release; then
            OS=centos
        else
            OS=rhel
        fi
    else
        OS=$(uname -s | tr '[:upper:]' '[:lower:]')
    fi

    # Update package lists and install necessary packages
    case $OS in
        ubuntu|debian|kali)
            # apt-get update || { echo "Failed to update apt cache. Please check your internet connection or try again later."; exit 1; }
            install_package "python3-pip"
            ;;
        centos|rhel|fedora)
            install_package "python3-pip"
            ;;
        arch)
            install_package "python-pip"
            ;;
        *)
            echo "Unsupported Linux distribution: $OS"
            exit 1
            ;;
    esac
fi

# Install websocket-client using pip
pip install websocket-client

# Check for installation error with pip
if [ $? -ne 0 ]; then
  echo "Error: Failed to install websocket-client using pip."
  exit 1
fi

# Clone the repository
git clone https://github.com/websocket-client/websocket-client.git

# Check repository cloning
if [ $? -ne 0 ]; then
  echo "Error: Failed to clone the repository."
  exit 1
fi

# Rename the directory
mv websocket-client websocket_client

# Navigate to the required directory
cd websocket_client

# Create wsdump.py with the provided content
cat << 'EOF' > wsdump.py
"""
websocket - WebSocket client library for Python

Copyright (C) 2010 Hiroki Ohtani(liris)

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
"""

import argparse
import code
import sys
import threading
import time
import ssl
import gzip
import zlib
import collections
collections.Callable = collections.abc.Callable
import six
from six.moves.urllib.parse import urlparse

import websocket

try:
    import readline
except ImportError:
    pass


def get_encoding():
    encoding = getattr(sys.stdin, "encoding", "")
    if not encoding:
        return "utf-8"
    else:
        return encoding.lower()


OPCODE_DATA = (websocket.ABNF.OPCODE_TEXT, websocket.ABNF.OPCODE_BINARY)
ENCODING = get_encoding()


class VAction(argparse.Action):

    def __call__(self, parser, args, values, option_string=None):
        if values is None:
            values = "1"
        try:
            values = int(values)
        except ValueError:
            values = values.count("v") + 1
        setattr(args, self.dest, values)


def parse_args():
    parser = argparse.ArgumentParser(description="WebSocket Simple Dump Tool")
    parser.add_argument("url", metavar="ws_url",
                        help="websocket url. ex. ws://echo.websocket.org/")
    parser.add_argument("-p", "--proxy",
                        help="proxy url. ex. http://127.0.0.1:8080")
    parser.add_argument("-v", "--verbose", default=0, nargs='?', action=VAction,
                        dest="verbose",
                        help="set verbose mode. If set to 1, show opcode. "
                        "If set to 2, enable to trace  websocket module")
    parser.add_argument("-n", "--nocert", action='store_true',
                        help="Ignore invalid SSL cert")
    parser.add_argument("-r", "--raw", action="store_true",
                        help="raw output")
    parser.add_argument("-s", "--subprotocols", nargs='*',
                        help="Set subprotocols")
    parser.add_argument("-o", "--origin",
                        help="Set origin")
    parser.add_argument("--eof-wait", default=0, type=int,
                        help="wait time(second) after 'EOF' received.")
    parser.add_argument("-t", "--text",
                        help="Send initial text")
    parser.add_argument("--timings", action="store_true",
                        help="Print timings in seconds")
    parser.add_argument("--headers",
                        help="Set custom headers. Use ',' as separator")

    return parser.parse_args()


class RawInput:

    def raw_input(self, prompt):
        if six.PY3:
            line = input(prompt)
        else:
            line = raw_input(prompt)

        if ENCODING and ENCODING != "utf-8" and not isinstance(line, six.text_type):
            line = line.decode(ENCODING).encode("utf-8")
        elif isinstance(line, six.text_type):
            line = line.encode("utf-8")

        return line


class InteractiveConsole(RawInput, code.InteractiveConsole):

    def write(self, data):
        sys.stdout.write("\033[2K\033[E")
        # sys.stdout.write("\n")
        sys.stdout.write("\033[34m< " + data + "\033[39m")
        sys.stdout.write("\n> ")
        sys.stdout.flush()

    def read(self):
        return self.raw_input("> ")


class NonInteractive(RawInput):

    def write(self, data):
        sys.stdout.write(data)
        sys.stdout.write("\n")
        sys.stdout.flush()

    def read(self):
        return self.raw_input("")


def main():
    start_time = time.time()
    args = parse_args()
    if args.verbose > 1:
        websocket.enableTrace(True)
    options = {}
    if args.proxy:
        p = urlparse(args.proxy)
        options["http_proxy_host"] = p.hostname
        options["http_proxy_port"] = p.port
    if args.origin:
        options["origin"] = args.origin
    if args.subprotocols:
        options["subprotocols"] = args.subprotocols
    opts = {}
    if args.nocert:
        opts = {"cert_reqs": ssl.CERT_NONE, "check_hostname": False}
    if args.headers:
        options['header'] = list(map(str.strip, args.headers.split(',')))
    ws = websocket.create_connection(args.url, sslopt=opts, **options)
    if args.raw:
        console = NonInteractive()
    else:
        console = InteractiveConsole()
        print("Press Ctrl+C to quit")

    def recv():
        try:
            frame = ws.recv_frame()
        except websocket.WebSocketException:
            return websocket.ABNF.OPCODE_CLOSE, None
        if not frame:
            raise websocket.WebSocketException("Not a valid frame %s" % frame)
        elif frame.opcode in OPCODE_DATA:
            return frame.opcode, frame.data
        elif frame.opcode == websocket.ABNF.OPCODE_CLOSE:
            ws.send_close()
            return frame.opcode, None
        elif frame.opcode == websocket.ABNF.OPCODE_PING:
            ws.pong(frame.data)
            return frame.opcode, frame.data

        return frame.opcode, frame.data

    def recv_ws():
        while True:
            opcode, data = recv()
            msg = None
            if six.PY3 and opcode == websocket.ABNF.OPCODE_TEXT and isinstance(data, bytes):
                data = str(data, "utf-8")
            if isinstance(data, bytes) and len(data)>2 and data[:2] == b'\037\213':  # gzip magick
                try:
                    data = "[gzip] " + str(gzip.decompress(data), "utf-8")
                except:
                    pass
            elif isinstance(data, bytes):
                try:
                    data = "[zlib] " + str(zlib.decompress(data, -zlib.MAX_WBITS), "utf-8")
                except:
                    pass

            if isinstance(data, bytes):
                data = repr(data)

            if args.verbose:
                msg = "%s: %s" % (websocket.ABNF.OPCODE_MAP.get(opcode), data)
            else:
                msg = data

            if msg is not None:
                if args.timings:
                    console.write(str(time.time() - start_time) + ": " + msg)
                else:
                    console.write(msg)

            if opcode == websocket.ABNF.OPCODE_CLOSE:
                break

    thread = threading.Thread(target=recv_ws)
    thread.daemon = True
    thread.start()

    if args.text:
        ws.send(args.text)

    while True:
        try:
            message = console.read()
            ws.send(message)
        except KeyboardInterrupt:
            return
        except EOFError:
            time.sleep(args.eof_wait)
            return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
EOF

# Test working of the help command
python wsdump.py -h

# Check for command error
if [ $? -ne 0 ]; then
  echo "Error: Failed to run wsdump.py. Please check the installation."
  exit 1
fi

# Print message
echo "websocket-client installation and setup successfully completed"
