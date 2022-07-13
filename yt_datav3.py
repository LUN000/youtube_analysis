from googleapiclient.discovery import build
import requests
import  json
import pandas as pd

# key = "AIzaSyD1a8V33_RIiEy71_lwTuta6CvWG4_u_iA"
# channel_id = "UCjv4bfP_67WLuPheS-Z8Ekg"


# youtube = build('youtube', 'v3', developerKey=key)

# request = youtube.channels().list(part="snippet,contentDetails,statistics", id=channel_id)
# response = request.execute()

# print(response)
# with open("text.json", "w") as file:
#     json.dump(response, file)
# file.close()

with open("text.json","r") as file:
    df = json.load(file)
file.close()
print(df)
df = pd.DataFrame(df)
df