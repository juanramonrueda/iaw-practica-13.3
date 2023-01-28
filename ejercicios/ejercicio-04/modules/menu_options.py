#-------------------------------------------------------------------------
# Declaración de funciones que hacen de menú

# Función con las distintas opciones disponibles
def main_menu():
    print('\n---   Security Group   ---')
    print(' 1.- List security groups')
    print(' 2.- Create security group')
    print(' 3.- Delete security group')
    print('\n---   EC2 Instance   ---')
    print(' 4.- Create EC2 instance')
    print(' 5.- Start EC2 instance')
    print(' 6.- Stop EC2 instance')
    print(' 7.- Terminate EC2 instance')
    print('\n---   EC2 Instances   ---')    
    print(' 8.- List all EC2 instances')
    print(' 9.- Start all EC2 instances')
    print(' 10.- Stop all EC2 instances')
    print(' 11.- Terminate all EC2 instances')
    print('\n---   Elastic IP   ---')
    print(' 12.- Allocate and associate Elastic IP')
    print(' 13.- Release Elastic IP')
    print('\n 14.- Exit')


# Función para mostrar los grupos de seguridad disponibles
def security_groups():
    print('\n---   Security Groups   ---')
    print(' 1.- Load balancer security group\n Open TCP ports: SSH, HTTP, HTTPS')
    print('\n 2.- Frontend security group\n Open TCP ports: SSH, HTTP')
    print('\n 3.- Backend security group\n Open TCP ports: SSH, MySQL / Aurora (3306)')
    print('\n 4.- NFS Server security group\n Open TCP ports: SSH, NFS Server (2049)')


# Función para mostrar las instancias disponibles
def amis():
    print('\n---   AMI Instances   ---')
    print(' 1.- Ubuntu Server 22.04')
    print(' 2.- Red Hat Enterprise Linux 9')
    print(' 3.- Amazon Linux 9')


# Función para mostrar los tipos de instancias disponibles
def instance_ram():
    print('\n---   RAM Instances   ---')
    print(' 1.- t2.micro (1GB)')
    print(' 2.- t2.small (2GB)')
    print(' 3.- t2.medium (4GB)')
    print(' 4.- t2.large (8GB)')