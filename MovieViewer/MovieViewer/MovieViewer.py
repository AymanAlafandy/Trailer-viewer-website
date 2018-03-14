from Media import Media
import FreshTomato

batmanVsSuperman = Media("BATMAN VS SUPERMAN", "BATMAN Fights with SUPERMAN", "http://i1.wp.com/bitcast-a-sm.bitgravity.com/slashfilm/wp/wp-content/images/batman-vs-superman-ew-pics-3-HR.jpg", "https://youtu.be/rYi5OPAoceA")

oggy = Media("Oggy and the cockroaches" , "Cats fights with cockroaches" , "http://3.bp.blogspot.com/-hbvMX2E-Eao/Uhmv_XIIh0I/AAAAAAAABho/FhcASFcTF_Y/s400/Oggy+and+the+Cockroaches,+film+team.jpg" , "https://www.youtube.com/watch?v=POvSDfEyxok")
#oggy.showTrailer()
movies = [oggy , batmanVsSuperman]
FreshTomato.open_movies_page(movies)