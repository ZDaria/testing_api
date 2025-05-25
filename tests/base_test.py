

class BaseTest:
    """Базовый тестовый класс"""
    error_list = []
    # main_config

    @staticmethod
    def assert_error(errors: list[str]):
        """Проверить ошибки в списке ошибок

        Args:
            errors: список ошибок
        """
        assert not errors, f"Обнаружены следующие ошибки{errors}"
