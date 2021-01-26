import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()
album_repository.delete_all()

artist_1 = Artist("Beyonce")
artist_repository.save(artist_1)

album_1 = Album("Dangerously in Love", artist_1, "Pop")
album_repository.save(album_1)

artist_repository.select_all()
album_repository.select_all()

pdb.set_trace()
