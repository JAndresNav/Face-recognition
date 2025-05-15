import os
import shutil

CARPETAS_A_LIMPIAR = ['personas_agrupadas', 'miniaturas_marcadas']

for carpeta in CARPETAS_A_LIMPIAR:
    if not os.path.exists(carpeta):
        print(f"❌ La carpeta '{carpeta}' no existe.")
        continue

    for subelemento in os.listdir(carpeta):
        ruta = os.path.join(carpeta, subelemento)
        try:
            if os.path.isdir(ruta):
                shutil.rmtree(ruta)
                print(f"🧹 Carpeta eliminada: {ruta}")
            else:
                os.remove(ruta)
                print(f"🗑 Archivo eliminado: {ruta}")
        except Exception as e:
            print(f"❌ Error al borrar {ruta}: {e}")

print("\n✅ Limpieza completa de 'personas_agrupadas/' y 'miniaturas_marcadas/'")
