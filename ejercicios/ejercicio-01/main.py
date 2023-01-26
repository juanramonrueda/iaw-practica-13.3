#------------------------------------------------------------------------------------------------------------------------------------------------------
# Importación de módulos / bibliotecas para el código

# Importación del módulo sys para importar módulos que están en niveles superiores del directorio actual
import sys

# "Subida" de dos niveles para importar el módulo para los ejercicios
sys.path.append("../..")

# Importación de módulo creado para la realización de los ejercicios
from aws_python_boto3.ejemplos.common import aws_resource_functions as aws

# Importación del archivo de variables
from ejercicios.vars import variables


#------------------------------------------------------------------------------------------------------------------------------------------------------
# Llamada a la función del módulo aws para crear el grupo de seguridad para las instancias backend

aws.create_security_group(variables.security_group_name_backend, variables.security_group_description_backend, variables.backend_ingress_permissions)


#------------------------------------------------------------------------------------------------------------------------------------------------------
# Comprobación de los grupos de seguridad

aws.list_security_groups()