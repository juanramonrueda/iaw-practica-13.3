#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Importación de módulos / bibliotecas para el código

# Importación del módulo sys para importar módulos que están en niveles superiores del directorio actual
import sys

# "Subida" de dos niveles para importar el módulo para los ejercicios
sys.path.append("../..")

# Importación de módulo creado para la realización de los ejercicios
from aws_python_boto3.ejemplos.common import aws_resource_functions as aws

# Importación del archivo de variables
from ejercicios.vars import variables


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creación de los grupos de seguridad

# Creación del grupo de seguridad del balanceador de carga
aws.create_security_group(variables.security_group_name_balancer, variables.security_group_description_balancer, variables.balancer_ingress_permissions)

# Creación del grupo de seguridad de los frontend
aws.create_security_group(variables.security_group_name_frontend, variables.security_group_description_frontend, variables.frontend_ingress_permissions)

# Creación del grupo de seguridad para los backend
aws.create_security_group(variables.security_group_name_backend, variables.security_group_description_backend, variables.backend_ingress_permissions)

# Creación del grupo de seguridad para el servidor NFS
aws.create_security_group(variables.security_group_name_nfs, variables.security_group_description_nfs, variables.nfs_ingress_permissions)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creación de las instancias

# Creación de la instancia que hará de balanceador de carga
aws.create_instance(variables.amazon_linux_ami_id, variables.total_instances, variables.instance_ram_4gb, variables.ssh_key, variables.instance_name_balancer, variables.security_group_name_balancer)

# Creación de la instancia que hará de primer frontend
aws.create_instance(variables.amazon_linux_ami_id, variables.total_instances, variables.instance_ram_4gb, variables.ssh_key, variables.instance_name_frontend_01, variables.security_group_name_frontend)

# Creación de la instancia que hará de segundo frontend
aws.create_instance(variables.amazon_linux_ami_id, variables.total_instances, variables.instance_ram_4gb, variables.ssh_key, variables.instance_name_frontend_02, variables.security_group_name_frontend)

# Creación de la instancia que hará de backend
aws.create_instance(variables.amazon_linux_ami_id, variables.total_instances, variables.instance_ram_8gb, variables.ssh_key, variables.instance_name_backend, variables.security_group_name_backend)

# Creación de la instnacian que hará de NFS Server
aws.create_instance(variables.amazon_linux_ami_id, variables.total_instances, variables.instance_ram_4gb, variables.ssh_key, variables.instance_name_nfs, variables.security_group_name_nfs)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Obtención y asociación de la IP elástica a una instancia

# Obtención de una dirección IP a la cuenta
elastic_ip = aws.allocate_elastic_ip()

# Obtención del identificador de la instancia
balancer_id = aws.get_instance_id(variables.instance_name_balancer)

# Asociación de la IP elástica al balanceador
aws.associate_elastic_ip(elastic_ip, balancer_id)