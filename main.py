import os
from supabase import create_client, Client
import scrapetube

url: str = os.environ.get('URL')
key: str = os.environ.get('KEY')
supabase: Client = create_client(url, key)

response = supabase.table('ur_cristiano').delete().neq("id", -1).execute()

videos = scrapetube.get_channel("UCtxD0x6AuNNqdXO9Wp5GHew",sort_by="oldest")

i = 1
for video in videos:
    #print(video['videoId'])
    response = (
    supabase.table("ur_cristiano")
    .insert({"id": i ,"title": video['title']['runs'][0]['text'], "link": f'http://www.youtube.com/watch?v={video["videoId"]}'})
    .execute()
    )
    i = i + 1

print(f"Done")


"""response = (
    supabase.table("test")
    .insert({})
    .execute())
print('Inserted succefully', )"""
