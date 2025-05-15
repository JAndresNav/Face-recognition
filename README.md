
# Face Grouping and Recognition System

This project allows you to automatically detect and group faces from images, either by **facial similarity** (like Google Photos) or by **known individuals** using pre-labeled encodings. It works with group or individual photos and organizes them into folders per person.

---

## Folder Structure

```
Face recognition
v1
└──┬── caras_detectadas/           # Output: recognition by known names
   ├── people_photos/              # Folders to be procesed (pre labeled encoding)
   ├── Test/                       # Photos to match with known people (people_photos/) (input)
   ├── Agrupar_por_cara.py         # Script (see next section)
   ├── Borrar caras detectadas.py  # Script (see next section)
   └── known_faces.pkl             # Encodings of known people (people_photos/) (ignore)
v2
└──┬── Fotos/                      # Individual or group photos to be processed (input)
   ├── miniaturas_marcadas/        # Copies of images with numbered face boxes (helps for testing)
   ├── personas_agrupadas/         # Output: grouped by facial similarity
   ├── encodings_autodetectados.pkl  # Auto-learned encodings (ignore)
```

---

## Scripts

### 1. Group by known people
**File:** `Agrupar_por_carpeta.py`

- Uses `known_faces.pkl` for labeled encodings
- Compares photos in `Test/`
- If someone is recognized, saves full photo in `caras_detectadas/Name/`

```bash
  Agrupar_por_carpeta.py
```
---


###  2. Clear detected face results (known people)
**File:** `Borrar caras detectadas.py`

- Deletes all images in `caras_detectadas/`, but keeps the name folders

```bash
  Borrar\ caras\ detectadas.py
```


---

###  3. Group by face (no names needed)
**File:** `Agrupar_por_cara.py`

- Detects and compares faces in `Fotos/`
- Saves whole photo in each person's folder based on facial similarity
- Draws numbered boxes for each detected face and saves in `miniaturas_marcadas/`

```bash
  Agrupar_por_cara.py
```
---


### 4. Clear grouped folders and thumbnails
**File:** `Limpiar_personas_agrupadas.py`

- Deletes all folders and photos inside `personas_agrupadas/` and `miniaturas_marcadas/`

```bash
  Limpiar_personas_agrupadas.py
```

---

## Adjustable Parameters

### Face recognition tolerance
Inside `Agrupar_por_cara.py` and `Agrupar_por_carpeta.py`:

```python
TOLERANCE = 0.6
```

| Value       | Description                          |
|-------------|--------------------------------------|
| 0.45 – 0.55 | Very strict (needs near identical faces) |
| 0.58 – 0.62 | Balanced (recommended)               |
| 0.65 – 0.7  | Loose tolerance (might misidentify)  |

---

##  How to Test


### Recognize known people

1. Place images to train the model in `people_photos/` 
2. Place test images in `Test/`
3. Run:

```bash
   Agrupar_por_carpeta.py
```

4. Results saved in `caras_detectadas/Name/`
---


### Group automatically (unsupervised)

1. Place photos inside `Fotos/`
2. Run:

```bash
   Agrupar_por_cara.py
```

3. Check results inside `personas_agrupadas/` and thumbnails in `miniaturas_marcadas/`
---

## Requirements

```bash
pip install face_recognition opencv-python
```

> On Windows, you may need:
> - [CMake](https://cmake.org/)
> - [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

---

## Extra Tips

- Use clear images with visible faces.
- You can improve detection by changing:

```python
model='hog'  →  model='cnn' // It will take longer to process
```
