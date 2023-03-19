import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import numpy as np
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud.bigquery.job import LoadJobConfig, WriteDisposition
import os

def remove_serious(element):
    post_split = element.split(" ")
    if post_split[0] == "[Serious]":
        new_post = " ".join(post_split[1:len(post_split)])
    else:
        new_post = element
    return new_post


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.reddit.com/r/AskReddit/new/")


subreddits = ["https://www.reddit.com/r/AskReddit/new/", "https://www.reddit.com/r/TooAfraidToAsk/new/","https://www.reddit.com/r/explainlikeimfive/new/"]

reddit_dict = {}

for link in subreddits:

    driver.get(link)

    subreddit = link.split("/")[4]

    post_title = driver.find_elements(By.XPATH, "//h3[@class = '_eYtD2XCVieq6emjKBH3m']")
    
    for count, item in enumerate(post_title):
        if count <= 8:
            if count == 1:
                continue
            else:
                if subreddit == "AskReddit":
                    new_post = "".join(map(remove_serious, item.text))
                    if subreddit not in reddit_dict:
                        reddit_dict[subreddit] = [new_post]
                    else:
                        reddit_dict[subreddit].append(new_post)
                elif subreddit == "explainlikeimfive":
                    new_post_split = item.text.split(" ")
                    new_post = " ".join(new_post_split[1:len(new_post_split)])
                    if subreddit not in reddit_dict:
                        reddit_dict[subreddit] = [new_post]
                    else:
                        reddit_dict[subreddit].append(new_post)
                else:
                    if subreddit not in reddit_dict:
                        reddit_dict[subreddit] = [item.text]
                    else:
                        reddit_dict[subreddit].append(item.text)


    time.sleep(3)


driver.close()

data = pd.DataFrame(reddit_dict)
data = data.melt(ignore_index=True, var_name = "subreddit", value_name = "post")
data["time"] = datetime.now()

key_path = "C:\\Users\\Ivan Shamoon\\Desktop\\Snek\\orders-371808-a85fe74cdb32.json"
# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
# to the path of the JSON key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path

# Create a BigQuery client object
client = bigquery.Client()

# Define the ID of the BigQuery table to query
table_id = 'orders-371808.new_reddit_post.ask_reddit'


tuple_list = data.to_dict(orient= "records")
table = client.get_table("{}.{}.{}".format("orders-371808","new_reddit_post","ask_reddit"))

from google.cloud.bigquery.job import LoadJobConfig, WriteDisposition

job_config = bigquery.LoadJobConfig()
job_config.write_disposition = WriteDisposition.WRITE_APPEND


client.load_table_from_dataframe(
    data, table, job_config=job_config
).result()
