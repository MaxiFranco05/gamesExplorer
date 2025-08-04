# 🎉 Challenge Amigo Invisible
📌 Breve descripción del proyecto: Este proyecto es una aplicación para jugar al amigo invisible de forma online. Sirve para generar parejas de amigos de manera aleatoria y asegurar que cada persona reciba un regalo sin saber quién es su "amigo invisible".

## ✨ Funcionalidades destacadas
* Generación de parejas de amigos de manera aleatoria
* Asignación de un "amigo invisible" a cada persona
* Posibilidad de establecer un presupuesto para los regalos
* Notificación a cada persona de su "amigo invisible" y del presupuesto establecido

## 🛠️ Tecnologías utilizadas
### Frontend
* HTML
* CSS
* JavaScript
### Backend
* Node.js
* Express.js
* MongoDB
### Herramientas
* GitHub para el control de versiones
* Heroku para el despliegue

## 📁 Estructura del proyecto
```markdown
ChallengeAmigoInvisible-ONE/
│
├── app.js
├── controllers/
│   ├── usuarioController.js
│   └── amigoInvisibleController.js
├── models/
│   ├── usuario.js
│   └── amigoInvisible.js
├── public/
│   ├── index.html
│   └── estilo.css
├── routes/
│   ├── usuarioRoutes.js
│   └── amigoInvisibleRoutes.js
├── package.json
└── README.md
```

## 🚀 Guía de instalación paso a paso
1. Clonar el repositorio con `git clone https://github.com/MaxiFranco05/ChallengeAmigoInvisible-ONE.git`
2. Instalar dependencias con `npm install`
3. Iniciar la aplicación con `node app.js`
4. Abrir el navegador y acceder a `http://localhost:3000`

## 🧪 Cómo usar la app
1. Registrar un nuevo usuario
2. Iniciar sesión con el usuario registrado
3. Establecer un presupuesto para los regalos
4. Generar las parejas de amigos de manera aleatoria
5. Verificar quién es tu "amigo invisible" y el presupuesto establecido

## ⚙️ Consideraciones técnicas
* La aplicación utiliza autenticación y autorización para asegurar que solo los usuarios registrados puedan acceder a la funcionalidad de la aplicación.
* La base de datos es almacenada en MongoDB, lo que permite una escalabilidad fácil y eficiente.
* La aplicación utiliza HTTPS para asegurar la privacidad y seguridad de los datos de los usuarios.

## 📈 Mejoras futuras o ideas en roadmap
* Implementar un sistema de notificaciones para informar a los usuarios de cambios en la aplicación
* Agregar la posibilidad de subir archivos para que los usuarios puedan compartir imágenes o archivos relacionados con los regalos
* Mejorar la interfaz de usuario para hacerla más atractiva y fácil de usar

## 👨‍💻 Autor o colaboradores
Maxi Franco <maxifranco05@gmail.com>

## 📄 Licencia
Este proyecto está bajo la licencia MIT. Puedes ver el archivo LICENSE para más información.