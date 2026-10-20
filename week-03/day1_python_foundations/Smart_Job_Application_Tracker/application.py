from storage import save_application,load_application
from logger import logger
import datetime

applications = load_application()

def add_application():
   application_id = input("Enter application ID: ")
   company = input("Enter company name: ")
   job_title = input("Enter job title: ")
   application_date = input("Enter application date (YYYY-MM-DD): ")

   application = {
        "id": application_id,
        "company": company,
        "job_title": job_title,
        "status": "Applied",
        "application_date": application_date
    }
   applications.append(application)
   save_application(applications)
   print("Application added successfully!")

def view_application():
    if not applications:
        print("Application Not FOund")
        return
    for app in applications:
        print("\nApplication ID:", app["id"])
        print("Company:", app["company"])
        print("Job Title:", app["job_title"])
        print("Status:", app["status"])
        print("Date:", app["application_date"])

def delete_application():
    application_id = input("Enter application ID to delete: ")

    for application in applications:
        if application["id"] == application_id:
            applications.remove(application)
            save_application(applications)
            print("Application deleted successfully!")
            return

    print("Application ID not found.")



    

