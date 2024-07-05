def welcome_rules():
    print("\t\t\t\"WELCOME TO THE QUIZ GAME\" ")
    print("\tIMPORTANT RULES TO KEEP IN MIND DURING PLAYING ")
    print("1.There will be 5 mcq's for each topic")
    print("2.There will be 4 options for each question")
    print("3.Each mcq carry one mark")
    print("4.For answering a question you just have to insert option number \n")

def topic_name(): 
    global a
    print("\"We have 3 options of topics\"")   
    print("1.CRICKET")
    print("2.POLITICS")
    print("3.PAKISTAN")
    print("Q1-->On which topic you want to play?")
    a = int(input("ANS: "))
    if a == 1:
        print("You have choosen Cricket as your topic")
    elif a==2:
        print("You have choosen Politics as your topic")
    else:
        print("You have choosen Pakistan as your topic")
                      
def Cricket():
    corrected = 0
    print("MCQ-1 :: Which bowler has taken the most wickets in Test cricket?")
    print("1.Shane Warne")
    print("2.Muttiah Muralitharan")    
    print("3.Anil Kumble") 
    print("4.Breet Lee") 
    answer_1 = int((input("Answer is: " )))
    try:
        if answer_1 == 2:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
        elif answer_1 == 1 or answer_1 == 3 or answer_1 == 4 :
            print("YOU GOT WRONG ANSWER, CORRECT IS \"Muttiah Muralitharan\" ") 
        else :
            print("Error")         
    finally:
        print("MCQ-2 :: Who is the only cricketer to have scored 100 international centuries?")
        print("1.Ricky Ponting")
        print("2.Kumar Sangakkara")    
        print("3.Jacques Kallas") 
        print("4.Sachin Tendulkar") 
        answer_2 = int((input("Answer is: " )))
    try:
        if answer_2 == 4:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
        elif answer_2 == 1 or answer_2 == 2 or answer_2 == 3 :
            print("YOU GOT WRONG ANSWER, CORRECT IS \"Sachin Tendulkar\"") 
        else :
            print("Error")        
    finally: 
        print("MCQ-3 :: Which country won the first ICC Cricket World Cup in 1975?")
        print("1.Australia")
        print("2.England")    
        print("3.India") 
        print("4.Srilanka") 
        answer_3 = int((input("Answer is: " )))       
    try:
        if answer_3 == 3:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
        elif answer_3 == 1 or answer_3 == 2 or answer_3 == 4 :
            print("YOU GOT WRONG ANSWER, CORRECT IS \"India\"") 
        else :
            print("Error")    
    finally: 
        print("MCQ-4 :: Who holds the record for the fastest century in ODIs?")
        print("1.Shahid Afridi")
        print("2.AB de Villiers ")    
        print("3.Corey Anderson") 
        print("4.Chris Gayle") 
        answer_4 = int((input("Answer is: " )))       
    try:
        if answer_4 == 2:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
        elif answer_4 == 1 or answer_4 == 3 or answer_4 == 4 :
            print("YOU GOT WRONG ANSWER, CORRECT IS \"AB de Villiers\"") 
        else :
            print("Error")    
    finally: 
        print("MCQ-5 :: Which cricketer has taken the most wickets in a single ODI match?")
        print("1.Anil Kumble")
        print("2.Breet Lee")    
        print("3.Wasim Akram") 
        print("4.Chaminda Vaas") 
        answer_5 = int((input("Answer is: " )))     
    if answer_5 == 4:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
    elif answer_5 == 1 or answer_5 == 2 or answer_5 == 3 :
            print("YOU GOT WRONG ANSWER,CORRECT IS \"Chaminda Vass\"") 
    else :
            print("Error")        
    print("FROM 5 MCQ'S YOU GOT "+ str(corrected) + " CORRECTED")    
    
