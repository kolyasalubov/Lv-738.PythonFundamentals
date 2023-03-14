REQUEST_STATUS = "upsc ups@localhost"     # Command to request of status UPS
HOST = ["192.168.220.2", "192.168.220.1", "192.168.220.3"]      # Remote hosts list
SHUTDOWN = "shutdown -h now"        # Command to shutdown remote host
REQUEST_FILE = "/file.status"       # File name for test
STATUS_ONLINE = "ups.status: OL"     # Expected status
STATUS_ONBATTERY = "ups.status: OB"     # Expected status
TIME_POOLING = 5    # sec. Waiting interval in the status recheck loop. Total time = TIME_POOLING * TIME_POOLING_TIMES
TIME_POOLING_TIMES = 5
TIME_DELAY = 10     # sec. Interval in the main status check loop  
PING_TIMES = 5      # 
DISCORD_URL = "https://discordapp.com/api/webhooks"     # URL module for connect to Discord Bot
LOG_FILE = "/file.log"