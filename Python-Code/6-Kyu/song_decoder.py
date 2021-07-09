def song_decoder(song):
    listLyrics = song.split("WUB")
    ans = ""
    for i in listLyrics:
        if len(i) > 0:
            ans += i + " "
            
    return ans[:-1]



print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))