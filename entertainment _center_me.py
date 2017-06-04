import fresh_tomatoes
import media
three_Idiots = media.Movie("3 Idiots",
            "Highest-grossing Bollywood film of all time in overseas markets",
            "https://en.wikipedia.org/wiki/File:3_idiots_poster.jpg",
            "https://www.youtube.com/watch?v=xvszmNXdM4w")

#print(three_Idiots.storyline)
#three_Idiots.show_trailer()
Baahubali_two = media.Movie("Baahubali 2: The Conclusion","English: The One with Strong Arms: The Conclusion",
	    "https://en.wikipedia.org/wiki/File:Baahubali_the_Conclusion.jpg",
	    "https://www.youtube.com/watch?v=qD-6d8Wo3do")
PK = media.Movie("PK","Indian satirical science fiction comedy film",
	    "https://en.wikipedia.org/wiki/File:PK_poster.jpg",
	    "https://www.youtube.com/watch?v=SOXWc32k4zA")
My_Name_Is_Khan = media.Movie("My Name Is Khan","My Name Is Khan and I'm not a terrorist ;)",
	    "https://en.wikipedia.org/wiki/File:My_Name_Is_Khan_film_poster.jpg",
	    "https://www.youtube.com/watch?v=_uNDm6YfN2k")
Airlift = media.Movie("Airlift","The world's largest air evacuation mission ever",
            "https://en.wikipedia.org/wiki/File:Airlift_poster.jpg",
            "https://www.youtube.com/watch?v=vb5xCMbMfZ0")
Wonder_Woman = media.Movie("Wonder Woman","It begins with her",
	    "https://en.wikipedia.org/wiki/File:Wonder_Woman_(2017_film).jpg",
	    "https://www.youtube.com/watch?v=1Q8fG0TtVAY")

movies = [three_Idiots, Baahubali_two, PK, My_Name_Is_Khan, Airlift, Wonder_Woman]
fresh_tomatoes.open_movies_page(movies)
