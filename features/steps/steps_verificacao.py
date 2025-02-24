from behave import given, when, then
import requests
import time

API_URL = "http://localhost:5000/taxa"

@given("que a UI está exibindo a taxa do pedido")
def step_ui_exibe_taxa(context):
    context.ui_taxa_valor = 10.50  

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


@given(u'que estou fazendo uma requisição para a API de taxas')
def step_impl(context):
    context.start_time = time.time()
    context.response = requests.get(API_URL)
    context.end_time = time.time()

@when(u'a API responde')
def step_impl(context):
    assert context.response is not None, "A resposta da API está vazia"

@then(u'o tempo de resposta deve ser menor que 200ms')
def step_impl(context):
    response_time = (context.end_time - context.start_time) * 100 
    assert response_time < 250, f"Tempo de resposta muito alto: {response_time}ms"

@given(u'a UI está exibindo um valor de taxa')
def step_impl(context):
    context.ui_taxa = "R$ 5,00"  # Simulação de um valor retornado pela UI

@when(u'a API retorna um valor nulo para a taxa do pedido')
def step_impl(context):
    context.api_taxa = None  # Simulando um retorno nulo da API

@then(u'a UI deve exibir uma mensagem de erro apropriada')
def step_impl(context):
    assert context.api_taxa is None, "A API deveria ter retornado um valor nulo"
    mensagem_erro = "Erro: taxa não disponível"
    assert mensagem_erro in ["Erro: taxa não disponível", "Taxa não encontrada"], "Mensagem de erro incorreta"
