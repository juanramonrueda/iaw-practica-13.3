#----------------------------------------------------------------------------------------------------------------------------------
# Definición de variables para la creación de las instancias

# Declaración de la variable para el nombre de la instancia que hará de balanceador de carga
instance_name_balancer = 'iaw-practica-09-balancer'

# Declaración de la variable para el nombre de la instancia que hará de primer frontal
instance_name_frontend_01 = 'iaw-practica-09-frontend-01'

# Declaración de la variable para el nombre de la instancia que hará de segundo frontal
instance_name_frontend_02 = 'iaw-practica-09-frontend-02'

# Declaración de la variable para el nombre de la instancia que hará de backend
instance_name_backend = 'iaw-practica-09-backend'

# Declaración de la variable para el nombre de la instancia que hará de NFS Server
instance_name_nfs = 'iaw-practica-09-nfs'

# Declaración de la variable para establecer el sistema operativo Amazon Linux
amazon_linux_ami_id = 'ami-0b5eea76982371e91'

# Declaración de la variable para establecer el sistema operativo Ubuntu Server 22.04
ubuntu_22_ami_id = 'ami-08e637cea2f053dfa'

# Declaración de la variable para establecer la cantidad de memoria RAM para la instancia, en este caso 1GB
instance_ram_1gb = 't2.micro'

# Declaración de la variable para establecer la cantidad de memoria RAM para la instancia, en este caso 4GB
instance_ram_4gb = 't2.medium'

# Declaración de la variable para establecer la cantidad de memoria RAM para la instancia, en este caso 8GB
instance_ram_8gb = 't2.large'

# Declaración de la variable para establecer el archivo de claves de conexión mediante SSH
ssh_key = 'vockey'

# Declaración de la variable para establecer la cantidad de instancias que van a crearse
total_instances = 1


#----------------------------------------------------------------------------------------------------------------------------------
# Declaración de las variables para los grupos de seguridad

# Declaración de la variable para el nombre del grupo de seguridad de los balanceadores
security_group_name_balancer = 'sg_balancer'

# Declaración de la variable para la descripción del grupo de seguridad de los balanceadores
security_group_description_balancer = 'Grupo de seguridad para los balanceadores de carga'

# Declaración de la variable para el nombre del grupo de seguridad de los frontales
security_group_name_frontend = 'sg_frontend'

# Declaración de la variable para la descripción del grupo de seguridad de los frontales
security_group_description_frontend = 'Grupo de seguridad para los frontales con balanceador de carga'

# Declaración de la variable para el nombre del grupo de seguridad de los backend
security_group_name_backend = 'sg_backend'

# Declaración de la variable para la descripción del grupo de seguridad de los backend
security_group_description_backend = 'Grupo de seguridad para los backend'

# Declaración de la variable para el nombre del grupo de seguridad de los NFS Server
security_group_name_nfs = 'sg_nfs'

# Declaración de la variable para la descripción del grupo de seguridad de los NFS Server
security_group_description_nfs = 'Grupo de seguridad para los NFS Server'


#----------------------------------------------------------------------------------------------------------------------------------
# Reglas de entrada de los grupos de seguridad

# Definición de una lista para las reglas de entrada para el grupo de seguridad de los balanceadores
balancer_ingress_permissions = [
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22},    
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80},
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 443, 'ToPort': 443}]


# Definición de una lista para las reglas de entrada para el grupo de seguridad de los frontales
frontend_ingress_permissions = [
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22},    
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80}]


# Definición de una lista para las reglas de entrada para el grupo de seguridad de los backend
backend_ingress_permissions = [
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22},    
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 3306, 'ToPort': 3306}]


# Definición de una lista para las reglas de entrada para el grupo de seguridad de los NFS Server
nfs_ingress_permissions = [
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22},    
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 2059, 'ToPort': 2059}]

