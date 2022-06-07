# Proyecto final - Blog - Gianluca Consolini

## **Información sobre el blog**

Se trata de un blog sobre la marca Mikrotik (dedicada a hardware y software) desarrollado en Python con el framework Django, donde se realizan post de diferentes noticias, novedades o guías acerca de dicho equipamiento. Al blog puede acceder cualquier usuario no registrado para leer los post's, pero para crear o editar uno es necesario haber ingresado. 

Los usuarios del post una vez registrados, pueden acceder también a un chat global (donde se indican noticias o se realizan preguntas sobre el blog), editar su perfil de usuario, cambiar su contraseña y como se menciono anteriormente crear o editar un post (si fue el mismo usuario que lo creo). En cambio, el único usuario que puede asignar un avatar a cada usuario es el admin desde su web de administración, y también es el único que cuenta con la posibilidad de eliminar un post de cualquier usuario.

**_Sepan disculpar la estética de la web, cuento con casi nulos conocimientos acerca de CSS, HTML o JS._**

**Video explicativo del funcionamiento**

[![Alt text](https://img.youtube.com/vi/P6H90I4M1uE/0.jpg)](https://www.youtube.com/watch?v=P6H90I4M1uE)

***

## **Partes del blog**

### **Barra de navegación / Navbar**
Desde dicha barra el usuario tendrá la posibilidad de ingresar al listado de post, al apartado de about me, al chat global, dirigirse al home del blog, de loguearse o desloguearse de la página, crear su usuario, ver un listado de usuarios de la página (únicamente  el admin tiene esa posibilidad) o de visualizar su perfil. A continuación, se mostrará una comparativa de que opciones para cada usuario.

- Usuario no registrado

![Navbar-no-regis](https://user-images.githubusercontent.com/98831807/172289047-817077fe-0394-4727-be0e-44574538f4cd.PNG)

- Usuario registrado

![Navbar-user](https://user-images.githubusercontent.com/98831807/172289076-2c059f63-b843-47d3-bc59-3adfb302372e.PNG)

- Usuario admin

![Navbar-admin](https://user-images.githubusercontent.com/98831807/172289116-e01ff253-0f3c-4684-99ac-3490d4e56c9b.PNG)


### **Home**
En esta página se da una breve descripciónn del blog, la posibilidad de dirigirse al listado de los post's, de crear un post o de ingresar al chat global. También tocando en la imagen con el logo de Mikrotik nos dirigiremos a la web oficial de dicha empresa.

![Home](https://user-images.githubusercontent.com/98831807/172289491-ef2161f3-2bdf-4d4d-8da9-d4d7e4114d5f.PNG)

### **About Me**
En esta página hablo acerca de mi y de lo que me apasiona, también un breve resumen de porque elegí a Mikrotik.

![About-me](https://user-images.githubusercontent.com/98831807/172289521-cf43ba4c-d9d2-4cf1-b504-b029d6514a70.PNG)

### **Chat**
Un chat global (*entre los usuarios del blog*) donde cada usuario puede enviar un mensaje con consultas, dudas o ideas para el blog.

![Globalchat](https://user-images.githubusercontent.com/98831807/172290263-f22096f0-5d34-40fb-b2f7-1589b616abb9.PNG)

### **Blog**

Acá veremos en primer lugar un listado de los post's y la posibilidad de realizar una búsqueda por el título del post, también se ve un breve resumen de dicho post y de ingresar a ver el post completo. Una vez ingresado al post completo, y registrado, se cuenta con la posibilidad de editarlo (siempre y cuando seamos el autor del mismo). *Únicamente el admin puede eliminar un post.*

Cada post esta compuesto por un título, un subtitulo, un cuerpo y una imagen sobre el tema.

- Listado de post's

![Post-list](https://user-images.githubusercontent.com/98831807/172289556-d1fc68d8-9a1d-411b-b027-fe063e9252dd.PNG)

- Post detallado

![Post-detail](https://user-images.githubusercontent.com/98831807/172289567-c4594a8a-2151-4b35-bee1-30e6ae35504c.PNG)

### **Información del usuario**
Desde este apartado vemos la información del usuario, su avatar (*si el admin no asigno ningún avatar se verá uno por defecto*) y la posibilidad de realizar un cambio de contraseña o editar la información del usuario.

![User-detail](https://user-images.githubusercontent.com/98831807/172289786-be28d44d-f321-478e-adbf-f66c8818b5b8.PNG)

- Cambio de contraseña

![Passwd](https://user-images.githubusercontent.com/98831807/172289894-2a0f5222-f710-46cf-bd2f-a0a28d492fe0.PNG)

- Actualizar información

![Edit](https://user-images.githubusercontent.com/98831807/172289929-5dbea4b4-0fd2-448d-acd9-cda2ae4b43a9.PNG)

### **Singup**
En esta página un usuario no registrado puede crear una cuenta para acceder al blog

![Registrarse](https://user-images.githubusercontent.com/98831807/172289753-733df989-6f1e-47d6-bb9e-5574797ba5d1.PNG)

### **Login / Logout**
Como indica el nombre desde aquí se puede ingresar al blog (con las credenciales validad de un usuario) o de salir de dicho blog.

### **User**
Desde aquí el admin puede visualizar la información sobre cada usuario registrado.

![User](https://user-images.githubusercontent.com/98831807/172289726-eca84b8d-cc02-4843-925b-aae6e435cdb4.PNG)

***

## **Funcionamiento para prueba**
Para poder correr este blog es necesario tener instalados las dependencias de Django y de Ckeditor, las mismas las podemos instalar de la siguiente manera:

- pip install django
- pip install django-ckeditor

Ahora utilizaremos el programa Visual Studio Code con la extensión de Python para pdoer correr el blog, ingresamos a la carpeta Blog mediante el comando cd. Una vez dentro corremos los comandos **python manage.py makemigrations** y **python manage.py makemigrations** para generar la base de datos, creamos nuestro usuario de administrador mediante **python manage.py createsuperuser** y para finalizar corremos el servidor para poder utilizar el programa (lo haecmos con **python manage.py runserver**).

Ahora debera ingresar a [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para visualizar el blog o a [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) para el panel de administracion.
