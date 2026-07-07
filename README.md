 ## Laboratorio del lenguaje Python
 **Materia:** Algoritmos y Estructuras de Datos 2026
 **Comisión 1.1 / Grupo A7**
 
 ## Integrantes
- Juan Ignacio Aguilera
- Valentina Magali Alvira Coseres
- Rocco Agustín Macías
- Jonathan Tomás Zilli Macías

## Descripción General del Sistema
El escenario asignado consiste en un sistema de inscripción a cursos desarrollado en Python mediante una interfaz de consola. Su objetivo es permitir la gestión básica de inscripciones de estudiantes en distintos cursos, controlando los cupos disponibles y administrando listas de espera cuando los cursos alcanzan su capacidad máxima. 
Cada curso posee un cupo máximo de estudiantes, cuando dicho cupo se completa, los nuevos estudiantes son agregados automáticamente a una lista de espera.
Además, el sistema genera estadísticas sobre la cantidad de inscriptos, estudiantes en espera y el curso con mayor demanda.

## Instrucciones de Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/juanigithub/labpyhton.git
```

### 2. Acceder a la carpeta del proyecto

```bash
cd labpyhton
```

### 3. Ejecutar el programa

```bash
python main.py
```

### 4. Utilizar el menú principal

Al iniciar el programa se mostrará el siguiente menú:

```text
--- Menu Sistema de Inscripción ---

1. Inscribir estudiante
2. Ver cursos y cupos
3. Ver estadísticas
0. Salir
```

Ingrese el número correspondiente a la operación deseada.


## Uso de Inteligencia Artificial

Durante el desarrollo del proyecto se utilizó Claude (Anthropic) como
herramienta de apoyo para el aprendizaje y la programación. Concretamente
se usó para:

 **Planificar el desarrollo**: definir un orden de trabajo progresivo
  (estructura de datos → menú → funciones → validaciones), pensado para
  reflejarse en commits incrementales.
 **Resolver dudas sobre validación de datos ingresados por el usuario**:
  uso de `try/except` para capturar `ValueError` al pedir números (ID de
  curso, DNI) y de bucles `while` para repetir la solicitud hasta obtener
  un dato válido.
 **Discutir decisiones de diseño**: cómo evitar inscripciones duplicadas
  usando el DNI del estudiante como identificador único por curso, y cómo
  definir la "demanda real" de un curso como la suma de sus inscriptos más
  su lista de espera (en vez de solo los inscriptos).

Todas las soluciones propuestas por la IA fueron analizadas, discutidas y
comprendidas por el equipo antes de incorporarlas al código.
