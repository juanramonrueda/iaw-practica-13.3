#-----------------------------------------------------------------------------------------------------------------
# Importación de módulos / bibliotecas para el código

# Importación del módulo sys para importar módulos que están en niveles superiores del directorio actual
import sys

# "Subida" de dos niveles para importar el módulo para los ejercicios
sys.path.append("../..")

# Importación de módulo creado para la realización de los ejercicios
from aws_python_boto3.ejemplos.common import aws_resource_functions as aws


#-----------------------------------------------------------------------------------------------------------------
# Declaración de variables para la creación de la instancia

# Declaración de la variable para selección del sistema operativo de la instancia
ami_id = 'ami-08e637cea2f053dfa'

# Declaración de la variable para especificar la cantidad de instancias a crear
number_of_instances = '1'

# Declaración de la variable para especificar la cantidad de memoria RAM que necesita
instance_type = 't2.micro'

# Declaración de la variable para especificar el archivo de claves a usar para la conexión
private_key = 'vockey'

# Declaración de la variable para especificar el nombre que tendrá la instancia
instance_name = 'backend'


#-----------------------------------------------------------------------------------------------------------------
# Declaración de variables para la creación del grupo de seguridad

# Declaración de la variable para el nombre del grupo de seguridad
security_group_name = 'backend-sg'

# Declaración de la variable para la descripción del grupo de seguridad
security_group_description = 'Grupo de seguridad para instancias backend'


#-----------------------------------------------------------------------------------------------------------------
# Reglas de entrada para un grupo de seguridad

# Definición de una lista para las reglas de entrada para el grupo de seguridad de los backend
ingress_permissions = [
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22},    
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 3306, 'ToPort': 3306}]


#-----------------------------------------------------------------------------------------------------------------
# Llamada a la función del módulo aws para crear el grupo de seguridad

aws.create_security_group(security_group_name, security_group_description, ingress_permissions)


#-----------------------------------------------------------------------------------------------------------------
# Comprobación de los grupos de seguridad

aws.list_security_groups()


#-----------------------------------------------------------------------------------------------------------------
# Llamada a la función para la creación de la instancia

aws.create_instance(ami_id, number_of_instances, instance_type, private_key, instance_name, security_group_name)