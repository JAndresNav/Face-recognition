import face_recognition
import pickle
import cv2
import os



TOLERANCIA_RECONOCIMIENTO = 0.6

ENCODINGS_FILE = 'known_faces.pkl'
TEST_FOLDER = 'Test'
SAVE_DIR = 'caras_detectadas'

# Cargar encodings conocidos
with open(ENCODINGS_FILE, 'rb') as f:
    known_encodings, known_names = pickle.load(f)

os.makedirs(SAVE_DIR, exist_ok=True)

for filename in os.listdir(TEST_FOLDER):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    IMAGE_PATH = os.path.join(TEST_FOLDER, filename)
    print(f"\n📸 Procesando: {filename}")

    image = face_recognition.load_image_file(IMAGE_PATH)
    locations = face_recognition.face_locations(image)
    encodings = face_recognition.face_encodings(image, locations)
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    personas_en_la_foto = set()

    for face_encoding, face_location in zip(encodings, locations):
        distances = face_recognition.face_distance(known_encodings, face_encoding)

        name = "Desconocido"
        if len(distances) > 0 and min(distances) < TOLERANCIA_RECONOCIMIENTO:
            match_index = int(distances.argmin())
            name = known_names[match_index]

        top, right, bottom, left = face_location
        cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(image_bgr, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        personas_en_la_foto.add(name)

    for persona in personas_en_la_foto:
        folder = os.path.join(SAVE_DIR, persona)
        os.makedirs(folder, exist_ok=True)
        count = len(os.listdir(folder)) + 1
        new_filename = os.path.join(folder, f"{count}_{filename}")
        cv2.imwrite(new_filename, image_bgr)
        print(f"✔ Guardado en: {new_filename}")

print("\n✅ Todas las imágenes procesadas.")
