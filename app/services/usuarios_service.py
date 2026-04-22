from app.config.database import get_connection


class UsuariosService:
    @staticmethod
    def listar_usuarios():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT id, nom, ape, email, tel, is_active
            FROM users
            ORDER BY id DESC
        """

        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data