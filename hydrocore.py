class Store_holder():
    
    def __init__(self):
        self.main_holder = []

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

    def __init__(self, title, rating, status, notes):
        self.title = title
        self.rating = rating
        self.status = status
        self.notes = notes


class Book(Media):
    pass

    
class Anime(Media):
    pass

    
class Game(Media):
    pass
