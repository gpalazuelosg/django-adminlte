# Integrar plantilla AdminLTE 3.1 a un proyecto Django 2.2 

Es un intento de integrar la plantilla AdminLTE 3.1 a un proyecto Django 2.2.

Éste proyecto me sirve de base para futuros iniciativos en Django. 


### Qué confirma éste proyecto?

 * [Django 2.2](https://www.djangoproject.com/)
 * [AdminLTE 3.1](https://adminlte.io)
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


### Postgres on Docker

References:
* [hub.docker.com/postgres](https://hub.docker.com/_/postgres)
* [Amigoscode - Docker and PostgreSQL in [10 Minutes]](https://youtu.be/aHbE3pTyG-Q)


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


### Cosas que necesito hacer para levantar proyecto demo

Utilizaré postgres (podrías usar MySQL también, _pero no MSSQL_). Entonces, necesitamos crear usuario y una base de datos.

> Recuerda anotar en un papel aparte usuario, su password y nombre de la base de datos a conectar.

Usuario: user_djangoadminlte
Contraseña: _
Base de datos: db_djangoadminlte


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



Cosas que podrían incluirse en fases posteriores:
 * Custom User authentication schema
 * REST API

[Sugerencias?](https://twitter.com/gpalazuelos)
