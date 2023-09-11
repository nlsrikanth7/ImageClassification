import os
import sys
import logging

#Create a custom logging str
# save the asc time 
# log level name 
# log the module like setup.py or index.html etc we are running the code
# log the message of the activity
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"



log_dir = "logs" #Create a directory 
log_filepath = os.path.join(log_dir, "running_logs.log") # creating a file within the directory
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # printing the log in the log file 
        logging.StreamHandler(sys.stdout) # printing the log in the terminal 
    ]
)

logger = logging.getLogger("cnnClassifierLogger") # Naming the log
