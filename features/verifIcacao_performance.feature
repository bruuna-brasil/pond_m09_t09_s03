Feature: Performance da API de taxas

    Scenario: Verificar tempo de resposta da API de taxas
        Given que estou fazendo uma requisição para a API de taxas
        When a API responde
        Then o tempo de resposta deve ser menor que 200ms
