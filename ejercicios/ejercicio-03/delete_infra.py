#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Importación de módulos / bibliotecas para el código

# Importación del módulo sys para importar módulos que están en niveles superiores del directorio actual
import sys

# "Subida" de dos niveles para importar el módulo para los ejercicios
sys.path.append("../..")

# Importación de módulo creado para la realización de los ejercicios
from aws_python_boto3.ejemplos.common import aws_resource_functions as aws

# Importación del archivo de variables
from ejercicios.vars import variables


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Declaración de listas para la eliminación de instancias y grupos de seguridad

# Declaración de una lista con los nombres de las instancias que hay que eliminar
ec2_list_instance_name = [variables.instance_name_balancer, variables.instance_name_frontend_01, variables.instance_name_frontend_02, variables.instance_name_backend, variables.instance_name_nfs]

# Declaración de una lista con los nombres de los grupos de seguridad que hay que eliminar
ec2_list_security_group_name = [variables.security_group_name_balancer, variables.security_group_name_frontend, variables.security_group_name_backend, variables.security_group_name_nfs]


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Obtención del ID de la instancia que hace de balanceador de carga, su IP elástica y la liberación de la misma

# Obtención del ID de la instancia que hace de balanceador de carga
balancer_id = aws.get_instance_id(ec2_list_instance_name[0])

# Obtención de la IP elástica del balanceador de carga mediante el ID de la instancia
balancer_ip = aws.get_instance_public_ip(balancer_id)

# Liberación de la IP elástica del balanceador de carga
aws.release_elastic_ip(balancer_ip)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Eliminación de una serie de instancias según el nombre que hay en la lista

for ec2_name in ec2_list_instance_name:
    print(f'Terminating the instance {ec2_name}...')

    # Eliminación de la instancia por nombre que hay en ese momento en el bucle 
    aws.terminate_instance_waiting(ec2_name)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Eliminación de los grupos de seguridad

for sg_name in ec2_list_security_group_name:
    print(f'Terminating the security group {sg_name}...')

    # Eliminación del grupo de seguridad por nombre que hay en ese momento en el bucle
    aws.delete_security_group(sg_name)