from datetime import datetime, timedelta

class DateHandler:
    @staticmethod
    def obter_ano_mes():
        """Retorna o ano e o mês do período passado no formato YYYYMM."""
        data_atual = datetime.today()
        primeiro_dia_mes_atual = datetime(data_atual.year, data_atual.month, 1)
        mes_passado = primeiro_dia_mes_atual - timedelta(days=1)
        return mes_passado.strftime("%Y%m")  # Retorna no formato YYYYMM

