import os
from supabase import create_client, Client
import scrapetube

url: str = os.environ.get('URL')
key: str = os.environ.get('KEY')
supabase: Client = create_client(url, key)

videos = scrapetube.get_channel("UCtxD0x6AuNNqdXO9Wp5GHew",sort_by="oldest")

for video in videos:
    response = (
    supabase.table("ur_cristiano")
    .insert({"title": video['title']['runs'][0]['text'], "link": f'http://www.youtube.com/watch?v={video["videoId"]}'})
    .execute()
    )
    print(video['title']['runs'][0]['text'])

print(f"Done")
"""response = (
    supabase.table("test")
    .insert({})
    .execute())
print('Inserted succefully', )"""
