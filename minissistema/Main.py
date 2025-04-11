from api.esMenu import APP
from minissistema.RuleBaseMontarPC import RuleBaseMontarPC

class Main:
    def __init__(self):
        self.app = APP("Sistema Especialista - Montagem de Computador")

    def main(self):
        try:
            # RuleBaseMontarPC recebe dois parâmetros:
            # o primeiro é o nome da base de regras,
            # o segundo é a lista de variáveis-alvo (objetivos).
            brMontarPC = RuleBaseMontarPC("Montar PC", ["gpu", "ram", "mobo"])
            self.app.add_rule_base(brMontarPC)
            self.app.menu()
        except Exception as e:
            print("Exception: RuleApp ", e)

if __name__ == '__main__':
    Main().main()
