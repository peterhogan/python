class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
"Happy birthday to you",
"Happy birthday, happy birthday",
"Happy birthday to you."])

bulls_on_parade = Song(["They rally round the family",
"With pockets full of shells"])

lyrics = "Hello, is it me you're looking for?"
lyrics_to_go = Song([lyrics])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

lyrics_to_go.sing_me_a_song()
