from app.config.database import get_connection


class DashboardService:
    @staticmethod
    def get_metrics():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        metrics = {
            "usuarios": 0,
            "vehiculos": 0,
            "vehiculos_disponibles": 0,
            "tickets_abiertos": 0,
            "reservas": 0,
        }

        try:
            cursor.execute("SELECT COUNT(*) AS total FROM users")
            metrics["usuarios"] = cursor.fetchone()["total"]

            cursor.execute("SELECT COUNT(*) AS total FROM vehiculos")
            metrics["vehiculos"] = cursor.fetchone()["total"]

            cursor.execute("SELECT COUNT(*) AS total FROM vehiculos WHERE disp = 1")
            metrics["vehiculos_disponibles"] = cursor.fetchone()["total"]

            cursor.execute("SELECT COUNT(*) AS total FROM tickets WHERE codesttic = 1")
            metrics["tickets_abiertos"] = cursor.fetchone()["total"]

            cursor.execute("SELECT COUNT(*) AS total FROM reservas")
            metrics["reservas"] = cursor.fetchone()["total"]

        finally:
            cursor.close()
            conn.close()

        return metrics