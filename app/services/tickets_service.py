from app.config.database import get_connection


class TicketsService:
    @staticmethod
    def listar_tickets():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT 
                t.cod,
                t.asu,
                t.des,
                t.res,
                t.feccre,
                t.fecpro,
                t.feccie,
                t.codres,

                et.des AS estado,
                pt.des AS prioridad,

                u.nom AS usuario_nombre,
                u.ape AS usuario_apellido,

                s.nom AS soporte_nombre,
                s.ape AS soporte_apellido

            FROM tickets t
            LEFT JOIN estados_ticket et ON t.codesttic = et.cod
            LEFT JOIN prioridades_ticket pt ON t.codpritic = pt.cod
            LEFT JOIN users u ON t.idusu = u.id
            LEFT JOIN users s ON t.idususop = s.id
            ORDER BY t.cod DESC
        """

        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data