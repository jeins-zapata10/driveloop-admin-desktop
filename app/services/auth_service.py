import bcrypt
from app.config.database import get_connection


class AuthService:
    @staticmethod
    def login(email, password):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT 
                u.id,
                u.nom,
                u.ape,
                u.email,
                u.password,
                u.is_active,
                r.name AS rol
            FROM users u
            LEFT JOIN model_has_roles mhr
                ON mhr.model_id = u.id
               AND mhr.model_type = 'App\\\\Models\\\\MER\\\\User'
            LEFT JOIN roles r
                ON r.id = mhr.role_id
            WHERE u.email = %s
            LIMIT 1
        """

        try:
            cursor.execute(query, (email,))
            user = cursor.fetchone()

            if not user:
                return {
                    "success": False,
                    "message": "Credenciales inválidas."
                }

            stored_hash = user.get("password")
            if not stored_hash:
                return {
                    "success": False,
                    "message": "El usuario no tiene contraseña válida."
                }

            try:
                password_ok = bcrypt.checkpw(
                    password.encode("utf-8"),
                    stored_hash.encode("utf-8")
                )
            except Exception:
                return {
                    "success": False,
                    "message": "No fue posible validar la contraseña."
                }

            if not password_ok:
                return {
                    "success": False,
                    "message": "Credenciales inválidas."
                }

            if not user.get("is_active"):
                return {
                    "success": False,
                    "message": "Este usuario está inactivo."
                }

            if user.get("rol") != "Administrador":
                return {
                    "success": False,
                    "message": "Acceso denegado. Esta aplicación solo permite ingreso de administradores."
                }

            return {
                "success": True,
                "user": user
            }

        finally:
            cursor.close()
            conn.close()