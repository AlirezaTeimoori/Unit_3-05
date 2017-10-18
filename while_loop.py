# Created by : Sidney Kang
# Created on : 15 Oct 2017
# Created for : ICS3UR
# Daily Assignment - Unit3-05
# This program displays a while loop program

import ui



def calculate_touch_up_inside(sender):
    
    user_input = int(view['user_input_textbox'].text)
    if user_input >= 0:
        answer = 1
        while user_input >= 1 :
            answer = answer * (user_input)
            
            user_input = user_input - 1
            
        view['answer_label'].text="The answer is: " + str(answer)
    else:
        view['answer_label'].text="enter a number greater than or equal to zero"
        
view = ui.load_view()
view.present('sheet')
