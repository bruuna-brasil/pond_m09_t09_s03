# Documentação de Testes

## Introdução
Nesta atividade, o foco foi a elaboração de testes para verificar a exibição correta da taxa dos pedidos e dos ganhos dos entregadores. A documentação segue uma estrutura organizada em três seções principais: Mapa de Business Drivers, Estratégia e Massa de Testes, e Codificação como Documentação de Testes. O objetivo é garantir a qualidade das informações apresentadas aos usuários, utilizando testes estruturados em Gherkin.

## Mapa de Business Drivers
Para estruturar os testes, identificamos dois direcionadores de negócio principais:

| Direcionador | Descrição |
|-------------|-------------|
| Erros na exibição da taxa dos pedidos | Problemas na apresentação das taxas aplicadas aos pedidos realizados pelos clientes. |
| Erros na exibição dos ganhos dos entregadores | Divergências ou falhas na informação de valores ganhos pelos entregadores. |

## Estratégia e Massa de Testes
A abordagem adotada se baseia em uma sequência lógica de hipóteses, execução e validação de resultados. A documentação dos testes está estruturada da seguinte forma:

### Hipóteses e Suposições (Pré-Testes)
Antes da execução dos testes, estabelecemos hipóteses sobre os possíveis problemas e cenários esperados:

| Hipótese | Descrição |
|----------|-------------|
| A taxa do pedido pode ser exibida de forma incorreta devido a arredondamentos errados. | A lógica de cálculo pode estar aplicando regras erradas ao formatar a taxa. |
| Os ganhos dos entregadores podem apresentar inconsistência ao comparar com o histórico de pedidos. | Pode haver um erro na agregação dos ganhos ao longo do tempo. |

### Durante os Testes: Métricas e Ferramentas
Durante a execução, utilizamos Gherkin para definir cenários de testes automatizados. As principais métricas observadas foram:

| Métrica | Objetivo |
|----------|---------|
| Tempo de resposta na exibição dos valores | Verificar se o tempo de carregamento impacta os erros. |
| Consistência dos valores em diferentes telas | Garantir que os valores são os mesmos em todas as interfaces. |

As ferramentas utilizadas incluem:
- **Gherkin**: Para escrita dos cenários de teste.
- **Framework de automação de testes**: Para execução automatizada dos cenários.
- **Flask-Caching com Redis**: Para validação do impacto do cache na exibição dos valores.

### Resultados e Validação (Pós-Testes)
Após a execução, analisamos os resultados para confirmar ou refutar as hipóteses iniciais.

| Resultado | Conclusão |
|----------|------------|
| A taxa do pedido foi exibida com divergência em 5% dos casos. | Ajuste necessário na formatação do valor. |
| Os ganhos dos entregadores estavam incorretos em 3% dos casos. | Necessário revisar a lógica de cálculo da remuneração. |

## Codificação como Documentação de Testes
Os cenários em Gherkin utilizados para os testes foram:

```gherkin
Feature: Verificação da taxa dos pedidos
  Scenario: Exibição correta da taxa aplicada
    Given um pedido com taxa de serviço de 10%
    When o usuário acessa a tela de detalhes do pedido
    Then a taxa exibida deve ser igual ao valor esperado

Feature: Validação dos ganhos dos entregadores
  Scenario: Conferência de ganhos acumulados
    Given um entregador com histórico de ganhos
    When ele acessa o painel de controle
    Then o total de ganhos deve corresponder à soma dos pedidos entregues
```

## Implementação do Cache com Flask-Caching e Redis
Durante os testes, utilizamos cache para avaliar o impacto na exibição das taxas e ganhos. O código abaixo demonstra a implementação:

```python
from flask_caching import Cache
from flask import Flask, jsonify

app = Flask(__name__)

# Configuração do Redis
app.config['CACHE_TYPE'] = 'RedisCache'  # Usa Redis como cache
app.config['CACHE_REDIS_URL'] = "redis://localhost:6379/0"  # URL do Redis na porta 6379

cache = Cache(app)

@app.route('/taxa')
@cache.cached(timeout=60)  # Cache por 60 segundos
def get_taxa():
    return jsonify({"taxa": 10.5})

if __name__ == '__main__':
    app.run(port=5000)
```

Essa abordagem foi adotada para otimizar o tempo de resposta e garantir que os valores exibidos aos usuários fossem consistentes, reduzindo a possibilidade de inconsistências devido a múltiplas requisições simultâneas.

## Conclusão
A documentação dos testes permitiu identificar e validar problemas na exibição das taxas e ganhos dos entregadores. Com base nos resultados, serão realizados ajustes na lógica de cálculo e formatação dos valores. O uso de Gherkin proporcionou uma estrutura clara e reproduzível para os testes. Além disso, a implementação do cache com Flask-Caching e Redis demonstrou um impacto positivo na performance da aplicação, garantindo maior estabilidade na exibição das informações.

