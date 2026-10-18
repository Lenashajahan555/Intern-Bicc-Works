import json
from dataclasses import dataclass,asdict

FILE="movie.json"

@dataclass
class Movie:
    title:str
    genre:str
    watched:bool=False
    rating:int=0


def load_movies()-> list[Movie]:
    try:
        with open(FILE,encoding="utf-8") as f:
            return[Movie(**item) for item in json.load(f)]
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        print("Warning ")
        return[]

def save_movies(movies: list[Movie])->None:
    with open(FILE,'w',encoding="utf-8") as f:
        json.dump([asdict(m) for m in movies],f,indent=4)

def ask_number(prompt:str, low:int, high:int)->int:
    while True:
        try:
            number=int(input("Enter a number"))  
            if low <= number <=high:
                return number
                
            print("type a number between {low} or {high}")
        except ValueError:
            print("please enter a valid number")
        

def add_movie(movies: list[Movie])-> None:
    title=input("Enter your movie title:").strip()
    if not title:
        print("Please type a valid title:")
        return
    genre=input("Enter genre of movie").strip()
    rating=ask_number("enter your movie rating",0 , 5)
    movies.append(Movie(title,genre,watched=False,rating=rating))
    save_movies(movies)
    print("----Movie Added-----")

def show_movies(movies:list[Movie])-> None:
    if not movies:
        print("Movie Not Found")
        return
    for number,m in enumerate(movies,start=1):
        mark="x" if m.watched else " "
        line=f"{number}.[{mark}] {m.title} ({m.genre})"
        if m.rating:
            line+=f"-{m.rating}/5"
        print(line)

def mark_watched(movies:list[Movie]) -> None:
    if not movies:
        print("Movie not watched")
        return
    show_movies(movies)
    movie=ask_number("enter yoour movie name:")
    if movies is None:
        return
    movies[movie - 1].watched=True
    save_movies(movies)
    print("-----movies read----")

def delete_movie(movies:list[Movie])-> None:
    if not movies:
        print("Movie not found ")
        return
    show_movies(movies)
    number=ask_number("enter a number",1,len(movies))
    if movies is None:
        return
    removed=movies.pop(number-1)
    save_movies(movies)
    print("---deleted-----")

def main():
    movies=load_movies()
    while True:
        print("\n 1.ADD \n 2.LIST \n 3.MARK WATCHED \n 4.DELETE \n5.QUIT")
        choice=input("ENTER YOUR CHOICE:")
        if choice=="1":
            add_movie(movies)
        elif choice=="2":
            show_movies(movies)
        elif choice=="3":
            mark_watched(movies)
        elif choice=="4":
            delete_movie(movies)
        elif choice=="5":
            print("HAVE A GREAT DAY!!")
            break
        else:
            print("Please choose a number 1 to 5")

if __name__ == "__main__":
    main()

    