# import os
import time
# import requests
# import datetime 
# import subprocess
from modules.discord import *
from modules.message import *
from modules.logger import *
from modules.status import *
from modules.validate import *
from configuration.config import *
from configuration.credentials import *

notification_label = 0

constant_validation()

while True:
    status = get_file_status(REQUEST_FILE)
    # status = get_service_status(REQUEST_STATUS)

    # # Actions in ONLINE status
    if STATUS_ONBATTERY not in status:
        if notification_label != 1:
            message = make_message("UPS STATUS - ON LINE")
            discord_notify(message)
            log_nonify(message)
            # print for test
            print(message)
            notification_label = 1
        time.sleep(TIME_DELAY)
        continue

    # # Actions in ONBATTERY status
    else:
        # Status Change Notification to ONBATTERY
        if notification_label != 2:
            message = make_message("UPS STATUS - ON BATTERY")
            discord_notify(message)
            log_nonify(message)
            # for test
            print(message)
            notification_label = 2
        
        # # ONBATTERY status recheck cycle
        # # Recheck lasts TIME_POOLING_TIMES * TIME_POOLING
        # # When the status changes from ONBATTERY to ONLINE, the loop is interrupted and the main loop starts.
        for i in range(0, TIME_POOLING_TIMES):
            status = get_file_status(REQUEST_FILE)
            # status = get_service_status(REQUEST_STATUS)
            if i < (TIME_POOLING_TIMES -1) and STATUS_ONBATTERY in status:
                time.sleep(TIME_POOLING)
                # print for test
                print(f"{i}")
            elif STATUS_ONBATTERY not in status:
                break

            # # If the status remains ONBATTERY, actions with remote hosts begin
            else:
                # # The loop iterates through the list of HOST values and performs the given actions
                # # Connect to remote host via ssh and execute shutdown command
                for i in HOST:
                    if notification_label != 3:
                        message = make_message(f"Start shutting down remote host {i}")
                        discord_notify(message)
                        log_nonify(message)
                        # print for test
                        print(message)
                        # shutdown(i)
                notification_label = 3

                # # Loop checking the status of remote hosts using ping
                # # The loop is limited by the size of the list, or the number of PING_TIMES retries
                hosts = HOST.copy()
                count = 0

                while len(hosts) > 0:
                    for i in hosts:
                        # print for test
                        print(f"Remaining hosts: {hosts}")
                        ping = get_ping(i)
                        if "bytes from" not in ping:
                            hosts.remove(i)
                            message = make_message(f"Remote host {i} was shutted down")
                            discord_notify(message)
                            log_nonify(message)
                            # print for test
                            print(message)
                    if count == PING_TIMES:
                        message = make_message(f"Attention! Remote host {i} was NOT shutted down")
                        discord_notify(message)
                        log_nonify(message)
                        # print for test
                        print(message)
                        break
                    count += 1
                    time.sleep(TIME_POOLING)  
                
                # # Waiting loop for status change to ONLINE
                while STATUS_ONLINE not in status:
                    status = get_file_status(REQUEST_FILE)
                    # status = get_service_status(REQUEST_STATUS)
                    if notification_label != 4:
                        message = make_message("Waiting UPS status - ON LINE")
                        discord_notify(message)
                        log_nonify(message)
                        # print for test
                        print(message)
                    notification_label = 4
                    time.sleep(TIME_DELAY)
                else:
                    break
                
                # WOL and check status block 

