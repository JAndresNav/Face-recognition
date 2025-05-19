import face_recognition
import os
import cv2
import pickle
import json

TOLERANCIA_RECONOCIMIENTO = 0.55

FOTOS_DIR = 'Fotos'
OUTPUT_DIR = 'personas_agrupadas'
MARCAS_DIR = 'miniaturas_marcadas'
ENCODINGS_FILE = 'encodings_autodetectados.pkl'

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(MARCAS_DIR, exist_ok=True)

if os.path.exists(ENCODINGS_FILE):
    with open(ENCODINGS_FILE, 'rb') as f:
        encodings_data, person_folders = pickle.load(f)
else:
    encodings_data = []
    person_folders = []

for filename in os.listdir(FOTOS_DIR):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    image_path = os.path.join(FOTOS_DIR, filename)
    print(f"📸 Procesando: {image_path}")
    image = face_recognition.load_image_file(image_path)
    locations = face_recognition.face_locations(image)
    encodings = face_recognition.face_encodings(image, locations)

    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cara_ids_en_foto = []

    for i, (face_encoding, face_location) in enumerate(zip(encodings, locations)):
        match_found = False
        folder = None

        if encodings_data:
            distances = face_recognition.face_distance(encodings_data, face_encoding)
            if len(distances) > 0 and min(distances) < TOLERANCIA_RECONOCIMIENTO:
                index = int(distances.argmin())
                folder = person_folders[index]
                match_found = True

        if not match_found:
            person_id = len(person_folders) + 1
            folder = f'persona_{person_id:03d}'
            person_folders.append(folder)
            encodings_data.append(face_encoding)

        person_path = os.path.join(OUTPUT_DIR, folder)
        os.makedirs(person_path, exist_ok=True)

        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        face_bgr = cv2.cvtColor(face_image, cv2.COLOR_RGB2BGR)
        count = len([f for f in os.listdir(person_path) if f.endswith('.jpg')]) + 1
        output_file = os.path.join(person_path, f'{count}.jpg')
        cv2.imwrite(output_file, face_bgr)
        print(f"🧠 Cara guardada en: {output_file}")

        cara_ids_en_foto.append((i + 1, folder))

        # Actualizar json con el nombre del archivo original
        json_file = os.path.join(person_path, "info.json")
        if os.path.exists(json_file):
            with open(json_file, 'r') as f:
                info = json.load(f)
        else:
            info = {"nombre": folder, "fotos": []}
        if filename not in info["fotos"]:
            info["fotos"].append(filename)
        with open(json_file, 'w') as f:
            json.dump(info, f, indent=2)

    # Guardar miniatura marcada
    for i, (top, right, bottom, left) in enumerate(locations):
        cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(image_bgr, str(i + 1), (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    output_marca = os.path.join(MARCAS_DIR, filename)
    cv2.imwrite(output_marca, image_bgr)
    print(f"🖼 Miniatura marcada guardada en: {output_marca}")

# Guardar encodings
with open(ENCODINGS_FILE, 'wb') as f:
    pickle.dump((encodings_data, person_folders), f)

print("\n✅ Proceso completado.")
