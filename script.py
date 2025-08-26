import os
from supabase import create_client, Client

url: str = os.environ.get('URL')
key: str = os.environ.get('KEY')
