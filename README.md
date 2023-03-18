# Tercera-pre-entrega-Valfosca.



◘◘ Breve descripcion del proyecto
    - Proyecto Web Django con patrón MTV 
    - Crear una Pagina con formularios para cada una de 4 clases, posibilitando agregar nuevos registros desde cada una de ellas y 
    permitiendo realizar una busqueda por algunos de sus campos mediante otro formulario. 
    


◘◘ Abrir el proyecto en un repositorio local   
   
• Para correr este proyecto se necesita Python 3.10 o superior y el framework Djando

• Instalar Django

      -pip install django
           
• Abrir Vs code y crear una carpeta donde se alojara el repositorio

• Abrir una terminal bash/cmd/powershell y correr

      -git clone (link nombre de la url del repositorio creado en github) .  <---  se clona lo que este en el repositorio no olvidarse 
      del "espacio" y del "pto", hace que no se genere otra carpeta dentro de la general creada.
      
      -python manage.py migrate  <---  para realizar la creacion de las tablas de la bd
                    
       
◘◘ Crear un repositorio desde Cero

• Crear un repositorio en Gighub

      -Debemos ir a arriba a la derecha donde tenemos nuestra sesion iniciada y vamos a ver un mas, cliqueamos ahi y en new repositorio

      -Agregamos el nombre que se le quiera dar, siempre y cuando este disponible.

      -Se tilda la opcion de agregar archivo readme.

      -Buscar la opcion .gitignore y elegir python  <--- esto hace que cuando estemos trabajando y querramos enviar lo creado de manera 
      local no guarde archivos basura y tampoco la base de datos creada con la que trabajamos en el local.

      -Crear repositorio
      
• Abrir Vs code y crear una carpeta donde se alojara el repositorio      
    
• Correr los siguientes comandos en la terminal (pueden variar de un sist operativo a otro) bash en windows
    
      -django-admin starproject (nombre del proyecto) .  <---  creacion de la carpeta del proyecto

      -python manage.py startapp (nombre de la app) .  <---  creacion de la carpeta de la app
      
      
◘◘ Correr el servidor

      -python manage.py runserver   <---  se genera por defecto en esta direccion http://127.0.0.1:8000/
      
      
◘◘ Si se modifica algun modelo 

      -python manage.py makemigrations  <---  para detectar los cambios y generar los scripts para actualizar y modificar la bd
      -python manage.py migrate   <---  corre los scripts y crea/modifica la tabla de la bd
      
      
◘◘ Crear un administrador

• Desde la terminal bash en windows para crear un super-usuario

      -python manage.py createsuperuser --username (nombre del administrador)
      -Ingresar Email y Password(el cursor no se mueve y no se registra tipeo por seguridad, parece que no funciona) y una verificacion
      del Password
      
      
◘◘ Utilizar archivo de prueba de carga de datos

• Usar el archivo seed_data.py

• Desde terminal bash en windows

      -python manage.py shell < seed_data.py

• Desde terminal powershell

      -python manage.py shell

• Dentro del shell hacer
          
       -import seed_data
      
     
◘◘ Comandos de Git

         -git clone (link nombre de la url del repositorio creado en github) .    <---  se clona lo que este en el repositorio remoto,
         no olvidarse del "espacio" y del "pto", hace que no se genere otra carpeta dentro de la general creada.

         -git branch -m (nombre rama)   <---  cambiar nombre de la rama que fuimos creando a lo largo del proyecto

         -git log  <---  para ver los commit q tengo, todos los ptos de recuperacion q fuimos creando a lo largo de la vida de nuestro 
         proyecto

         -git status    <---  nos muestra cuales archivos estan siendo seguidos para ser versionados, como tambien los q no y ademas 
         las modificaciones, creaciones o borrados del contenido hasta ahora
         
          -git checkout  (nombre de la rama)  <---  permite movernos en las disitntas versiones del codigo, ir a una rama en particular
         
         -git checkout -b (nombre-de-tu-rama)  <---  crear una rama nueva y movernos a ella directamente
         
         -git branch -d (nombre rama) / git branch --delete (nombre rama)  <---  borra una rama

         -history te muestra todos los comandos que se usaron en esa sesion

         -git merge (nombre de la rama q se quiere fusionar)  <---  fusiona una rama con otra agregandole los ptos de commit que tiene 
         y las modificacioens que se hicieron, pararse en la rama a la que se le quiere fusionar la otra 

         -git reset –hard (codigo alfanunerico commit)  <---  elimina los commit que estan arriba de ese pto de recuperacion no hay 
         vuelta atras si se usa este comando

         -git add .   <---  hace que toda modificacion creacion o borrado o archivo que no esta siendo seguido se agregue para el 
         proximo commit
         
         -git add (nombre del archivo)   <---  para agregar solo un archivo al stagging 
         
         -git commit -m "mensaje de descripcion de lo q se hizo"   <---  se crea un pto seguro de todo lo que se agrego anteriormente
         
         -git remote -vv  <---  para ver en que directorio estoy
         
         -git push origin (nombre rama)  <---  para enviar solo la rama donde estoy parado de mi repositorio local al remoto

         -git push --all origin  <---  sube todas las ramas con todos los commits que tiene cada uno al repositorio remoto de GitHub
         
         -git pull   <---  para enviar desde el repositorio remoto alguna actualizacion del codigo que no esta en nuestro repositorio 
         local                 
