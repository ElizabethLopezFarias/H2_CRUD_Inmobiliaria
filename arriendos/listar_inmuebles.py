import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arriendos.settings')
django.setup()

from app_arriendos.models import Inmuebles

def listar_inmuebles_por_comuna():
    inmuebles = Inmuebles.objects.select_related('id_direccion__id_ubicacion').all()

    comunas_list = {}

    for inmueble in inmuebles:
        comuna = inmueble.id_direccion.id_ubicacion.nombre_comuna
        if comuna not in comunas_list:
            comunas_list[comuna] = []
        comunas_list[comuna].append({
            'nombre': inmueble.nombre,
            'descripcion': inmueble.descripcion
        })

    return comunas_list

def guardar_inmuebles_en_archivo(comunas_list, archivo):
    with open(archivo, 'w', encoding='utf-8') as f:
        for comuna, inmuebles in comunas_list.items():
            f.write(f"Comuna: {comuna}\n")
            for inmueble in inmuebles:
                f.write(f"  Nombre: {inmueble['nombre']}\n")
                f.write(f"  Descripción: {inmueble['descripcion']}\n")
            f.write("\n")


def listar_inmuebles_por_region():
    inmuebles = Inmuebles.objects.select_related('id_direccion__id_ubicacion').all()

    regiones_list = {}

    for inmueble in inmuebles:
        region = inmueble.id_direccion.id_ubicacion.nombre_region
        if region not in regiones_list:
            regiones_list[region] = []
        regiones_list[region].append({
            'nombre': inmueble.nombre,
            'descripcion': inmueble.descripcion
        })

    return regiones_list

def guardar_inmuebles_en_archivo_region(regiones_list, archivo):
    with open(archivo, 'w', encoding='utf-8') as f:
        for region, inmuebles in regiones_list.items():
            f.write(f"Región: {region}\n")
            for inmueble in inmuebles:
                f.write(f"  Nombre: {inmueble['nombre']}\n")
                f.write(f"  Descripción: {inmueble['descripcion']}\n")
            f.write("\n")

if __name__ == "__main__":
#Archivo salida comuna
    archivo_salida = 'inmuebles_por_comuna.txt'
    comunas_list = listar_inmuebles_por_comuna()
    guardar_inmuebles_en_archivo(comunas_list, archivo_salida)
    print(f"Listado de inmuebles guardado en {archivo_salida}")
#Archivo salida region
    archivo_salida_region = 'inmuebles_por_region.txt'
    regiones_list = listar_inmuebles_por_region()
    guardar_inmuebles_en_archivo_region(regiones_list, archivo_salida_region)
    print(f"Listado de inmuebles guardado en {archivo_salida_region}")
