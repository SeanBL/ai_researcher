import os
import requests
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager, config_list_from_dotenv
from dotenv import load_dotenv


load_dotenv()

config_list = config_list_from_dotenv(
    dotenv_file_path='.env', # If None the function will try to find in the working directory
    filter_dict={
        "model": {
            "gpt-3.5-turbo",
        }
    }
)

print(config_list)