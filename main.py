import os
from supabase import create_client, Client

url: str = os.environ.get('URL')
key: str = os.environ.get('KEY')
supabase: Client = create_client(url, keyKEY)
response = (
    supabase.table("test")
    .insert({})
    .execute())
