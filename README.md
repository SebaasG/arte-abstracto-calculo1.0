````md
# 🎨 Integral Art

> Transformando cálculo integral en arte visual mediante programación.

Integral Art es un proyecto de aula enfocado en la integración entre matemáticas, programación y visualización gráfica.  
El sistema permite resolver integrales definidas utilizando Python y convertir los resultados numéricos obtenidos en composiciones de arte abstracto dinámico generadas por computadora.

La propuesta busca demostrar cómo conceptos matemáticos pueden representarse visualmente a través de herramientas de desarrollo web y procesamiento simbólico.


## 🌐 Aplicación Web

El proyecto se encuentra desplegado en línea mediante Vercel:

🔗 https://arte-abstracto-c-lculo.vercel.app/


# 📌 Objetivo del proyecto

Desarrollar un sistema capaz de:

- Recibir funciones matemáticas ingresadas por el usuario.
- Resolver integrales definidas mediante Python y SymPy.
- Procesar resultados numéricos automáticamente.
- Convertir valores matemáticos en parámetros visuales.
- Generar composiciones de arte abstracto dinámico.

El proyecto combina fundamentos de:

- Cálculo integral
- Programación
- Desarrollo web
- Procesamiento simbólico
- Visualización computacional

---

# 🧠 ¿Cómo funciona?

El sistema sigue el siguiente flujo:

```text
Usuario → Función matemática → Integral definida →
Procesamiento con SymPy → Resultado numérico →
Mapeo de datos → Generación visual
````

Cada resultado obtenido modifica propiedades gráficas como:

* 🎨 Colores
* 🔳 Cantidad de figuras
* 🌫️ Nivel de opacidad
* 📐 Tamaño de elementos
* 🌀 Distribución visual

Esto permite que cada integral genere una representación gráfica única.

---

# 🛠️ Tecnologías utilizadas

| Tecnología | Uso                                |
| ---------- | ---------------------------------- |
| Python     | Procesamiento matemático           |
| SymPy      | Resolución simbólica de integrales |
| HTML       | Estructura de la interfaz          |
| CSS        | Diseño visual                      |
| JavaScript | Interacción dinámica               |
| Vercel     | Despliegue web                     |

---

# 👥 Integrantes

* Daniela Andrea Brito Vanegas
* Karim Yulexi Castillo Garnica
* Keyner Steven Garcia Anaya
* Miguel Sebastian Poveda Grimaldos

---

# ⚙️ Instalación local

## 1. Clonar el repositorio

```bash
git clone https://github.com/Steven02177/arte-abstracto-c-lculo.git
```

---

## 2. Entrar al proyecto

```bash
cd arte-abstracto-c-lculo
```

---

## 3. Instalar dependencias

```bash
pip install sympy
```

---

# ▶️ Ejecución del motor matemático

Ejecute el archivo principal del proyecto:

```bash
python nombre_del_archivo.py
```

---

# 🧪 Ejecución en Google Colab

El motor matemático también puede probarse directamente desde Google Colab.

## Verificar SymPy

En la mayoría de los casos SymPy ya viene instalado.
Si ocurre algún error relacionado con dependencias, ejecute:

```bash
!pip install sympy
```

---

## Ejecutar el sistema

Una vez abierto el archivo:

1. Ejecute la celda principal del proyecto.
2. Ingrese la función matemática.
3. Defina el intervalo de integración.
4. Visualice el resultado obtenido.

---

# 📈 Ejemplo de uso

## Función ingresada

```python
x^2
```

## Intervalo

```python
0 a 5
```

## Resultado aproximado

```python
41.67
```

El valor calculado será utilizado para modificar parámetros visuales dentro del sistema gráfico.

---

# 🧮 Motor principal de cálculo

```python
import sympy as sp

def motor_de_calculo(funcion, a, b):
    x = sp.Symbol('x')

    expr = sp.sympify(
        funcion.replace('^', '**')
    )

    resultado = sp.integrate(
        expr,
        (x, a, b)
    )

    return float(resultado.evalf())
```

Este módulo representa el núcleo matemático del proyecto y es el encargado de:

* interpretar funciones,
* resolver integrales definidas,
* validar expresiones matemáticas,
* y generar resultados numéricos utilizados posteriormente por el sistema visual.

---

# 🎨 Generación visual

El proyecto implementa un sistema de mapeo de datos, donde el resultado de la integral modifica automáticamente distintos elementos gráficos.

Dependiendo del valor obtenido:

* composiciones pequeñas generan estructuras simples,
* valores elevados producen figuras más complejas,
* diferentes rangos alteran colores y opacidad,
* y cada función genera resultados visuales distintos.

---

# 📸 Capturas del proyecto

## Motor matemático

*Agregar captura aquí*

```md
![Motor matemático](./assets/motor.png)
```

---

## Resultado visual generado

*Agregar captura aquí*

```md
![Arte generado](./assets/resultado.png)
```

---

# 📂 Estructura general del proyecto

```text
arte-abstracto-c-lculo/
│
├── backend/
│   ├── motor_calculo.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── assets/
│   ├── motor.png
│   └── resultado.png
│
└── README.md
```

---

# 🚧 Estado actual

Actualmente el proyecto cuenta con:

* ✔️ Motor de cálculo funcional
* ✔️ Resolución automática de integrales
* ✔️ Procesamiento simbólico con SymPy
* ✔️ Generación de parámetros visuales
* ✔️ Interfaz web básica
* ✔️ Despliegue en Vercel


```
