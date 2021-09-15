from object_oriented_programming import Song


new_song = Song("""
Жил-был у бабушки серенький козлик,
Жил-был у бабушки серенький козлик,
Вот как, вот как, серенький козлик,
Вот как, вот как, серенький козлик.

Бабушка козлика очень любила,
Бабушка козлика очень любила,
Вот как, вот как, очень любила,
Вот как, вот как, очень любила.

Вздумалось козлику в лес погуляти,
Вздумалось козлику в лес погуляти,
Вот как, вот как, в лес погуляти,
Вот как, вот как, в лес погуляти.

Напали на козлика серые волки,
Напали на козлика серые волки,
Вот как, вот, как серые волки,
Вот как, вот, как серые волки.

Остались от козлика рожки да ножки,
Остались от козлика рожки да ножки,
Вот как, вот как, рожки да ножки,
Вот как, вот как, рожки да ножки.
""")

print(new_song.text_length())
print(new_song.number_of_tokens())
print(new_song.number_of_sentences())
print(new_song.number_of_lemmatized_tokens())
print(new_song.number_of_lines())
