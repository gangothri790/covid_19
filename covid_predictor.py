class Invalid_input_error(Exception):
    """used when user enters an invalid input."""

    pass




def predict_covid():

    print("This tool will help you assess your symptoms and determine if you are a good candidate for covid-19.\n"
          "It also offers you guidance on when to seek medical care.")
    print("This tool is not meant to the original covid-19 test or diagnosis.\n"
          "The information about the pandemic is also changing day-by-day.\n"
          "So if you have any doubt or in case of any medical emergency,its advisable to consult a doctor.\n")
    list_yes = ["Yes", "yes", "Y", "y", "YES"]
    list_no = ["No", "no", "n", "N", "NO"]
    while True:
        try:
            symptom_1=input("Have you met or been in contact with the person\n"
                    "who has been infected by covid-19?Yes/No\n")
            if(symptom_1 not in list_yes and symptom_1 not in list_no):
                 raise Invalid_input_error


            symptom_2=input("Have you travelled to foreign countries \n"
                    "or any other far places after covid-19 discovery?Yes/No\n")
            if (symptom_2 not in list_yes and symptom_2 not in list_no):
                raise Invalid_input_error

            symptom_3=input("Have you met with fever/cough/cold in last few days?Yes/No\n")
            if (symptom_3 not in list_yes and symptom_3 not in list_no):
                 raise Invalid_input_error

            symptom_4=input("Do you have trouble in breathing?Yes/No\n")
            if (symptom_4 not in list_yes and symptom_4 not in list_no):
                 raise Invalid_input_error

            symptom_5=input("Do you have sore throat?Yes/No\n")
            if (symptom_3 not in list_yes and symptom_3 not in list_no):
                 raise Invalid_input_error
            symptom_6=input("Are you facing loss of smell/taste?Yes/No\n")
            if (symptom_3 not in list_yes and symptom_3 not in list_no):
                 raise Invalid_input_error
            symptom_7=input("Are you having diarrhea or vomitings or head ache regularly?Yes/No\n")
            if (symptom_3 not in list_yes and symptom_3 not in list_no):
                 raise Invalid_input_error

            symptom_8=input("Do you have any body pains/muscle achesYes/No\n")
            if (symptom_3 not in list_yes and symptom_3 not in list_no):
                 raise Invalid_input_error


            if symptom_1 in list_yes:
                 print("Immediately go for a lab test and get into quarantine for 14 days\n"
                 "After 14 days again make sure you get a covid-19 test.\n"
                 "Covid-19 is a highly infectious diesease and it may be infected due to\n"
                 "contact with the infected person.")

            elif symptom_2 in list_yes:
                 print("Immediately go for a lab test and get into quarantine for 14 days\n"
                 "After 14 days again make sure you get a covid-19 test.\n"
                 "Because of high and fast spread,covid-19 may be in the places you travelled")


            elif symptom_3 in list_yes:
                print("You have common covid-19 symptoms.Immediately consult a doctor.")


            elif symptom_4 in list_yes:
                print("Diffifculty in breathing is a very serious symptom for covid-19\n"
                    "Immediately consult a doctor.")



            elif (symptom_5 in list_yes) or (symptom_6 in list_yes) or (symptom_7 in list_yes) or (symptom_8 in list_yes):
                print("You have mild covid-19 symptoms.Stay in quarantine for a few days\n"
                      "If you feel same after that .Better to go for a laboratory test.")
            else:
                print("You are in a safe zone.If your area is\n"
                      "containment zone stay home.\n"
                      "Wear mask and sanititize every 2 hours. \n"
                      "Also remember that covid-19 can be caused\n"
                      "even without symptoms.So it's better to have remedies\n"
                      "and maintain social distance.")
            break
        except Invalid_input_error:
            print("entered an invalid input.Try again!")


predict_covid()
