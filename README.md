# Mastermind

Esta es una versión del juego Mastermind implementado completamnete en Python, donde el objetivo es adivinar un código secreto de cuatro colores únicos. Cada intento permite ingresar una combinación de colores, y el juego proporciona pistas visuales indicando qué colores son correctos y si están en la posición adecuada.

El programa cuenta con un modo manual, donde el jugador introduce sus intentos, y un modo automático, en el que un algoritmo de búsqueda inteligente resuelve el código de manera óptima. Además, el juego genera un tablero gráfico que representa los intentos realizados y las pistas obtenidas.

## Requisitos

Para ejecutar el código, asegúrate de tener instaladas las siguientes dependencias:

### Usando Conda:
Si deseas configurar el entorno con Conda, usa el archivo `environment.yml`:
```bash
conda env create -f environment.yml
conda activate mastermind
```

### Usando pip:
Como alternativa, puedes instalar los requisitos desde `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Cómo jugar

Ejecuta el script principal para iniciar el juego:
```bash
python3 master.py
```

### Modos de juego
- **Juego Manual:** Podrás ingresa colores manualmente y recibirás retroalimentación visualmente.
- **Autoplay:** Un algoritmo automático resuelve el código de colores sin intervención del usuario. Además, incluye al inicio instrucciones detalladas de cuales son las reglas del juego y como debes jugarlo.

## Instrucciones
1. El juego generará un código de cuatro colores únicos.
2. En cada intento, ingresa cuatro colores en inglés.
3. Recibirás pistas con "x" de colores:
   - Verde: color y posición correctos.
   - Amarillo: color correcto, pero en la posición incorrecta.
   - Rojo: color incorrecto.
4. El juego termina cuando aciertas los cuatro colores y sus posiciones.

## Autor
Desarrollado por Eduardo Buenrostro.

## Licencia
Este proyecto se distribuye bajo la licencia MIT.
