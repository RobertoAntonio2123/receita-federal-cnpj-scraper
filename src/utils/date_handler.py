from datetime import datetime, timedelta

def get_last_month():
    """Retorna o ano e mês anterior ao atual no formato YYYYMM."""
    hoje = datetime.today()
    primeiro_dia_mes_atual = hoje.replace(day=1)
    mes_passado = primeiro_dia_mes_atual - timedelta(days=1)
    return mes_passado.strftime("%Y%m")
