# JOB APLLICATION TRACKER

applications = {}


while True:
    print("\n========== Job Application Tracker ============")
    print("1. Add Application")
    print("2.Display All Applications")
    print("3.Search Application")
    print("4. Update Application")
    print("5. Delete Application")
    print("6. Tracker / Update Status")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1: 
                    print("--------- ADD APPLICATION --------")

                    application_ID = int(input("Enter Apllication ID: "))

                    if application_ID in applications:
                            print("Application ID already exist.")
                    else:
                        company = input("Enter Company Name: ")
                        role = input("Enter job role: ")
                        location = input("Enter Job Location: ")

                        applications[application_ID]={
                                "application_ID": application_ID,
                                "company": company,
                                "role": role,
                                "location": location,
                                "status": "Applied"
                        }

                        print("Application submitted successfully")
# ------------------------------------------------------------------------------------------
               
        case 2: 
                    print("--------- DISPLAY APPLICATION --------")

                    if len(applications) == 0:
                            print("NO Application Found.")
                    else:
                        for application_ID, details in applications.items():
                            print("Application Id :: ", application_ID)
                        print("Company        :: ", details["company"])
                        print("Role           :: ", details["role"])
                        print("Location       :: ", details["location"])
                        print("Status         :: ", details["status"])
                        print("=" * 30)
# ---------------------------------------------------------------------------------------
        case 3: 
                    print("--------- SEARCH APPLICATION --------")

                    application_ID = int(input("Enter Application ID to Search: "))

                    if application_ID in applications:
                        print("Application Found")
                        print("Application Id :: ", application_ID)
                        print("Company        :: ", applications[application_ID]["company"])
                        print("Role           :: ", applications[application_ID]["role"])
                        print("Location       :: ", applications[application_ID]["location"])
                        print("Status         :: ", applications[application_ID]["status"])
                        print("=" * 30)
                    else:
                        print("Application not found")
#  -------------------------------------------------------------------------------------
        case 4: 
                    print("--------- UPDATE APPLICATION --------")

                    
                    if application_ID in applications:
                        company = input("Enter updated company name :: ")
                        role = input("Enter updated job role :: ")
                        location = input("Enter updated job location :: ")

                        applications[application_ID]["company"] = company
                        applications[application_ID]["role"] = role
                        applications[application_ID]["location"] = location

                        print("Application updated successfully")
                        print("Application Id :: ", application_ID)
                        print("Company        :: ", applications[application_ID]["company"])
                        print("Role           :: ", applications[application_ID]["role"])
                        print("Location       :: ", applications[application_ID]["location"])
                        print("Status         :: ", applications[application_ID]["status"])
                    else:
                        print("Application not found")
# -------------------------------------------------------------------------------------------------
        case 5: 
                    print("--------- DELETE APPLICATION --------")

                    application_ID = int(input("Enter application ID for DELETION: "))

                    if application_ID in applications:
                           del applications[application_ID]
                           print("Application Deleted Sucessfully")
                    else:
                        print("Application not found")
        case 6: 
                    print("--------- TRACK APPLICATION --------")

                    application_ID = int(input("Enter application ID for updation: "))

                    if application_ID in applications:
                       if application_ID in applications:
                        print("Current Status :: ", applications[application_ID]["status"])

                        print("1. Applied")
                        print("2. Shortlisted")
                        print("3. Rejected")
                        print("4. Selected")

                        statusChoice = int(input("Choose new status (1-4) :: "))

                        if statusChoice == 1:
                            applications[application_ID]["status"] = "Applied"
                            print("Status updated to Applied")
                        elif statusChoice == 2:
                            applications[application_ID]["status"] = "Shortlisted"
                            print("Status updated to Shortlisted")
                        elif statusChoice == 3:
                            applications[application_ID]["status"] = "Rejected"
                            print("Status updated to Rejected")
                        elif statusChoice == 4:
                            applications[application_ID]["status"] = "Selected"
                            print("Status updated to Selected")
                        else:
                            print("Invalid status choice")
                    else:
                        print("Application not found")    

        case 7:
            print("Thank you for using the Job Tracker. Good luck!")
            break
        case _:
            print("Invalid choice, try again.")
        


