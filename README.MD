# Integrar plantilla AdminLTE 3.0.1 a un proyecto Django 2.2 

Es un intento de integrar la plantilla AdminLTE 3.0.1 a un proyecto Django 2.2.

Éste proyecto me sirve de base para futuros iniciativos en Django. 


### Qué conforma éste proyecto?

 * [Django 2.2](https://www.djangoproject.com/)
 * [AdminLTE 3.0.1](https://adminlte.io)
 * Repositorio Git en Github


### Características?

La primera fase es:

 * Una Django App con plantilla integrada
 * Login y Logout usando Django standard
 * Catálogo de ejemplo: City History

### Catálogo de Ejemplo: City History

La Django app se llama ```city_history```.

Los casos son muy simples:
 1. Usuario se identifica.
 2. Usuario puede crear un país.
 3. Usuario puede crear una ciudad, la cual esta ligada a un país.
 4. Usuario puede crear un hecho (fact), ligada a una ciudad.
 5. Usuario puede crear un Punto de interes por visitar (point of interest to visit) ligada a una ciudad.


### Postgres

References:
* [hub.docker.com/postgres](https://hub.docker.com/_/postgres)
* [Amigoscode - Docker and PostgreSQL in [10 Minutes]](https://youtu.be/aHbE3pTyG-Q)
* [How to setup PostgreSQL on MacOS](https://www.robinwieruch.de/postgres-sql-macos-setup)
* [Getting Started with PostgreSQL on Mac OSX](https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb)
* [Django with Docker: Add Postgres](https://rayed.com/posts/2018/01/django-with-docker-add-postgres/)

#### Instalando Postgresql con Homebrew

Una alternativa viable es instalar postgres utilizando Homebrew.
```bash
$ brew install postgresql
Updating Homebrew...
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> Deleted Formulae
docker-cloud

==> Downloading https://homebrew.bintray.com/bottles/postgresql-12.1.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/30/309377407d7cb766d238f063c10210c4e48d48fcdadd62560346c2d4af782bc4?__gda__=exp=1576221171~hmac=d6185c86503fe6d0
######################################################################## 100.0%
==> Pouring postgresql-12.1.catalina.bottle.tar.gz
==> /usr/local/Cellar/postgresql/12.1/bin/initdb --locale=C -E UTF-8 /usr/local/var/postgres
==> Caveats
To migrate existing data from a previous major version of PostgreSQL run:
  brew postgresql-upgrade-database

To have launchd start postgresql now and restart at login:
  brew services start postgresql

Or, if you don't want/need a background service you can just run:
  pg_ctl -D /usr/local/var/postgres start
  
==> Summary
🍺  /usr/local/Cellar/postgresql/12.1: 3,217 files, 37.7MB
==> `brew cleanup` has not been run in 30 days, running now...
Removing: /Users/gerardo/Library/Caches/Homebrew/composer--1.9.0.phar... (1.8MB)
Removing: /Users/gerardo/Library/Caches/Homebrew/curl-openssl--7.66.0.mojave.bottle.tar.gz... (1MB)
Removing: /Users/gerardo/Library/Caches/Homebrew/glib--2.62.2.mojave.bottle.tar.gz... (4.5MB)
Removing: /Users/gerardo/Library/Caches/Homebrew/libidn2--2.2.0_1.mojave.bottle.tar.gz... (224.5KB)
Removing: /Users/gerardo/Library/Caches/Homebrew/libpq--11.5_1.mojave.bottle.tar.gz... (5.4MB)
Removing: /Users/gerardo/Library/Caches/Homebrew/libtiff--4.0.10_1.mojave.bottle.tar.gz... (1MB)
Removing: /Users/gerardo/Library/Caches/Homebrew/nghttp2--1.39.2_1.mojave.bottle.tar.gz... (947.8KB)
Removing: /Users/gerardo/Library/Caches/Homebrew/nginx--1.17.3_1.mojave.bottle.tar.gz... (1.2MB)
Removing: /Users/gerardo/Library/Caches/Homebrew/php--7.3.11.mojave.bottle.tar.gz... (19.9MB)
Removing: /Users/gerardo/Library/Caches/Homebrew/python--3.7.4_1.mojave.bottle.1.tar.gz... (14.7MB)
Removing: /usr/local/Cellar/readline/8.0.0_1... (48 files, 1.5MB)
Removing: /Users/gerardo/Library/Caches/Homebrew/sqlite--3.29.0.mojave.bottle.tar.gz... (1.9MB)
...
Pruned 0 symbolic links and 15 directories from /usr/local

```

```bash
# check postgres version:
$ postgres --version
postgres (PostgreSQL) 12.1

# Now you can initialize the physical space on your hard-disk to allocate databases. To do this, create a default postgres database on the command line in case it didn't happen automatically:
$ initdb /usr/local/var/postgres
....
initdb: error: directory "/usr/local/var/postgres" exists but is not empty
....
# You will see the error message: "initdb: directory "/usr/local/var/postgres" exists but is not empty" if the database was already created when you installed PostgreSQL. It means the folder where you are attempting to create a physical place for the database already has one. Either way, next you can move on to the next step.
```


##### Credenciales ejemplo
 * Usuario: user_djangoadminlte
 * Contraseña: pepito_cabron (ejemplo)
 * Base de datos: db_djangoadminlte



Iniciar y Detener postgres:
```bash
$ pg_ctl -D /usr/local/var/postgres start
$ pg_ctl -D /usr/local/var/postgres stop
```

##### Comandos postgress:

https://www.postgresqltutorial.com/psql-commands/

```bash
$ select version();
\d employees
\dn
\dt
\l
\c mvp_employees gerardo;
```


##### Configurando postgres:
```bash
$ psql postgres
psql (12.1)
Type "help" for help.

postgres=# 

# Listar que usuarios existen en servidor:
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 gerardo   | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

# existe gerardo en lugar de postgres!! 
# esto no lo sabia, es interesante la razon
# cuando se instalo, se genero un rol (usuario) con el nombre
# del usuario en sesion, y por eso puedo hacer psql postgres, sin mas

# crear role:
postgres=# CREATE ROLE user_djangoadminlte WITH LOGIN PASSWORD 'pepito_cabron';
CREATE ROLE
postgres=# \du
                                        List of roles
      Role name      |                         Attributes                         | Member of 
---------------------+------------------------------------------------------------+-----------
 gerardo             | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 user_djangoadminlte |                                                            | {}


# usuario no tiene ningun privilegio otro que entrar, asignar un privilegio:
postgres=# ALTER ROLE user_djangoadminlte CREATEDB;
ALTER ROLE
postgres=# \du
                                        List of roles
      Role name      |                         Attributes                         | Member of 
---------------------+------------------------------------------------------------+-----------
 gerardo             | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 user_djangoadminlte | Create DB                                                  | {}
```

Otro modo de crear el usuario seria:
```bash
$ createuser user_djangoadminlte --createdb
# pero no hay comando desde bash para otros comandos ALTER
```



Crear database:

Existen un par de modos. Veamos:

```bash
$ psql postgres -U user_djangoadminlte -W
postgres=> CREATE DATABASE db_djangoadminlte;
CREATE DATABASE

# al menos un usuario deberia tener acceso a dicha base de datos
postgres=> GRANT ALL PRIVILEGES ON DATABASE db_djangoadminlte TO user_djangoadminlte;
GRANT
postgres=> \l # lists all the databases in Postgres
                                                 List of databases
       Name        |        Owner        | Encoding | Collate | Ctype |              Access privileges              
-------------------+---------------------+----------+---------+-------+---------------------------------------------
 db_djangoadminlte | user_djangoadminlte | UTF8     | C       | C     | =Tc/user_djangoadminlte                    +
                   |                     |          |         |       | user_djangoadminlte=CTc/user_djangoadminlte
 postgres          | gerardo             | UTF8     | C       | C     | 
 template0         | gerardo             | UTF8     | C       | C     | =c/gerardo                                 +
                   |                     |          |         |       | gerardo=CTc/gerardo
 template1         | gerardo             | UTF8     | C       | C     | =c/gerardo                                 +
                   |                     |          |         |       | gerardo=CTc/gerardo
(4 rows)

# conectar a la base de datos:
postgres=> \connect db_djangoadminlte # connect to a specific database
Password for user user_djangoadminlte: 
You are now connected to database "db_djangoadminlte" as user "user_djangoadminlte".
db_djangoadminlte=> \dt # list the tables in the currently connected database
Did not find any relations.
```

Otro modo de crearla desde la bash:
```bash
$ createdb db_djangoadminlte -U user_djangoadminlte
```



```bash
$ createdb mydatabasename
$ dropdb mydatabasename

# Conectar a la bd:
$ psql mydatabasename

# he command leads you to the psql shell, which you can exit by typing CTRL + d. In the psql shell, you can create and drop databases as well:
CREATE DATABASE mydatabasename;
DROP DATABASE mydatabasename;

# To list all your databases, you can type \list. Your will see any new databases listed, as well as two default databases that come with postgreSQL called template0 and template1. The templates should remain in your database list even if you aren't using them, as they may be useful later.

    \list - List all of your actual databases.
    \c mydatabasename - Connect to another database.
    \d - List the relations of your currently connected database.
    \d mytablename - Shows information for a specific table.
```


#### Postgresql y Docker

```bash
$ docker pull postgres:12.1-alpine
...
Status: Downloaded newer image for postgres:12.1-alpine
docker.io/library/postgres:12.1-alpine
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
postgres            12.1-alpine         c8abd8e13a5c        9 days ago          146MB
$ docker run --name postgres-djangoadminlte -e POSTGRES_PASSWORD=pepito_cabroncito -d -p 5432:5432 postgres:12.1-alpine
7088e9f942b87a6638d3eaedcfdb96ef7a28d7ba3117f77cd7ace8929e75b1e4
$ docker ps
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                    NAMES
7088e9f942b8        postgres:12.1-alpine   "docker-entrypoint.s…"   45 seconds ago      Up 45 seconds       0.0.0.0:5432->5432/tcp   postgres-djangoadminlte
```

Ahora ya podria hacer bash en el container postgres. En Docker es para ahorrar instalar Postgres entero.
```bash
$ docker ps
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                    NAMES
7088e9f942b8        postgres:12.1-alpine   "docker-entrypoint.s…"   2 minutes ago       Up 2 minutes        0.0.0.0:5432->5432/tcp   postgres-djangoadminlte
Gerardos-MacBook-Pro-2:django-adminlte gerardo$ docker exec -it postgres-djangoadminlte bash
bash-5.0# 
bash-5.0# pwd
/
bash-5.0# ls
bin                         home                        opt                         sbin                        usr
dev                         lib                         proc                        srv                         var
docker-entrypoint-initdb.d  media                       root                        sys
etc                         mnt                         run                         tmp
bash-5.0# psql
psql: error: could not connect to server: FATAL:  role "root" does not exist
bash-5.0# psql --help # busca por como pasar el username

# el usuario postgres es el que normalmente deberias usar en modo local
bash-5.0# psql -U postgres
psql (12.1)
Type "help" for help.

postgres=#
```

Otro modo de entrar:
```bash
$ docker run -it --rm --network some-network postgres psql -h some-postgres -U postgres
```


En esa shell ya podemos trabajar con docker normal.
```bash
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

postgres=# create database test;
CREATE DATABASE
postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 test      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
(4 rows)

postgres=# \c test
You are now connected to database "test" as user "postgres".
test=# \d
Did not find any relations.
test=# 
```

Ahora ya podria conectarme si tuviera psql instalado del siguiente modo:
```bash
$ psql -h localhost -p 5432 -U postgres
Password for user postgres: # usar password del docker container: pepito_cabroncito
postgres=#
```

Borrar todo despues:
```bash
$ docker volume rm $(docker volume ls -q)

# el modo correcto de borrar todo seria:
$ docker rm -f -v postgres_container_name
```

Extras [referencia](https://stackoverflow.com/questions/43618517/docker-postgress-clear-all-data):
```bash
$ docker kill $(docker ps -q) # stop all containers
$ docker rm $(docker ps -a -q) # remove all containers 
$ docker rmi $(docker images -q) # remove all images
$ docker network prune # remove all networks
$ docker volume prune # remove all volumes 
```


### Acciones para levantar proyecto demo

Utilizaré postgresql (podrías usar MySQL también, _pero no MSSQL_). Entonces, necesitamos crear usuario y una base de datos.

> Recuerda anotar en un papel aparte usuario, su password y nombre de la base de datos a conectar.

 * Usuario: user_djangoadminlte
 * Contraseña: _
 * Base de datos: db_djangoadminlte


#### Probar conexión a la base de datos:
Probar conexión a la base de datos:
```bash
$ sudo -u postgres psql
```

#### Crear usuario postgres
 
Crear usuario postgres:
```bash
$ sudo -u postgres createuser -e -E -s -h 127.0.0.1 -p 5432 -U postgres -W -P user_djangoadminlte
Enter password for new role: 
Enter it again: 
Password: 
SELECT pg_catalog.set_config('search_path', '', false);
CREATE ROLE user_djangoadminlte PASSWORD 'md5a131afbf8f28881ddbbd21ee72e564f1' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;


# quitar rol SuperUser al usuario de ser necesario
#$ ALTER ROLE user_djangoadminlte WITH NOSUPERUSER;
```

#### Crear base de datos:
Crearla mediante conexion SQL Script en psql ó ```createdb``` (preferida):

```bash
$ sudo -u postgres psql -h 127.0.0.1 -U user_djangoadminlte -d postgres -W -p 5432
Password: 
psql (12.1 (Ubuntu 12.1-1.pgdg18.04+1), server 10.11 (Ubuntu 10.11-1.pgdg18.04+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

$ CREATE DATABASE db_djangoadminlte WITH OWNER = user_djangoadminlte ENCODING = 'UTF8' CONNECTION LIMIT = -1;
```

Crearla mediante programa createdb de postgres:
```bash
$ sudo -u postgres createdb -h 127.0.0.1 -p 5432 -O user_djangoadminlte -U user_djangoadminlte -W -e db_djangoadminlte
Password: 
SELECT pg_catalog.set_config('search_path', '', false);
CREATE DATABASE db_djangoadminlte OWNER user_djangoadminlte;
```

#### Correr migraciones de base de datos

```bash
$ python manage.py makemigrations
$ python manage.py showmigrations
$ python manage.py migrate
```


### Comandos utiles git

```bash
$ git branch
$ git checkout master
$ git checkout -b 09_countries_crud
$ git merge 09_countries_crud
$ git push origin <branch>
$ git push origin --all
$ git branch -d ch_countries_crud
```


Cosas que podrían incluirse en fases posteriores:
 * Custom User authentication schema
 * REST API

[Sugerencias?](https://twitter.com/gpalazuelosg)
