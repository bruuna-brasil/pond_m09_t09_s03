
Feature: Verificação do valor da taxa dos pedidos

  Scenario: Verificar se o valor exibido na UI é igual ao valor retornado pela API
    Given que a UI está exibindo a taxa do pedido
    When eu consulto o valor da taxa diretamente da API
    Then o valor exibido na UI deve ser exatamente igual ao valor retornado pela API
