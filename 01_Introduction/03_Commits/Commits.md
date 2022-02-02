### Motivación
- Explicar de una forma pedagógica el qué es un *commit* y cómo se inserta esta operación en el gran esquema del control de versiones.

### Explicación con palabras del Pepe
Imagínate a una organización que está formada por dos trabajadores: un operador y un supervisor. Su objetivo es el desarrollo de un proyecto y el aporte de trabajo del operador modifica el estado del proyecto en construcción, esperando que dicha modificación sea un acercamiento al estado de finalización de este. Cada día de trabajo el supervisor lleva un registro exhaustivo del aporte del operador y anota al final del día todos los pasos llevados a cabo por éste desarrollador que modificaron el estado del proyecto. Dicha anotación en su "repostorio" de notas, es lo que sería el equivalente a un *commit* en el mundo del desarrollo de software.

Las modificaciones que un desarrollador puede hacerle a un proyecto para producir un *commit* son:
- Modificar un archivo.
- Crear un nuevo archivo.
- Borrar algún archivo.

Otro aspecto interesante de un commit es que estos se enmarcan en el trabajo que se hace en una **rama** (*branch*). Una *branch* es una versión el proyecto que puede convivir en paralelo con otras, esto abre la posibilidad de paralelizar con confianza el desarrollo de una aplicación entre múltiples personas. Eso último suponiendo que el equipo de desarrollo siga buenas prácticas, que permita la unificación eventual de esos esfuerzos paralelizados en una rama única que sirva para lanzar un determinado *release*.

En la siguiente imagen vemos un flujo típico de una operación con múltiples ramas en un ambiente colaborativo.

![Control de versiones en acción](assets/git_flow.png?raw=true "Title")

### Recursos
- [Documentación oficial de Git](https://git-scm.com/docs)
- [Explicación visual de lo que es un commit](https://stackoverflow.com/a/43970646)
