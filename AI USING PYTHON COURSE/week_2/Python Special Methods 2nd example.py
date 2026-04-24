from operator import add


class playlist:

    def __init__ (self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __add__ (self, other):
        return playlist ( self.songs + other.songs)
    
playlist1 = playlist(["song1", "song2", "song3"])
playlist2 = playlist(["song4", "song5"])
playlist3 = playlist(["song6"])

print(len(playlist1))  # Output: 3
print(len(playlist2))  # Output: 2
print(len(playlist3))  # Output: 1

print(add(playlist1, playlist2).songs)  # Output: ['song1', 'song2', 'song3', 'song4', 'song5']
print(len(add(playlist1, playlist2)))  # Output: 5