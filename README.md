[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=AronCervantes/ProyectoMSF)

# ProyectoMSF

## Información de los estudiantes
Aron Cervantes Armenta \[22211750]; l22211750@tectijuana.edu.mx

Bricia Idalia Arellano Salones \[22211746]; l22211776@tectijuana.edu.mx

Alejandro Ramirez Zepeda \[22211765]; l22211765@tectijuana.edu.mx

Abigail Villa Camacho \[22212276]; l22212276@tectijuana.edu.mx


Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente
Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Calcular la función de transferencia.
2. Determinar el modelo de ecuaciones integro-diferenciales.
3. Establecer el sistema de ecuaciones diferenciales ordinarias lineales de primer orden.
4. Emular la respuesta del circuito RLC en Simulink/Simscape al escalón, impulso, rampa y función sinusoidal.
5. Simular la respuesta de los modelos matemáticos en Simulink/MATLAB al escalón, impulso, rampa y función sinusoidal.
6. Sintonizar las ganancias de un controlador PID para eliminar el error entre la entrada y la salida del sistema.

## Descripción detallada del sistema

El sistema urinario puede representarse como un circuito eléctrico donde cada componente imita la función de una parte del sistema. La producción de orina se modela con la fuente Vin. El riñón se representa con el capacitor CR y la resistencia Rr, que simulan su capacidad de regular presión y la oposición al flujo. Los uréteres se modelan mediante la resistencia RU, que representa la fricción natural del transporte hacia la vejiga.
La vejiga funciona como un capacitor CV, encargado de almacenar orina; mientras más grande sea su valor, mayor es su capacidad de llenado. La salida del sistema depende del esfínter uretral, representado por la resistencia RE, que actúa como una barrera que controla cuándo la orina puede pasar hacia la uretra. Finalmente, la uretra se modela con el capacitor Cu, que representa el volumen previo a la expulsión y lleva a la salida Vout.

Control: 
En un individuo sano, todos los componentes del circuito mantienen valores adecuados para asegurar la producción, transporte, almacenamiento y vaciado normal de la orina. La vejiga (CV) almacena suficiente volumen, y el esfínter (RE) mantiene la continencia.

Caso 1: Incontinencia por esfuerzo
En este caso, la resistencia RE disminuye para representar un esfínter débil. Al bajar su valor, el flujo hacia la uretra se libera con mayor facilidad, simulando pérdidas involuntarias de orina cuando aumenta la presión abdominal (al toser, reír o cargar peso). El resto del circuito permanece igual.

Caso 2: Vejiga rígida o de baja capacidad
Aquí el problema está en la vejiga, por lo que el capacitor CV se reduce. Un valor más pequeño significa menos capacidad de almacenamiento, lo que provoca urgencia para orinar y vaciamientos frecuentes. La resistencia del esfínter (RE) se mantiene normal, ya que no es el origen del problema.

Palabras Clave: Circuito RC; Controlador PI; Sistema urinario; Modelo matematico; Simulaciones numericas.

## Lista de archivos incluidos en el repositorio
1. Cuaderno computacional de MATLAB [.mlx]. [1]
2. Modelo de Simulink [.slx]. [1]
3. Imagen con los parámetros del controlador. [2]
4. Imagénes de las simulaciones [.pdf y .png]. [2 + 2]

## Referencias
\[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2025. Permalink: https://biomath.xyz/course/

\[2] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018, Section 4, Page 93.

\[3] N. S. Nise. Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.
