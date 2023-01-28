#------------------------------------------------------------------------------------------------
# Import libraries / modules for the code

# Import library / module to know the operating system where the code is executed
import platform

# Import library / module to run instructions according to the operating system
import os


#------------------------------------------------------------------------------------------------
# Declaration of functions

# Function to detect the operating system where the code is executed
def main():
    # Detection of the operating system using platform.system() and saved in a variable
    os_system = platform.system()

    # In the case that it is neither Linux nor Windows, the execution of the code will end
    if (os_system != 'Linux') and (os_system != 'Windows'):
        print('It is neither Linux nor Windows, so the program execution will stop')
        exit()

    # In the case that it is Linux system, it will use the command "clear" to clear the screen
    elif os_system == "Linux":
        # Execution of the command "clear" to clear the screen using os.system()
        os.system('clear')
    
    # In the case that it is Windows system, it will use the command "cls" to clear the screen
    elif os_system == "Windows":
        # Execution of the command "cls" to clear the screen using os.system()
        os.system('cls')