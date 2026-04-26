# Projeto de Teste de Mutação

Este projeto é dedicado a teste de mutação, uma técnica importante para avaliar a eficácia dos testes automatizados. O objetivo principal é introduzir mutantes no código para verificar se os testes existentes conseguem detectar essas mudanças.

## Estrutura do Projeto

O projeto contém os seguintes arquivos:

1. **maximo.py**: Código original que implementa a lógica principal.
2. **mutantes_maximo.py**: Implementação dos mutantes gerados a partir do código original.
3. **casos_de_teste_maximo.py**: Conjunto de casos de teste que são utilizados para verificar a funcionalidade do código.
4. **logica_teste_mutacao.py**: Lógica para aplicar testes de mutação e verificar a detecção dos mutantes.
5. **teste_mutacao_maximo.py**: Testes que são executados para validar a eficácia dos testes de mutação.
6. **logica_de_teste.py**: Lógica geral para execução dos testes.
7. **test_maximo.py**: Testes adicionais para o código original.
8. **executar_testes_maximo.py**: Script para executar todos os testes de forma automatizada.

## Mutantes Criados

Foram gerados 7 mutantes, contemplando os seguintes tipos:
- **ROR (Replacement of Operators)**: Substituição de operadores lógicos e aritméticos.
- **VDL (Variable Discrepancy Logic)**: Mudança na lógica de variáveis.
- **SDL (Statement Deletion Logic)**: Exclusão de instruções relevantes no código.

## Casos de Teste

Os testes consistem em um total de 22 casos, divididos da seguinte forma:
- **8 Casos Básicos**: Testes fundamentais que verificam as funcionalidades principais do código.
- **14 Casos de Validação**: Testes robustos que garantem a validação das entradas e saídas, testando limites e condições especiais.

## Como Executar os Testes

Para executar os testes, siga os passos abaixo:
1. Certifique-se de que você tem o Python instalado em seu ambiente.
2. Clonar o repositório:
   ```bash
   git clone https://github.com/Edsonalex/portfolio_teste_de_software_unopar.git
   cd portfolio_teste_de_software_unopar
   ```
3. Execute o script de testes:
   ```bash
   python executar_testes_maximo.py
   ```
4. Verifique os resultados no console para ver a eficácia dos testes.

## Conclusão

Este projeto proporciona uma abordagem eficaz para a identificação de fraquezas nos testes automatizados através da técnica de teste de mutação. Através da implementação de mutantes e execução de testes, podemos melhorar continuamente a qualidade do código.