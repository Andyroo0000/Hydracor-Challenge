class Store_holder():
    
    def __init__(self):
        self.main_holder = []
        self.book_holder = []
        self.anime_holder = []
        self.game_holder = []

    # def sort_by_attribute(self, attr):
    #     func_map = {
    #         "book": Media.is_type_book,
    #         "anime": Media.is_type_anime,
    #         "rating": Media.
            
    #     }

    #     return self.instance_of_media.sort(lambda x: func_map[attr])
    def user_add(self):
        media_type = str(input("Do you want to enter a book, game, or anime? ")).lower()
        media_name = str(input("What is the name? ")).lower()
        media_rating = str(input("What would you rate it out of 10? ")).lower()
        media_status = str(input("What is your completion status? ")).lower()
        media_notes = str(input("Any other notes or comments about it? ")).lower()

        type_map = {
            "game": Game(media_name, media_rating, media_status, media_notes, media_type),
            "anime": Anime(media_name, media_rating, media_status, media_notes, media_type),
            "book": Book(media_name, media_rating, media_status, media_notes, media_type),
        }

        user_media_input = type_map[media_type]
        self.main_holder.append(user_media_input)

        self.display_all()

        # if media_type == "book":
        #     user_media_input = Book(media_name, media_rating, media_status, media_notes)
        #     self.book_holder.append(user_media_input)

        # elif media_type == "anime":
        #     user_media_input = Anime(media_name, media_rating, media_status, media_notes)
        #     self.anime_holder.append(user_media_input)

        # elif media_type == "game":
        #     user_media_input = Game(media_name, media_rating, media_status, media_notes)
        #     self.book_holder.append(user_media_input)
        
    def display_all(self):
        for content in (self.main_holder):
            print(content.display())


    def sort_by_attribute(self, attr):
        
        type_map = {
            "game": Game,
            "anime": Anime,
            "book": Book,
        }

        if attr in type_map():
            return [x for x in self.main_holder if isinstance(x, type_map[attr])]
        else:
            return sorted(self.main_holder, key=lambda x: getattr(x, attr))

        

class Media():

    def __init__(self, title, rating, status, notes, type):
        self.title = title
        self.rating = rating
        self.status = status
        self.notes = notes
        self.type = type

    def display(self):
        print(f"Type: {self.type} | Title: {self.title} | Rating: {self.rating} | Status: {self.status} | Notes: {self.notes} ")


class Book(Media):
    pass

    
class Anime(Media):
    pass

    
class Game(Media):
    pass


start = Store_holder()

start.user_add()