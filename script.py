import os
from supabase import create_client, Client

url: str = os.environ.get('URL2')
key: str = os.environ.get('KEY2')

supabase: Client = create_client(url, key)
response = supabase.table("table").insert({}).execute()
