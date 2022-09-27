from alura.jogo_da_forca.forca import *


class TestJogoForca:

    def test_se_marcara_retorna_numero_underscore_igual_tamanho_da_palavra_recebida(self):
        # given
        entrada = 'banana'
        esperado = ['_', '_', '_', '_', '_', '_']

        # when
        resultado = mascarar_palavra_secreta(entrada)

        # then
        assert resultado == esperado

    def test_quando_palpite_completo_for_igual_palavra_secreta_deve_ganhar(self):
        entrada = 'manga'.upper()
        palavra_secreta = 'manga'.upper()
        esperado = True

        resultado = verificar_palavra_completa(entrada, palavra_secreta)

        assert resultado == esperado