def Politics():
    corrected = 0
    print("MCQ-1 :: Who was the first female Prime Minister of the United Kingdom?")
    print("1.Theresa May")
    print("2.Margaret Thatcher")    
    print("3.Angela Merkel") 
    print("4.Benazir Bhutto") 
    answer_1 = int((input("Answer is: " )))
    try:
        if answer_1 == 2:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
        elif answer_1 == 1 or answer_1 == 3 or answer_1 == 4 :
            print("YOU GOT WRONG ANSWER,CORRECT IS \"Margaret Thatcher\"") 
        else :
            print("Error")         
    finally:
        print("MCQ-2 :: Who is the current (as of 2024) Secretary-General of the United Nations?")
        print("1.Ban Ki-moon")
        print("2.Kofi Annan")    
        print("3.Boutros Boutros-Ghali") 
        print("4.António Guterres") 
        answer_2 = int((input("Answer is: " )))
    try:
        if answer_2 == 4:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
        elif answer_2 == 1 or answer_2 == 2 or answer_2 == 3 :
            print("YOU GOT WRONG ANSWER,CORRECT IS \"António Guterres\"") 
        else :
            print("Error")        
    finally: 
        print("MCQ-3 :: The concept of 'Iron Curtain' was popularized during which major historical period?")
        print("1.World War I")
        print("2.World War II")    
        print("3.Cold War") 
        print("4.Vietnam War") 
        answer_3 = int((input("Answer is: " )))       
    try:
        if answer_3 == 3:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
        elif answer_3 == 1 or answer_3 == 2 or answer_3 == 4 :
            print("YOU GOT WRONG ANSWER,CORRECT IS \"Cold War\"") 
        else :
            print("Error")    
    finally: 
        print("MCQ-4 :: Which of the following countries is a permanent member of the UN Security Council?")
        print("1.Germany")
        print("2.China")    
        print("3.India") 
        print("4.Japan") 
        answer_4 = int((input("Answer is: " )))       
    try:
        if answer_4 == 2:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
        elif answer_4 == 1 or answer_4 == 3 or answer_4 == 4 :
            print("YOU GOT WRONG ANSWER,CORRECT IS \"China\"") 
        else :
            print("Error")    
    finally: 
        print("MCQ-5 ::Who is known as the Father of the Indian Constitution?")
        print("1.Mahatma Gandhi")
        print("2.Jawaharlal Nehru")    
        print("3.Sardar Vallabhbhai Patel") 
        print("4.B.R.Ambedkar") 
        answer_5 = int((input("Answer is: " )))     
    if answer_5 == 4:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
    elif answer_5 == 1 or answer_5 == 2 or answer_5 == 3 :
            print("YOU GOT WRONG ANSWER,CORRECT IS \"B.R.Ambedkar\"") 
    else :
            print("Error")        
    print("FROM 5 MCQ'S YOU GOT "+ str(corrected) + " CORRECTED")    

def Pakistan():
    corrected = 0
    print("MCQ-1 ::Which river is the longest in Pakistan?")
    print("1.Chenab River")
    print("2.Indus River")    
    print("3.Ravi River") 
    print("4.Jhelum River") 
    answer_1 = int((input("Answer is: " )))
    try:
        if answer_1 == 2:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
        elif answer_1 == 1 or answer_1 == 3 or answer_1 == 4 :
            print("YOU GOT WRONG ANSWER,CORRECT IS \"Indus River\"") 
        else :
            print("Error")         
    finally:
        print("MCQ-2 :: Which city is known as the \"City of Gardens\" in Pakistan?")
        print("1.Islamabad")
        print("2.Faisalabad")    
        print("3.Karachi") 
        print("4.Lahore") 
        answer_2 = int((input("Answer is: " )))
    try:
        if answer_2 == 4:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
        elif answer_2 == 1 or answer_2 == 2 or answer_2 == 3 :
            print("YOU GOT WRONG ANSWER,CORRECT IS \"Lahore\"") 
        else :
            print("Error")        
    finally: 
        print("MCQ-3 :: Which mountain is the highest peak in Pakistan?")
        print("1.Nanga Parbat")
        print("2.Rakaposhi")    
        print("3.K2") 
        print("4.Gasherbrum I") 
        answer_3 = int((input("Answer is: " )))       
    try:
        if answer_3 == 3:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
        elif answer_3 == 1 or answer_3 == 2 or answer_3 == 4 :
            print("YOU GOT WRONG ANSWER,CORRECT IS \"K2\"") 
        else :
            print("Error")    
    finally: 
        print("MCQ-4 ::Which desert is located in the southeastern part of Pakistan?")
        print("1.Sahara Desert")
        print("2.Thar Desert")    
        print("3.Gobi Desert") 
        print("4.Kalahari Desert") 
        answer_4 = int((input("Answer is: " )))       
    try:
        if answer_4 == 2:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
        elif answer_4 == 1 or answer_4 == 3 or answer_4 == 4 :
            print("YOU GOT WRONG ANSWER,CORRECT IS \"Thar Desert\"") 
        else :
            print("Error")    
    finally: 
        print("MCQ-5 ::Which Pakistani city is known for its ancient civilization, Mohenjo-Daro?")
        print("1.Lahore")
        print("2.Karachi")    
        print("3.Multan") 
        print("4.Larkana") 
        answer_5 = int((input("Answer is: " )))     
    if answer_5 == 4:
            print("CONGRATULATIONS YOU GOT CORRECT ANSWER") 
            corrected +=1
    elif answer_5 == 1 or answer_5 == 2 or answer_5 == 3 :
            print("YOU GOT WRONG ANSWER,CORRECT IS \"Larkana\"") 
    else :
            print("Error")        
    print("FROM 5 MCQ'S YOU GOT "+ str(corrected) + " CORRECTED")        

def Play_again():
    again = input("Do you want to play again(Yes/No):")    

def main():
    while True:
        welcome_rules()
        topic_name()
        global a 
        if a == 1:
            Cricket()
        elif a== 2:
            Politics()
        else:
            Pakistan() 
        again = input("Do you want to play again(Yes/No):")
        if again == "Yes":
            print("")
        elif again == "No":
            print("\"THANKS FOR PLAYING\"")
            break    

if __name__ == "__main__":
    main()               
        