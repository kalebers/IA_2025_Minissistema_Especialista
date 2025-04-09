from api.esBooleanRuleBase import BooleanRuleBase
from api.esRuleVariable import RuleVariable
from api.esCondition import Condition
from api.esRule import Rule
from api.esClause import Clause

class RuleBaseMontarPC:
    def __init__(self, nome, goals_list):
        self.br = BooleanRuleBase(nome)
        self.goals_list = goals_list

    def get_goal_list(self):
        return self.goals_list

    def create(self):
        uso = RuleVariable(self.br, "uso")
        uso.set_labels("jogos escritorio edicao")
        uso.set_prompt_text("Qual será o uso do computador [jogos, escritorio, edicao]?")

        cpu = RuleVariable(self.br, "cpu")
        cpu.set_labels("i9 i5 ryzen7 ryzen5")
        cpu.set_prompt_text("Qual processador deseja [i9, i5, ryzen7, ryzen5]?")

        gpu = RuleVariable(self.br, "gpu")
        gpu.set_labels("RTX3060 GTX1650 integrada")
        gpu.set_prompt_text("Qual placa de vídeo deseja [RTX3060, GTX1650, integrada]?")

        ram = RuleVariable(self.br, "ram")
        ram.set_labels("8GB 16GB 32GB")
        ram.set_prompt_text("Quantos GB de RAM deseja [8GB, 16GB, 32GB]?")

        fonte = RuleVariable(self.br, "fonte")
        fonte.set_labels("500W 600W 750W")
        fonte.set_prompt_text("Qual potência da fonte [500W, 600W, 750W]?")

        mobo = RuleVariable(self.br, "mobo")
        mobo.set_labels("intel amd")
        mobo.set_prompt_text("Qual o tipo de placa-mãe compatível [intel, amd]?")

        c_equals = Condition("=")

        # Regras
        regra_jogos = Rule(self.br, "Regra_Jogos",
                           [Clause(uso, c_equals, "jogos")],
                           Clause(gpu, c_equals, "RTX3060"))

        regra_escritorio = Rule(self.br, "Regra_Escritorio",
                                [Clause(uso, c_equals, "escritorio")],
                                Clause(gpu, c_equals, "integrada"))

        regra_edicao = Rule(self.br, "Regra_Edicao",
                            [Clause(uso, c_equals, "edicao")],
                            Clause(ram, c_equals, "32GB"))

        regra_amd_cpu = Rule(self.br, "Regra_AMD_CPU",
                             [Clause(cpu, c_equals, "ryzen7")],
                             Clause(mobo, c_equals, "amd"))

        regra_intel_cpu = Rule(self.br, "Regra_Intel_CPU",
                               [Clause(cpu, c_equals, "i5")],
                               Clause(mobo, c_equals, "intel"))

        return self.br

    def demo_fc(self, LOG):
        LOG.append(" --- Demonstração com Forward Chaining ---")
        self.br.set_variable_value("uso", "jogos")
        self.br.set_variable_value("cpu", "ryzen7")
        self.br.set_variable_value("gpu", None)
        self.br.set_variable_value("ram", None)
        self.br.set_variable_value("fonte", None)
        self.br.set_variable_value("mobo", None)
        self.br.display_variables(LOG)

    def demo_bc(self, LOG):
        LOG.append(" --- Demonstração com Backward Chaining ---")
        self.br.set_variable_value("uso", None)
        self.br.set_variable_value("cpu", None)
        self.br.set_variable_value("gpu", None)
        self.br.set_variable_value("ram", None)
        self.br.set_variable_value("fonte", None)
        self.br.set_variable_value("mobo", None)
        self.br.display_variables(LOG)
