from gmusicapi.clients import Mobileclient

api = Mobileclient()
logged_in = api.login('<<email_address>>', '<<password>>', Mobileclient.FROM_MAC_ADDRESS)
print(logged_in)

playlists = api.get_all_playlists()
myplaylists = list(filter(lambda p: p['name'].find('My Library') == 0, playlists))
for playlist in myplaylists:
    api.delete_playlist(playlist['id'])
    print(playlist['name'])
