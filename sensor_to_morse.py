import time
variable_X = False
variable_Y = False
variable_Z = True



def classify_input():
    morse_words = [".-.-",".-.-----",".-."]
    morse_word = ""

    while True:
        # variable_X = read_sensor_X()
        # variable_Y = read_sensor_Y()
        # variable_Z = read_sensor_Z()

        if (variable_X and not variable_Y and not variable_Z):
            morse_word += "."
        elif (not variable_X and variable_Y and not variable_Z):
            morse_word += "-"
        elif (not variable_X and not variable_Y and variable_Z):
            morse_words.append(morse_word)
            
            with open('morse1.txt', 'w') as file:
                
                file.write(''.join(morse_words))
                morse_word = ""
        else:
            continue

        # with open('morse1.txt', 'w') as file:
            
        #     file.write(''.join(morse_words))
        time.sleep(1)  # Adjust the time interval as needed

classify_input()






