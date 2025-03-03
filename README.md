# 🎮 GamesExplorer

GamesExplorer es un paquete en Python diseñado para explorar y gestionar información sobre juegos en diferentes plataformas. Actualmente, se enfoca en la integración con Steam, proporcionando herramientas para interactuar con datos de juegos.

## 📌 Características
- 📦 Módulos organizados para la gestión de juegos y plataformas.
- 🚀 Soporte para la API de Steam.
- ✅ Sistema de utilidades para facilitar la manipulación de datos.
- 🧪 Pruebas unitarias incluidas en la carpeta `tests/`.

## 📂 Estructura del Proyecto
```
proyecto1/
│
├── gamesExplorer/        # Paquete principal
│   ├── plataformas/      # Módulo para diferentes plataformas
│   │   ├── steam/        # Implementación para Steam
│   │   │   ├── __init__.py
│   │   │   ├── steam.py
│   │   │   ├── utils.py
│   ├── __init__.py
│   ├── manager.py        # Gestión general de juegos
│
├── tests/                # Pruebas unitarias
│   ├── steam_test.py
│
├── setup.py              # Configuración para empaquetado
└── README.md             # Documentación del proyecto
```

## 🚀 Instalación
Puedes instalar este paquete de manera local ejecutando:

```sh
pip install -e .
```

Esto permitirá que puedas importarlo y probarlo sin necesidad de reinstalar tras cambios en el código.

## 🔧 Uso
Ejemplo de cómo importar y utilizar `GamesManager`:

```python
from gamesExplorer.manager import GamesManager

manager = GamesManager()
manager.list_games()
```

## 🛠 Desarrollo
Si deseas contribuir o modificar el código, sigue estos pasos:

```sh
git clone https://github.com/MaxiFranco05/gamesExplorer.git
cd gamesExplorer
pip install -r requirements.txt  # Si hay un archivo de dependencias
```

Ejecuta las pruebas con:

```sh
pytest tests/
```

## 📜 Licencia
Este proyecto se distribuye bajo la licencia MIT. ¡Siéntete libre de contribuir! 🎉

