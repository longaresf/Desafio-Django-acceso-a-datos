# Django ORM Data Access & Query Optimization

Este repositorio contiene un proyecto desarrollado en **Python** con el framework **Django**, enfocado en el diseño, estructuración e implementación avanzada de la capa de acceso a datos. El objetivo principal de este desarrollo es demostrar el dominio del ORM de Django para realizar consultas complejas, filtrados dinámicos y manipulación eficiente de modelos relacionales, minimizando el impacto en el rendimiento de la base de datos.

## 🚀 Características y Capacidades Técnicas

* **Consultas Avanzadas con ORM:** Reemplazo de consultas SQL crudas por lógica orientada a objetos mediante el ORM de Django, garantizando seguridad contra inyecciones SQL.
* **Filtrado y Agregación Dinámica:** Implementación de consultas con filtros específicos (`filter()`, `exclude()`) y funciones de agregación para procesar volúmenes de datos en el servidor.
* **Optimización de Consultas:** Uso de buenas prácticas para evitar el problema común de las consultas redundantes (ej. control de consultas perezosas o *lazy loading*).
* **Integración con la Capa de Negocio:** Conexión directa entre los modelos de datos y las vistas o controladores para despachar información estructurada al cliente final.

## 🛠️ Stack Tecnológico

* **Lenguaje de Programación:** Python 3.x
* **Framework Backend:** Django 4.x / 5.x
* **Capa de Persistencia:** Django ORM
* **Base de Datos:** PostgreSQL.

## ⚙️ Arquitectura de Datos y Resolución de Problemas

El desarrollo aborda el desafío de interactuar con el motor de almacenamiento de manera eficiente y segura:

1. **Abstracción del Acceso a Datos:** Se estructuraron los modelos definiendo índices y relaciones adecuadas para asegurar que la búsqueda y recuperación de registros sea óptima.
2. **Lógica de Consultas Reutilizable:** Implementación de métodos de filtrado optimizados directamente en la lógica del backend para mantener los controladores limpios y legibles (*Fat Models, Skinny Views*).
3. **Manejo de Transacciones Seguro:** Operaciones de lectura y escritura estructuradas para mantener la consistencia de los registros en la base de datos usando transacciones atómicas.

## 🔧 Instalación y Despliegue Local

Sigue estos pasos para configurar el entorno de pruebas localmente:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/longaresf/django-orm-data-access.git](https://github.com/longaresf/django-orm-data-access.git)
   ```
2. Ingresar al directorio:
   Bash
   cd django-orm-data-access

3. Configurar el entorno virtual e instalar requerimientos:
   Bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   pip install -r requirements.txt

4. Sincronizar el esquema de la base de datos:
   Bash
   python manage.py makemigrations
   python manage.py migrate

5. Ejecutar la aplicación en el servidor local:
   Bash
   python manage.py runserver

✒️ Créditos y Autoría

    Francisco Longares - Desarrollador Backend Python - longaresf

    Este proyecto fue desarrollado para resolver las evaluaciones técnicas avanzadas sobre manipulación y optimización de la capa de datos dentro del programa Full Stack Python de Desafío Latam.
