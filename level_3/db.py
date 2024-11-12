import mysql.connector

class MutantDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.connect()

    def connect(self):
        """Establece la conexión con la base de datos."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión exitosa")
        except mysql.connector.Error as err:
            print("Error al conectar:", err)

    def saveData(self, dna, is_mutant):
        """Guarda datos en la tabla `mutant`."""
        dna_str = ','.join(dna)
        sql = "INSERT INTO mutant (dna, is_mutant) VALUES (%s, %s)"
        valores = (dna_str, is_mutant)

        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, valores)
            self.connection.commit()
            print("Registro insertado exitosamente")
        except mysql.connector.Error as err:
            print("Error al insertar datos:", err)
        finally:
            if cursor is not None:
                cursor.close()


    def getStats(self):
            """Obtiene estadísticas de mutantes y humanos, además del ratio de mutantes."""
            cursor = None
            try:
                cursor = self.connection.cursor(dictionary=True)

                query = """
                    SELECT
                        SUM(CASE WHEN is_mutant = TRUE THEN 1 ELSE 0 END) AS mutantes,
                        SUM(CASE WHEN is_mutant = FALSE THEN 1 ELSE 0 END) AS humanos
                    FROM mutant;
                """
                cursor.execute(query)
                result = cursor.fetchone()
                mutantes = result['mutantes']
                humanos = result['humanos']

                total = mutantes + humanos
                ratio_mutantes = round(mutantes / total if total > 0 else 0, 2)

                return {
                    "count_mutant_dna": mutantes,
                    "count_human_dna": humanos,
                    "ratio": ratio_mutantes
                }
            except mysql.connector.Error as err:
                print("Error al obtener estadísticas:", err)
                return None
            finally:
                if cursor is not None:
                    cursor.close()
    def dna_exists(self, dna):
            """Verifica si un valor de DNA ya existe en la base de datos."""
            cursor = None
            try:
                cursor = self.connection.cursor()
                dna_str = ','.join(dna)

                query = "SELECT COUNT(*) FROM mutant WHERE dna = %s"
                cursor.execute(query, (dna_str,))
                result = cursor.fetchone()

                return result[0] > 0
            except mysql.connector.Error as err:
                print("Error al verificar existencia de DNA:", err)
                return False
            finally:
                if cursor is not None:
                    cursor.close()

    def close(self):
        """Cierra la conexión con la base de datos."""
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")

