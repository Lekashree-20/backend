#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install dropbox




from dropbox import DropboxOAuth2FlowNoRedirect

APP_KEY = '8w35z9rhhk91rls'
APP_SECRET = 'uirmsvy9tkg0886'

auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

authorize_url = auth_flow.start()
print("1. Go to: " + authorize_url)
print("2. Click 'Allow' (you might have to log in first)")
print("3. Copy the authorization code.")

auth_code = input("Enter the authorization code here: ")

access_token, user_id = auth_flow.finish(auth_code)

