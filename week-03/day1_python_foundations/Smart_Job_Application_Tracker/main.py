import logger
from storage import load_application
from application import(add_application,view_application,
                        delete_application
                        )
from api import get_api_app
def main():
    application=load_application()
    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add student")
        print("2. View students")
        print("3. Delete student")
        print("4. Get API data")
        print("5. Exit")

        choice = input("Enter your choice: ")
        try:
            if choice=="1":
                add_application()

            elif choice=="2":
                view_application()
                
            elif choice=="3":
                delete_application()
            elif choice=="4":
                get_api_app()
                
            elif choice=="5":
                print("SEE YOU NEXT TIME!!1")
                return
            
            else:
                print("Invalid choices")
        except ValueError:
            logger.warning("Something went wrong %s")

if __name__=="__main__":
    main()

