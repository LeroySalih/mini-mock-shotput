COMPETITORS = [
  'Pupil 1', 'Pupil 2', 'Pupil 3' 
]

ATTEMPTS = [
  [4, 6, 7],
  [3, 1, 2],
  [2, 9, -1]
]

def show_menu():
  print("Chose and option:")
  print("1. Add a pupil")
  print("2. Add an attempt for a pupil")
  print("3. Calculate the winner")
  print("4. Display Data")
  print("5. Quit")


#Todo - tell the user the id of the added pupil 
def add_pupil():
  pupil_name = input("Enter Pupil name: ")
  COMPETITORS.append(pupil_name)
  ATTEMPTS.append([])


#Todo - check that no more than 3 attempts can be added 
def add_attempt():
  pupil_id = int(input("Enter Pupil ID"))
  pupil_attempt = int(input("Enter Attempt for pupil"))
  ATTEMPTS[pupil_id].append(pupil_attempt) 

#Todo Create a trace table 
#Todo Make sure that there are attempts before checking if the pupil has won.
#Todo Display the pupil name of the winner

def calc_winner():

  winner = -1
  winning_attempt = -1
  
  for i in range(len(COMPETITORS)):
    current_pupil = COMPETITORS[i]
    
    highest = sorted(ATTEMPTS[i], reverse=True)[0]
    
    if highest > winning_attempt:
      winner = i 
      winning_attempt = highest 

  print("The Winner is {0} with a distance of {1}".format(winner, winning_attempt) ) 

def display_data():
  print (COMPETITORS)
  print (ATTEMPTS)


def main():
  
  show_menu()
  choice = int(input("Enter Choice: "))
  
  while choice != 5:

    if choice == 1:
      add_pupil()
    
    if choice == 2:
      add_attempt()
    
    if choice ==3:
      calc_winner()

    if choice == 4:
      display_data()

    show_menu()
    choice = int(input("Enter Choice: "))

if __name__ == "__main__":
  main()
