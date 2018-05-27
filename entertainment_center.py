import fresh_tomatoes
import media

#Movie instances that contains movie titles, box art, poster images,
#movie trailer URLs
coco = media.Movie("Coco",
                   "The story follows a 12-year-old boy named Miguel Rivera "
                   "who is accidentally transported to the land of the dead",
                   "https://vignette.wikia.nocookie.net/disney/images/1/14/Coco_poster.png/revision/latest?cb=20170912170727",
                   "https://www.youtube.com/watch?v=Rvr68u6k5sI")

up = media.Movie("Up",
                 "Seventy-eight year old Carl Fredricksen travels to Paradi"
                 "se Falls in his home equipped with balloons, inadvertently "
                 "taking a young stowaway.",
                 "https://img.hindilinks4u.to/2014/11/Up-2009-In-Hindi.jpg",
                 "https://www.youtube.com/watch?v=qas5lWp7_R0")

wall_e = media.Movie("WALL-E",
                   "In the distant future, a small waste-collecting robot"
                   " inadvertently embarks on a space journey that will "
                   "ultimately decide the fate of mankind.",
                   "https://pixar-planet.fr/wp-content/uploads/2010/04/affiche-walle-40.jpg",
                   "https://www.youtube.com/watch?v=qGBZWbg_26A")

big_hero6 = media.Movie("Big Hero 6",
                   "The special bond that develops between plus-sized "
                   "inflatable robot Baymax, and prodigy Hiro Hamada, who t"
                   "eam up with a group of friends to form a band of "
                   "high-tech heroes.",
                   "https://images-na.ssl-images-amazon.com/images/I/81%2BMTze25KL._SL1500_.jpg",
                   "https://www.youtube.com/watch?v=z3biFxZIJOQ")

dragon = media.Movie("How to Train Your Dragon",
                   "The story takes place in a mythical Viking world where a y"
                   "oung Viking teenager named Hiccup aspires to follow his tr"
                   "ibe's tradition of becoming a dragon slayer",
                   "http://cdn.collider.com/wp-content/uploads/how-to-train-your-dragon-2-poster2.jpg",
                   "https://youtu.be/oKiYuIsPxYk?t=6s")

ferdinand = media.Movie("Ferdinand",
                   "Ferdinand is a young bull who escapes from a training cam"
                   "p in rural Spain after his father never returns from a sh"
                   "owdown with a matador. Adopted by a girl who lives on a fa"
                   "rm,",
                   "https://i.pinimg.com/originals/74/54/57/745457295a72883a4d3fc516adbc03e2.jpg",
                   "https://youtu.be/YLn1_S3JJfg")

brave = media.Movie("Brave",
                   "In Medieval Scotland, Princess Merida of the clan Dunbro"
                   "ch, is given a bow and arrow by her father, King Fergus, "
                   "for her 6th birthday. Her mother, Queen Elinor, disagrees"
                   " with the present",
                   "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-7119-1mm8kcq_30f3d3a4.jpeg?region=0,0,1000,1409",
                   "https://youtu.be/TEHWDA_6e3M?t=7s")

monsters = media.Movie("Monsters",
                   "In order to power the city, monsters have to scare child"
                   "ren so that they scream",
                   "https://vignette.wikia.nocookie.net/disney/images/f/fe/1000px-Monsters_inc_ver1_xlg.jpeg/revision/latest?cb=20160202161958",
                   "https://www.youtube.com/watch?v=QxrQ6BaijAY")

inside_out = media.Movie("Inside Out",
                   "After young Riley is uprooted from her Midwest life and "
                   "moved to San Francisco, her emotions - Joy, Fear, Anger,"
                   " Disgust and Sadness - conflict on how best to navigate "
                   "a new city, house, and school.",
                   "https://vignette.wikia.nocookie.net/disney/images/f/fb/Inside-Out-60.png/revision/latest?cb=20150304211113",
                   "https://www.youtube.com/watch?v=QxrQ6BaijAY")
# Movie variable contains all movies
movies = [coco, up, wall_e, big_hero6, dragon, ferdinand, brave, monsters,
inside_out]

# fresh_tomatoes generates HTML file with a Movie trailers
# and opens up on browser
fresh_tomatoes.open_movies_page(movies)
