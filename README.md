# 🎮 Games Explorer
📌 Breve descripción del proyecto: Games Explorer es una aplicación web diseñada para explorar y descubrir nuevos juegos de diferentes plataformas. Permite a los usuarios buscar, filtrar y obtener información detallada sobre juegos, incluyendo descripciones, imagenes, y enlaces a tiendas en línea.

## ✨ Funcionalidades destacadas
* Búsqueda de juegos por título, género o plataforma
* Filtrado de resultados por popularidad, fecha de lanzamiento o calificación
* Información detallada sobre cada juego, incluyendo:
 + Descripciones y sinopsis
 + Imágenes y trailers
 + Enlaces a tiendas en línea para comprar o descargar el juego
* Posibilidad de agregar juegos a una lista de favoritos para acceder rápidamente

## 🛠️ Tecnologías utilizadas
### Frontend
* **HTML5**: Estructura y contenido de la página web
* **CSS3**: Estilos y diseño visual
* **JavaScript**: Funcionalidad interactiva y lógica de la aplicación
* **React**: Biblioteca para construir interfaces de usuario
### Backend
* **Node.js**: Entorno de ejecución para JavaScript en el servidor
* **Express**: Framework para crear aplicaciones web
* **MongoDB**: Base de datos NoSQL para almacenar información de juegos
### Herramientas
* **GitHub**: Control de versiones y colaboración
* **npm**: Gestor de paquetes para Node.js

## 📁 Estructura del proyecto
```markdown
gamesExplorer/
├── client/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── containers/
│   │   ├── actions/
│   │   ├── reducers/
│   │   ├── index.js
│   ├── package.json
├── server/
│   ├── app.js
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── package.json
├── README.md
├── LICENSE
```

## 🚀 Guía de instalación paso a paso
1. Clonar el repositorio: `git clone https://github.com/MaxiFranco05/gamesExplorer.git`
2. Instalar dependencias en el cliente: `cd client && npm install`
3. Instalar dependencias en el servidor: `cd server && npm install`
4. Iniciar el servidor: `cd server && npm start`
5. Iniciar el cliente: `cd client && npm start`
6. Abrir el navegador y acceder a `http://localhost:3000`

## 🧪 Cómo usar la app
1. Buscar juegos por título, género o plataforma
2. Filtrar resultados por popularidad, fecha de lanzamiento o calificación
3. Ver información detallada sobre un juego
4. Agregar juegos a la lista de favoritos
5. Acceder a la lista de favoritos y jugar

## ⚙️ Consideraciones técnicas
* **Seguridad**: La aplicación utiliza HTTPS para cifrar la comunicación entre el cliente y el servidor
* **Almacenamiento**: La base de datos MongoDB almacena información de juegos y usuarios
* **Rendimiento**: La aplicación utiliza técnicas de caching y optimización para mejorar el rendimiento

## 📈 Mejoras futuras o ideas en roadmap
* Agregar más plataformas de juego
* Implementar autenticación de usuarios
* Crear un sistema de recomendaciones de juegos
* Mejorar la búsqueda y filtrado de juegos

## 👨‍💻 Autor o colaboradores
* **Maxi Franco**: Desarrollador y creador del proyecto

## 📄 Licencia
Este proyecto está licenciado bajo la licencia **MIT**. Ver [LICENSE](LICENSE) para más información.