import face_recognition
import os
import pickle

KNOWN_FACES_DIR = 'people_photos'
ENCODINGS_FILE = 'known_faces.pkl'

known_encodings = []
known_names = []

for person_name in os.listdir(KNOWN_FACES_DIR):
    person_path = os.path.join(KNOWN_FACES_DIR, person_name)
    if not os.path.isdir(person_path):
        continue

    print(f"\n📂 Procesando: {person_name}")

    for filename in os.listdir(person_path):
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        image_path = os.path.join(person_path, filename)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person_name)
            print(f"✔ Encoding añadido: {filename}")

# Guardar encodings
with open(ENCODINGS_FILE, 'wb') as f:
    pickle.dump((known_encodings, known_names), f)

print("\n✅ known_faces.pkl generado correctamente.")
