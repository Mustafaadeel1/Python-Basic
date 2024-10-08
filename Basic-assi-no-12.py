# user_start = input("'Assalamu Alaikum' You can start new Journey after your Death. To Run Journey, say 'start': ")  

# if user_start == "start":
#     print("Feel you are in Grave...")
#     print("Munker and Nakir have come to question you...")
    
#     question = input("Who is Your God? ").lower().strip()#Remove any spaces
    
#     if question == "Allah":
#         print("Well done 'Mashallah'")
#         question2 : str = input("Who is your Prophet ?").lower().strip()
#         question2 =="Muhmmad"
#         print("Mashallah Well done..")
#         question3 : str = input("What is your Religion ?")
#         question3 == "Islam"
#         print("Mashallah 'Welcome to 'Jannah'")
#         print("'Assalamu Alaikum'")
#         question3 == "end"
#         break
#     else:   
#         print("You are Fail. Now you are going to hell.")
# else:
#     print("Its your choice---If you start Its your own choice you say 'No' Its you choice")

        
def start_journey():
    user_start = input("'Assalamu Alaikum' You can start a new Journey after your Death. To Run Journey, say 'start': ").lower().strip()

    if user_start == "start":
        print("Feel you are in the Grave...")
        print("Munker and Nakir have come to question you...")

        question = input("Who is Your God? ").lower().strip()
        if question == "allah":
            print("Well done 'Mashallah'")

            question2 = input("Who is your Prophet? ").lower().strip()
            if question2 == "muhammad":
                print("Mashallah, Well done...")

                question3 = input("What is your Religion? ").lower().strip()
                if question3 == "islam":
                    print("Mashallah, Welcome to Jannah!")
                    print("'Assalamu Alaikum'")
                    
                    end_journey = input("To end the journey, type 'end': ").lower().strip()
                    if end_journey == "end":
                        print("Journey ended.")
                    else:
                        print("Continuing journey...")  # You can handle other cases if needed
                else:
                    print("Incorrect answer for Religion. You have failed.")
            else:
                print("Incorrect answer for Prophet. You have failed.")
        else:
            print("You have failed. Now you are going to hell.")
    else:
        print("It's your choice. If you start, it's your own decision. If you say 'no', that's your choice.")


# Call the function to start the journey
start_journey()
