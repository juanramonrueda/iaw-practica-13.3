#-----------------------------------------------------------------------------------------------------------
# Import of modules

# sys module import to import modules that are at higher levels of the current directory
import sys

# Import the time module to control some executions
import time

# Two-level upload to import module for exercises
sys.path.append("../..")

# Import of module created to carry out the exercises
from aws_python_boto3.ejemplos.common import aws_resource_functions as aws

# Variable file import
from ejercicios.vars import variables

# Module import to clear screen
from modules import clear_screen
 
# Import of personal modules
from modules import menu_options


#-----------------------------------------------------------------------------------------------------------
# Variable declaration

# Variable declaration to enter the WHILE loop
user_option = str(1)

counter = 0

#-----------------------------------------------------------------------------------------------------------
# Declaration of functions

# Main function
def main(user_option, counter):
    while user_option != '14':
        if counter >= 1:
            time.sleep(3)
            input('\nPress the Enter key to continue... ')

        clear_screen.main()
        menu_options.main_menu()
        user_option = str(input('\nSelect a menu option (1 - 14): '))

        if user_option == '1':
            aws.list_security_groups()

        elif user_option == '2':
            menu_options.security_groups()
            sg_choice = str(input('\nSelect the security group (1 - 4): '))
            if sg_choice == '1':
                sg_ingress_permissions = variables.balancer_ingress_permissions
            elif sg_choice == '2':
                sg_ingress_permissions = variables.frontend_ingress_permissions
            elif sg_choice == '3':
                sg_ingress_permissions = variables.backend_ingress_permissions
            elif sg_choice == '4':
                sg_ingress_permissions = variables.nfs_ingress_permissions
            else:
                print('Wrong option, returning to main menu...')
                time.sleep(3)
                continue
            sg_name = input('Enter the name for the security group: ')
            sg_description = input('Enter the description for the security group: ')
            aws.create_security_group(sg_name, sg_description, sg_ingress_permissions)

        elif user_option == '3':
            sg_name = input('Enter the name of the security group to be deleted: ')
            aws.delete_security_group(sg_name)
            if aws.security_group_exists(sg_name) == False:
                print('\nThe security group does not exist')
                time.sleep(3)
                continue
        
        elif user_option == '4':
            count = 0
            menu_options.amis()
            ami_option = int(input('\nSelect the AMI to assign to the instance (1 - 3): '))
            if ami_option == 1:
                ami_code = variables.ubuntu_22_ami_id
            elif ami_option == 2:
                ami_code = variables.rhel_9_ami_id
            elif ami_option == 3:
                ami_code = variables.amazon_linux_ami_id
            else:
                print('Wrong option, returning to main menu...')
                time.sleep(3)
                continue
            total_instances = int(input('Enter the total instances to create (min 1 -- max 9): '))
            while total_instances < 1 or total_instances > 9:
                total_instances = int(input('Enter the total instances to create (min 1 -- max 9): '))
                count = count + 1
                if count >= 5:
                    print('Jerk!!')
                    time.sleep(3)
                    continue
            menu_options.instance_ram()
            ram_type = int(input('\nSelect the total RAM to assign to the instance: '))
            if ram_type == 1:
                ram_instance = variables.instance_ram_1gb
            elif ram_type == 2:
                ram_instance = variables.instance_ram_2b
            elif ram_type == 3:
                ram_instance = variables.instance_ram_4gb
            elif ram_type == 4:
                ram_instance = variables.instance_ram_8gb
            else:
                print('Wrong option, returning to main menu...')
                time.sleep(3)
                continue
            key_file = input('Enter the name of private key to use against the SSH server: ')
            instance_name = input('Enter the instance name: ')
            sg_name = input('Select the security group to assign: ')
            if aws.security_group_exists(sg_name) == False:
                print('\nThe security group does not exist')
                time.sleep(3)
                continue
            aws.create_instance(ami_code, total_instances, ram_instance, key_file, instance_name, sg_name)

        elif user_option == '5':
            instance_name = input('\nEnter the instance name: ')
            aws.start_instance(instance_name)

        elif user_option == '6':
            instance_name = input('\nEnter the instance name: ')
            aws.stop_instance(instance_name)

        elif user_option == '7':
            instance_name = input('\nEnter the instance name: ')
            aws.terminate_instance(instance_name)

        elif user_option == '8':
            aws.list_instances()

        elif user_option == '9':
            aws.start_instances()

        elif user_option == '10':
            aws.stop_instances()

        elif user_option == '11':
            aws.terminate_instances()

        elif user_option == '12':
            instance_name = input('Instance the instance name: ')
            instance_id = aws.get_instance_id(instance_name)

            if instance_id == None:
                print('There is no instance with that name')
                time.sleep(4)
                continue

            # Allocate and associate Elastic IP
            elastic_ip = aws.allocate_elastic_ip()
            aws.associate_elastic_ip(elastic_ip, instance_id)

        elif user_option == '13':
            instance_name = input('Instance name: ')
            instance_id = aws.get_instance_id(instance_name)

            if instance_id == None:
                print('There is no instance with that name')
                time.sleep(4)
                continue

            # Get Elastic IP from instance ID
            elastic_ip = aws.get_instance_public_ip(instance_id)

            # Release Elastic IP
            aws.release_elastic_ip(elastic_ip)

        elif user_option == '14':
            print('Bye!')

        else:
            print('Invalid option')

        counter = counter + 1

#-----------------------------------------------------------------------------------------------------------
# Execution of the "main" function
if __name__ == "__main__":
    main(user_option, counter)