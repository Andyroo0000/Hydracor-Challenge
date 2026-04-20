class Store_holder():
    
    def __init__(self):
        self.main_holder = []
        self.instant_of_media = {}


    # def sort_by_attribute(self, attr):
    #     func_map = {
    #         "book": Media.is_type_book,
    #         "anime": Media.is_type_anime,
    #         "rating": Media.
            
    #     }

    #     return self.instance_of_media.sort(lambda x: func_map[attr])
    

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

    def __init__(self, title, rating, status):
        self.title = title
        self.rating = rating
        self.status = status

    def is_type_movie():
        return False
    
    def is_type_anime():
        return False

    def is_type_book():
        return False
    
    def is_type_game():
        return False

class Book(Media):

    def __init__(self):
        super.__init__("example")

    def is_type_book():
        return True
    
class Anime(Media):

    def __init__(self):
        super.__init__("example")

    def is_type_anime():
        return True
    
class Game(Media):

    def is_type_game():
        return True