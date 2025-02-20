import os
from supabase import create_client, Client
import scrapetube

url: str = os.environ.get('URL')
key: str = os.environ.get('KEY')
supabase: Client = create_client(url, key)




response = (
    supabase.table("test")
    .insert({})
    .execute())
print('Inserted succefully', )
