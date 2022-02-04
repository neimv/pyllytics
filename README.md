# pyllytics

## Acerca de:

Este es un pequeño proyecto en Python, en donde espero poder crear una pequeña plataforma que haga un poco de analitica las ideas son:
 
 - tener un backend con todo lo relacionado a accesos, y manejo de obtencion de los dataframe
 - tener un frontend que muestre todas las estadisticas del dataset, asi como algunos "consejos"
 - hacer un pequenio analisis del dataset, donde:
    - obtenga el dataset de acuerdo al lugar donde se tenga almacenado (file, sql)
    - obtener los valores mas comunes de la estadistica
    - obtener correlaciones entre las variables
    - obtener los tipos de datos y cuales podrian ser los mejores para usar
    - nice to have: imputacion de datos

Hasta el momento es la idea principal, este pequeño sistema no hara modelos matematicos por el momento, tal vez en una segunda iteracion sea posible y despues de resolver el problema de los dataset grandes ;-)

## Limitando el proyecto

- Se usaran herramientas python, en general pandas, django y fastapi
- Aun no se tiene algo definido para el Front (debido a que tiene años que no lo uso)
- Los lectores de archivos hasta el momento solo seran:
    - CSV, limitado por coma, pipe, punto y coma y dos puntos en caso de que el usuario no lo proporcione
    - JSON
    - Excel
    - XML
    - Parquet
- Los lectores de bases de datos estaran limitados a:
    - MySQL
    - Postgres
    - MariaDB
- El lector web:
    - REST API
