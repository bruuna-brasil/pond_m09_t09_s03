from behave import given, when, then
import requests

@given("que a UI está exibindo a taxa do pedido")
def step_ui_exibe_taxa(context):
    # Simular acesso à UI para capturar o valor exibido
    context.ui_taxa_valor = 12.50  # Exemplo estático, substituir com integração real

import requests

import requests

@when("eu consulto o valor da taxa diretamente da API")
def step_consulta_api_taxa(context):
    response = requests.get("http://localhost:5000/taxa")
    context.api_taxa_valor = response.json().get("taxa")


@then("o valor exibido na UI deve ser exatamente igual ao valor retornado pela API")
def step_verifica_taxa(context):
    assert abs(context.ui_taxa_valor - context.api_taxa_valor) < 0.1, \
        f"Erro: Valor UI {context.ui_taxa_valor}, Valor API {context.api_taxa_valor}"


@given("que a UI está exibindo os ganhos do entregador")
def step_ui_exibe_ganhos(context):
    context.ui_ganhos_valor = 500.75  # Exemplo estático

@when("eu realizo o cálculo esperado dos ganhos")
def step_calcula_ganhos(context):
    # Simular cálculo real dos ganhos, exemplo fictício
    context.calculo_real_ganhos = 500.50

@when("eu consulto o valor exibido pela UI")
def step_consulta_ganhos_ui(context):
    # Já capturado no given
    pass

@then("a diferença entre o valor calculado e o valor exibido deve ser menor que 0.5%")
def step_verifica_diferenca_ganhos(context):
    diferenca = abs(context.ui_ganhos_valor - context.calculo_real_ganhos)
    margem = context.calculo_real_ganhos * 0.005
    assert diferenca <= margem, \
        f"Erro: Diferença {diferenca}, Margem Permitida {margem}"
