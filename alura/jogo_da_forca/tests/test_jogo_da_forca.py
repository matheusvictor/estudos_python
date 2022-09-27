from alura.jogo_da_forca.forca import mascarar_palavra_secreta


class TestJogoForca:

    def test_se_marcara_retorna_numero_underscore_igual_tamanho_da_palavra_recebida(self):
        # given
        entrada = 'banana'
        esperado = ['_', '_', '_', '_', '_', '_']

        # when
        resultado = mascarar_palavra_secreta(entrada)

        # then
        assert resultado == esperado
