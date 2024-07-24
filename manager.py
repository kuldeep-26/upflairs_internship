manager_name = "Dharampal Ji"
manager_add = "Bihar"

emp_list = ['rohit','rahul','mohit','suresh','jagdish']

rohit_id = 'hello@gmail.com'
rohit_pass = '124@786'
def rohit_hi():
    print('Employee Name: ','Rohit')
    print('Rohit Id: ',rohit_id)
    print('Rohit Password: ',rohit_pass)

print('Manager file executed !')
if __name__ == "__main__":         # Restriction (Now only execute from manager.py)

    def manager_hi():
        print('Manager Name: ','Dharampal')
        print('Dharmpal Id: ',manager_id)
        print('Dharampal Password: ',manager_pass)

    manager_id = 'manager_boss@gmail.com'
    manager_pass = 'boss123456'