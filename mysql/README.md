# Docker MySQL Connections

### 1. we need to the next images:

#### Pull mysql Image, you can choise the tags from this [official mysql Page](https://hub.docker.com/_/mysql)
>  `docker pull mysql:latest`

to Start the myphpapacheserver container ditectliy and temporary:
>  `docker run -d --rm -v %cd%:/var/www/html -p 80:80 myphpapacheserver `

`--rm` to remove this container after stop/end


### 3. Create mysql Container with out dicker compose:
>  `docker run -d -v ${pwd}:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-pass -e MYSQL_PASSWORD=my-user-pass -e MYSQL_USER=user-name -e MYSQL_DATABASE=default_db -p 3306:3306 mysql:latest --default-authentication-plugin=mysql_native_password `\
You need to specify one of `MYSQL_ROOT_PASSWORD`, `MYSQL_ALLOW_EMPTY_PASSWORD` and `MYSQL_RANDOM_ROOT_PASSWORD`
*  ``MYSQL_PASSWORD=my-user-pass`` 
*  ``MYSQL_USER=user-name``\
if you don't set the above Environment Variables:
>  `docker run -d -v ${pwd}:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-pass -e MYSQL_DATABASE=default_db -p 3306:3306 mysql:latest --default-authentication-plugin=mysql_native_password `\
the user name will be ``root``

#### Note:
When using the docker image to start without an existing database, the container's entrypoint.sh script tries to call the mysqld binary to create the database. This fails in versions later than 5.7.5 because the script starts by calling mysqld --verbose --help to get the configured datadir and when that runs and there is no database, it initializes it automatically.
When the script then calls --initialize, that fails with the error:\
``[ERROR] --initialize specified but the data directory has files in it. Aborting.``
for that we neet to craete a default database
add new Environment: ``-e MYSQL_DATABASE=default_db``

___

# Create All Images and Containers with Docker Composer
you must be in docker-compose.yml file directery and write this commend:
>  `docker-compose up`

