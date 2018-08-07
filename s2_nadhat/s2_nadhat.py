#!/usr/bin/env python3

"""
s2_nadhat.py

 Copyright (c) 2016, 2017 Alan Yorinks All right reserved.

 Python Banyan is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""
import json
import sys
import time
import os
import pigpio
import psutil
from subprocess import call
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket


# This class inherits from WebSocket.
# It receives messages from the Scratch and reports back for any digital input
# changes.
class S2Nadhat(WebSocket):
   
    def handleMessage(self):
        # get command from Scratch2
        payload = json.loads(self.data)
        print(payload)
        client_cmd = payload['command']
        # When the user wishes to set a pin as a digital Input
        if client_cmd == 'send_sms':
            sms_text_out = payload['sms_text']
            phone_number_out = payload['phone_number']
            sms_mode = payload['normal']
            # code to write SMS there
            #
            #
            # end of code to write SMS there
        elif client_cmd == 'ready':
            pass
        else:
            print("Unknown command received", client_cmd)

    # call back from pigpio when a digital input value changed
    # send info back up to scratch
    def input_callback(self, pin, level, tick):
        payload = {'report': 'incoming_sms', 'from': , 'content': str(level)}
        print('callback', payload)
        msg = json.dumps(payload)
        self.sendMessage(msg)

    def handleConnected(self):
        self.pi = pigpio.pi()
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')


def run_server():
    # checking running processes.
    # if the backplane is already running, just note that and move on.
    # add gammu-smsd deamon check

    found_gammu-smsd = False

    # add gammu-smsd deamon check
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.name() == "gammu-smsd":
            found_ = True
            print("gammu-smsd is running")
        else:
            continue

    if not found_gammu-smsd:
        call(['sudo', 'systemctl start gammu-smsd.service'])
        print('gammu-smsd has been started')

    os.system('scratch2&')
    server = SimpleWebSocketServer('', 9000, S2Nadhat)
    server.serveforever()


if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        sys.exit(0)


