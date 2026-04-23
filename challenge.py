import json
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
            
    #     ]

    #     return self.instance_of_media.sort(lambda x: func_map[attr])

    
    def main(self):
        self.load()
        while True:
            # print(self.main_holder)
            print("\n--- Media Tracker ---")
            print("1. Add media")
            print("2. View all")
            print("3. Sort/Filter")
            print("4. Remove")
            print("5. Quit")
            
            choice = int(input("Enter choice: "))

            options = {
                1: self.user_add,
                2: self.display_all,
                3: self.sort_by_attribute,
                4: self.remove,
                5: None,
            }

            if choice == 5:
                break
            elif choice in options:
                options[choice]()
            else:
                print("Invalid input")
            self.save()

    def user_add(self):
        media_type = str(input("Do you want to enter a book, game, movie, or anime? ")).lower()
        media_name = str(input("What is the name? ")).lower()
        media_rating = int(input("What would you rate it out of 10? "))
        media_status = int(input("What is your completion status?(Enter a percentage) "))
        media_notes = str(input("Any other notes or comments about it? ")).lower()

        type_map = {
            "game": Game(media_name, media_rating, media_status, media_notes, media_type),
            "anime": Anime(media_name, media_rating, media_status, media_notes, media_type),
            "book": Book(media_name, media_rating, media_status, media_notes, media_type),
            "movie": Movie(media_name, media_rating, media_status, media_notes, media_type),
        }

        user_media_input = type_map[media_type]
        self.main_holder.append(user_media_input)

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

    def sort_by_attribute(self):
        
        print("\n--- Sort or Filter By ---")
        print("1. Game")
        print("2. Anime")
        print("3. Book")
        print("4. Movie")
        print("5. Rating")
        print("6. Alphabetical")
        print("7. Status")
        
        choice = int(input("Enter your choice: "))

        type_map = {
            1: (Game, "type"),
            2: (Anime, "type"),
            3: (Book, "type"),
            4: (Movie, "type"),
            5: ("rating", "attr"),
            6: ("title", "attr"),
            7: ("status", "attr"),

        }

        value_category, category = type_map[choice]

        if category == "type":
            sorted_list = ([x for x in self.main_holder if isinstance(x, value_category)])
            for content in (sorted_list):
                print(content.display())
        else:
            if value_category == "rating" or value_category == "status":
                sorted_list = (sorted(self.main_holder, key=lambda x: getattr(x, value_category), reverse=True))
                self.main_holder = sorted_list
            else:
                sorted_list = (sorted(self.main_holder, key=lambda x: getattr(x, value_category)))
                self.main_holder = sorted_list
        
    def remove(self):
        
        choice = str(input("Which media do you want to remove? ")).lower()

        for i in self.main_holder:
            if i.title == choice:
                self.main_holder.remove(i)
                print(f"Removed {i.title}. ")
                break


    def save(self):
        user_data = []
        
        for i in self.main_holder:
            user_data.append(vars(i))

        with open("media.json", "w") as f:
            json.dump(user_data, f)
    
    def load(self):
        
        type_chart = {
            "book": Book,
            "anime": Anime,
            "game": Game,
        }
        try:
            with open("media.json", "r") as f:
                user_data = json.load(f)
                for item in user_data:
                    self.main_holder.append(type_chart[item["type"]](item["title"], item["rating"], item["status"], item["notes"], item["type"]))
        except:
            pass

                



class Media():

    def __init__(self, title, rating, status, notes, type):
        self.title = title
        self.rating = rating
        self.status = status
        self.notes = notes
        self.type = type

    def display(self):
        return (f"Type: {self.type} | Title: {self.title} | Rating: {self.rating} | Status: {self.status}% | Notes: {self.notes} ")


class Book(Media):
    pass

    
class Anime(Media):
    pass

    
class Game(Media):
    pass

class Movie(Media):
    pass




start = Store_holder()

start.main()

