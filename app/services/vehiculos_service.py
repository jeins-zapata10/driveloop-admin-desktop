from app.config.database import get_connection


class VehiculosService:
    @staticmethod
    def listar_vehiculos():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT 
                v.cod,
                v.`mod`,
                v.`col`,
                v.`pas`,
                v.`prerent`,
                v.`disp`,
                v.`vin`,
                v.`cil`,
                m.des AS marca,
                l.des AS linea,
                c.des AS clase,
                co.des AS combustible,
                ci.des AS ciudad,
                u.nom AS usuario_nombre,
                u.ape AS usuario_apellido,

                (
                    SELECT COUNT(*)
                    FROM reservas r
                    WHERE r.codveh = v.cod
                ) AS total_reservas,

                (
                    SELECT COUNT(*)
                    FROM reservas r
                    WHERE r.codveh = v.cod
                      AND r.codestres IN (1, 2)
                ) AS reservas_activas

            FROM vehiculos v
            LEFT JOIN users u ON v.user_id = u.id
            LEFT JOIN marcas m ON v.codmar = m.cod
            LEFT JOIN lineas l ON v.codlin = l.cod
            LEFT JOIN clases c ON v.codcla = c.cod
            LEFT JOIN combustibles co ON v.codcom = co.cod
            LEFT JOIN ciudades ci ON v.codciu = ci.cod
            ORDER BY v.cod DESC
        """

        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data

    @staticmethod
    def obtener_reservas_por_vehiculo(codveh):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT
                r.cod,
                r.fecrea,
                r.fecini,
                r.fecfin,
                r.val,
                r.confirmado_propietario,
                er.des AS estado,
                u.nom AS usuario_nombre,
                u.ape AS usuario_apellido,
                u.email,
                u.tel
            FROM reservas r
            LEFT JOIN estados_reserva er ON r.codestres = er.cod
            LEFT JOIN users u ON r.idusu = u.id
            WHERE r.codveh = %s
            ORDER BY r.fecini DESC, r.cod DESC
        """

        cursor.execute(query, (codveh,))
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data

    @staticmethod
    def actualizar_vehiculo(cod, data):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE vehiculos
            SET `mod` = %s,
                `col` = %s,
                `pas` = %s,
                `prerent` = %s,
                `disp` = %s
            WHERE cod = %s
        """

        cursor.execute(query, (
            data["mod"],
            data["col"],
            data["pas"],
            data["prerent"],
            data["disp"],
            cod
        ))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def validar_eliminacion(cod):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        resultado = {
            "puede_eliminar": True,
            "documentos": 0,
            "reservas": 0,
            "mensaje": ""
        }

        try:
            cursor.execute(
                "SELECT COUNT(*) AS total FROM documentos_vehiculo WHERE codveh = %s",
                (cod,)
            )
            docs = cursor.fetchone()["total"]

            cursor.execute(
                "SELECT COUNT(*) AS total FROM reservas WHERE codveh = %s",
                (cod,)
            )
            reservas = cursor.fetchone()["total"]

            resultado["documentos"] = docs
            resultado["reservas"] = reservas

            razones = []
            if docs > 0:
                razones.append(f"{docs} documento(s) asociados")
            if reservas > 0:
                razones.append(f"{reservas} reserva(s) asociadas")

            if razones:
                resultado["puede_eliminar"] = False
                resultado["mensaje"] = (
                    "No se puede eliminar este vehículo porque tiene "
                    + " y ".join(razones)
                    + "."
                )

            return resultado

        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def eliminar_vehiculo(cod):
        validacion = VehiculosService.validar_eliminacion(cod)

        if not validacion["puede_eliminar"]:
            raise Exception(validacion["mensaje"])

        conn = get_connection()
        cursor = conn.cursor()

        try:
            query = "DELETE FROM vehiculos WHERE cod = %s"
            cursor.execute(query, (cod,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()