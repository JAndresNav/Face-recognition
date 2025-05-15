import os

CARAS_DIR = 'caras_detectadas'

# Recorrer todas las subcarpetas
for persona in os.listdir(CARAS_DIR):
    persona_dir = os.path.join(CARAS_DIR, persona)
    if not os.path.isdir(persona_dir):
        continue

    for archivo in os.listdir(persona_dir):
        archivo_path = os.path.join(persona_dir, archivo)
        try:
            os.remove(archivo_path)
            print(f"🗑 Borrado: {archivo_path}")
        except Exception as e:
            print(f"⚠ No se pudo borrar {archivo_path}: {e}")

print("\n✅ Todas las fotos de 'caras_detectadas/' fueron eliminadas.")
