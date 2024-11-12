
# Challenge Meli

Este proyecto implementa una API para verificar si una secuencia de ADN pertenece a un mutante o no. Está desarrollado en Python y utiliza `Flask` para crear el servidor web y `MySQL` como base de datos.

## Requisitos

Asegúrate de tener instalado lo siguiente:

- Python 3.7 o superior
- MySQL (con una base de datos configurada)
- `pip` para instalar dependencias

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/francobalich/Challenge-Meli.git
   cd challenge-meli
   ```

2. **Crea y activa un entorno virtual**:

   ```bash
   python -m venv env-challenge
   source env-challenge/bin/activate  # En MacOS/Linux
   env-challenge\Scripts\activate     # En Windows
   ```

3. **Instala las dependencias**:

   Asegúrate de que tienes el archivo `requirements.txt` en el directorio principal del proyecto y ejecuta:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos**:

   Crea una base de datos en MySQL y agrega una tabla llamada `mutant` con la siguiente estructura:

   ```sql
   CREATE TABLE mutant (
       id INT AUTO_INCREMENT PRIMARY KEY,
       dna TEXT NOT NULL,
       is_mutant BOOLEAN NOT NULL
   );
   ```

   Asegúrate de actualizar los parámetros de conexión a la base de datos en tu código, como el nombre de la base de datos, usuario y contraseña.

## Uso

1. **Inicia el servidor**:

   Desde el directorio raíz del proyecto, ejecuta el siguiente comando para iniciar el servidor Flask:

   ```bash
   python main.py
   ```

   El servidor estará disponible en `http://127.0.0.1:5000`.

2. **Endpoint para verificar ADN**:

   - **POST /mutant/**: Este endpoint recibe un JSON con una secuencia de ADN y determina si pertenece a un mutante.

     ```json
     {
       "dna": ["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"]
     }
     ```

     - **Respuesta para mutantes**:
       ```json
       {
         "message": "Mutant detected"
       }
       ```
       Código de estado: 200

     - **Respuesta para humanos**:
       ```json
       {
         "message": "Not a mutant"
       }
       ```
       Código de estado: 403

3. **Ver estadísticas de mutantes**:

   - **GET /stats**: Devuelve las estadísticas de ADN procesados, incluyendo la cantidad de mutantes y humanos, además del ratio.

     **Respuesta**:
     ```json
     {
       "count_mutant_dna": 40,
       "count_human_dna": 100,
       "ratio": 0.4
     }
     ```

## Pruebas

Para ejecutar las pruebas unitarias y verificar la funcionalidad:

```bash
python -m unittest discover -s tests
```

### Medir la cobertura de código (opcional)

Para medir la cobertura del código, asegúrate de tener `coverage` instalado y ejecuta:

```bash
coverage run -m unittest discover -s tests
coverage report
```

## Contribuciones

Si deseas contribuir a este proyecto, por favor realiza un *fork* y abre un *pull request*. Asegúrate de seguir los estándares de código y documentar cualquier cambio importante.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).
