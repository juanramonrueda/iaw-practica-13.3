import boto3

# Creación de un objeto ec2 de boto3
ec2 = boto3.resource('ec2')

# Obtención de listado de todos los grupos de seguridad
for sg in ec2.security_groups.all():
    print(f'group_id: {sg.group_id} \t group_name: {sg.group_name} \t description: {sg.description}')
    print(sg.ip_permissions)
