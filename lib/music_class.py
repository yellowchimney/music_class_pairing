class MusicListening:
    def __init__(self, starting_list):
        self.storage = starting_list

    def add_tracks(self, track):
        if isinstance(track, str):
            self.storage.append(track)
        else:
            raise Exception("Track name must be a string")

    def list_all(self):
        return self.storage