# Dubstep song titles often have WUB in their names
# this decodes the song title by removing any WUB in it

# eg: A song with words "I AM X" can transform into a dubstep remix as
# "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX"


def song_decoder(song):
    return " ".join(song.replace("WUB", " ").strip().split())


print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
