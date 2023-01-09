from Cotizador.models import Neumatico

#Bridgestone Turanza ER300

Neumatico(medida="205/55r16", marca="Bridgestone", modelo="Turanza ER300", stock=12, precio="$79.800").save()
Neumatico(medida="225/45r17", marca="Bridgestone", modelo="Turanza ER300", stock=35, precio="$102.000").save()
Neumatico(medida="185/65r15", marca="Bridgestone", modelo="Turanza ER300", stock=0, precio="$64.000").save()

#Firestone F-600

Neumatico(medida="175/65r14", marca="Firestone", modelo="F-600", stock=16, precio="$34.600").save()
Neumatico(medida="175/70r14", marca="Firestone", modelo="F-600", stock=53, precio="$36.300").save()
Neumatico(medida="185/60r14", marca="Firestone", modelo="F-600", stock=12, precio="$34.600").save()
print("Se cargó el nuevo neumático correctamente")


