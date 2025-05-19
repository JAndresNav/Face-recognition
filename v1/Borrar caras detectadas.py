import os
import shutil

CARAS_DIR = 'caras_detectadas'

# Recorrer todas las subcarpetas
for persona in os.listdir(CARAS_DIR):
    persona_dir = os.path.join(CARAS_DIR, persona)
    if not os.path.isdir(persona_dir):
        continue

    try:
        shutil.rmtree(persona_dir)
        print(f"🗑 Carpeta eliminada: {persona_dir}")
    except Exception as e:
        print(f"⚠ No se pudo eliminar la carpeta {persona_dir}: {e}")

print("\n✅ Todas las fotos y carpetas de 'caras_detectadas/' fueron eliminadas.")
