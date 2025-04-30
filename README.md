# 🚀 quickpkg  
**Paquete Python distribuido vía GitHub Releases**  
✨ Versión ligera para aprender empaquetado y distribución de módulos Python  

---

## 📦 Descripción  
Paquete demostrativo que incluye:  
- ✅ Estructura básica de paquete PIP  
- 📦 Configuración de `setup.py`  
- 🚀 Publicación en GitHub Releases  
- 🔄 Instalación desde archivo `.whl`  

**Función principal**:  
```python
saludar(nombre)  # Retorna un saludo personalizado
```

---

## 🔧 Instalación Rápida
Puedes instalar directamente el paquete desde la sección de [Releases](https://github.com/LionelMc/projPractice---quickpkg/releases):

```bash
pip3 install https://github.com/LionelMc/projPractice---quickpkg/releases/download/v0.1.0/quickpkg-0.1.0-py3-none-any.whl
```

---

## 🧪 Probar el Paquete
Sigue estos pasos para probar el paquete en un entorno limpio:

### 1. Configurar entorno virtual
```bash
python3 -m venv venv           # Crea el entorno virtual
source venv/bin/activate       # Actívalo (Linux/Mac)
venv\Scripts\activate          # Windows
```

### 2. Instalar el paquete
```bash
pip install https://github.com/LionelMc/projPractice---quickpkg/releases/download/v0.1.0/quickpkg-0.1.0-py3-none-any.whl
pip list | grep quickpkg       # Verificar: deberías ver "quickpkg 0.1.0"
```

### 3. Ejecutar la aplicación de prueba
```bash
cd app                         # Navega a la carpeta de la app
python3 app.py                 # Ejecuta el script
# Salida esperada: "Hola Lio, este es mi primer paquete pip!"
```

### 4. Desactivar el entorno
```bash
deactivate  # Ejecutar cuando termines de trabajar
```

---

### 📝 Nota:
- **app.py**: Debe contener el código que usa el paquete:

```python
from quickpkg import saludar
print(saludar("Lio"))  # Reemplaza "Lio" con tu nombre.
```