def journal():
    while True:
        list1=[]
        action = input("Enter 'write' to add an entry, 'read' to view an entry, or 'exit' to quit: ").lower()
        
        if action == 'write':
            Date_in = input("Enter today's date: ")
            Date_in += '.txt'
            list1.append(Date_in)
            thoughts = input("Enter the thought of the day: ")
            with open(Date_in, 'w') as file:
                file.write(thoughts)
            print("Entry saved successfully.")
        
        elif action == 'read':
            print(list1)
            Date_in = input("Enter the date to show: ")
            Date_in += '.txt'
            try:
                with open(Date_in, 'r') as file:
                    content = file.read()
                    print(f"Thoughts for {Date_in[:-4]}:")
                    print(content)
            except FileNotFoundError:
                print(f"No entry found for {Date_in[:-4]}")
        
        elif action == 'exit':
            print("Exiting the journal. Goodbye!")
            break
        
        else:
            print("Invalid input. Please try again.")
            
            

journal()