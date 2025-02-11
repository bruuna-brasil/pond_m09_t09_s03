Feature: Verificação dos ganhos dos entregadores

  Scenario: Garantir que o valor exibido dos ganhos é coerente com o cálculo real
    Given que a UI está exibindo os ganhos do entregador
    When eu realizo o cálculo esperado dos ganhos
    And eu consulto o valor exibido pela UI
    Then a diferença entre o valor calculado e o valor exibido deve ser menor que 0.5%

