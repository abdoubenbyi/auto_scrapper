import os
from supabase import create_client, Client
import scrapetube

url: str = os.environ.get('URL')
key: str = os.environ.get('KEY')
db1: str = os.environ.get('db1')
db2: str = os.environ.get('db2')
supabase: Client = create_client(url, key)

projects = {  "ur_cristiano": "UCtxD0x6AuNNqdXO9Wp5GHew",
  "aboflah": "UCqq5n-Oe-r1EEHI3yvhVJcA"}

for project in projects.keys():
    response = supabase.table(project).delete().neq("id", -1).execute()
    videos = scrapetube.get_channel(projects[project],sort_by="newest")
    i = 1
    for video in videos:
        #print(video['videoId'])
        response = (
        supabase.table(project)
        .insert({"id": i ,"title": video['title']['runs'][0]['text'], "link": f'http://www.youtube.com/watch?v={video["videoId"]}'})
        .execute()
        )
        i = i + 1
print(f"Done")
