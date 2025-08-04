# gamesExplorer
Una aplicación web para explorar y descubrir nuevos juegos 🎮

## Descripción
gamesExplorer es una plataforma que permite a los usuarios buscar y explorar diferentes juegos, leyendo reseñas y viendo trailers de los mismos. Esta aplicación utiliza PHP, SQL y JavaScript para traer la información desde una base de datos MySQL y mostrarla de manera interactiva en la interfaz web.

## Funcionalidades
*   Buscar juegos por nombre o categoría 🎲
*   Ver reseñas y puntuaciones de cada juego 🤔
*   Ver trailers de los juegos en YouTube 📹
*   Registrarse y loguearse como usuario para personalizar la experiencia 📝

## Tecnologías
*   **PHP**: Utilizado para crear la lógica del lado del servidor y manejar peticiones a la base de datos.
*   **MySQL**: Base de datos relacional utilizada para almacenar información sobre los juegos.
*   **JavaScript**: Utilizado para agregar interactividad en la interfaz web.
*   **CSS**: Utilizado para dar estilo y diseña la interfaz web.
*   **HTML**: Utilizado para crear la estructura de la interfaz web.

## Estructura
La estructura del proyecto es la siguiente:
```markdown
- gamesExplorer/
  - Css/
    - Estilos.css
  - Php/
    - conexion.php
    - mostrarJuegos.php
  - Js/
    - script.js
  - Index.html
  - Loguin.html
  - Register.html
  - buscador.php
  - README.md
```
## Instalación
1.  Clonar el repositorio utilizando `git clone`.
2.  Importar la base de datos MySQL desde el archivo `.sql` proporcionado.
3.  Configurar la conexión a la base de datos en `conexion.php`.
4.  Iniciar el servidor web utilizando `php -S localhost:8080` o cualquier otro método deseado.

## Uso
1.  Abrir el navegador y navegar a `http://localhost:8080` (o la URL configurada).
2.  Buscar juegos por nombre o categoría utilizando el formulario de búsqueda.
3.  Ver reseñas y puntuaciones de cada juego haciendo clic en el juego deseado.
4.  Registrarse y loguearse como usuario para personalizar la experiencia.

## Consideraciones técnicas
*   La seguridad de la aplicación depende de la implementación adecuada de medidas de seguridad en la base de datos y en la lógica del lado del servidor.
*   La optimización del rendimiento es importante para asegurar una experiencia fluida para los usuarios.

## Mejoras futuras
*   Agregar más características para personalizar la experiencia del usuario, como la capacidad de crear listas de juegos favoritos.
*   Mejorar la interfaz web para que sea más atractiva y fácil de usar.
*   Agregar más juegos a la base de datos para que los usuarios tengan más opciones.

## Autor
Maxi Franco

## Licencia
Este proyecto está bajo la licencia MIT. Se puede utilizar, modificar y distribuir libremente. 📄