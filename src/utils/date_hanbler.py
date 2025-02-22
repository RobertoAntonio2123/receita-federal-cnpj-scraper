from datetime import datetime

class DateHandler:
    
    def obter_ano_mes_atual():
        """Retorna a data atual no formato YYYYMM."""
        return datetime.now().strftime("%Y%m")

if __name__ == "__main__":
    print(DateHandler.obter_ano_mes_atual())  # Deve sempre retornar o ano e mês atuais
