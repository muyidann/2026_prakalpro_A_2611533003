correct_pin = "1234" 
MAX_ATTEMPTS = 3       
attempt = 1            
pin = ""

while pin != correct_pin and attempt <= MAX_ATTEMPTS:  
    pin = input("Enter PIN: ")  

    if pin == correct_pin:  
        print("Access granted")  
    else:  
        attempt += 1  
        print("Incorrect PIN.") 

if pin != correct_pin: 
    print("Account locked") 