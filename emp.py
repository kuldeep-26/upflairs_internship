# Rohit
#import manager

#print(manager.rohit_id)
#print(manager.rohit_pass)

#print(manager.emp_list)

# calling...
#manager.rohit_hi()

#import manager as mng
#mng.manager_hi()

# problem :-  1. Security   2. Storage

# storage solution :-
#from manager import rohit_id
#from manager import rohit_pass
#from manager import rohit_hi
#print('Employee file executed !')
#print(rohit_id)
#print(rohit_pass)
#print()
#rohit_hi()

# security solution :-            # __name__ == "__main__":
#from manager import manager_id
#print(manager_id)