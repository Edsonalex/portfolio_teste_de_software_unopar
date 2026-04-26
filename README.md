# 📚 Portfolio de Teste de Software - Unopar

## Teste de Software: Executando e Validando a Qualidade dos Testes

Este projeto demonstra uma abordagem completa para **criar e validar a eficácia dos testes automatizados** através da técnica de **Teste de Mutação**, implementando boas práticas de **modularização e manutenibilidade** de código.

---

## 🏗️ Arquitetura Modular - Separação de Responsabilidades

O projeto é estruturado em **módulos independentes** para facilitar manutenção, extensão e reutilização:

### 📦 Camada 1: Código Fonte
- **`maximo.py`** - Função principal com validações robustas de tipo

### 📋 Camada 2: Dados de Teste (Casos de Teste)
- **`casos_de_teste_maximo.py`** - Define todos os casos de teste em estruturas de dados reutilizáveis
  - `CASOS_TESTE_BASICOS` - 8 casos para lógica principal
  - `CASOS_TESTE_VALIDACAO` - 14 casos para validação TDD
  - `TODOS_OS_CASOS` - Agregação centralizada

**Benefício de manutenibilidade**: Adicionar novos casos de teste não requer modificação dos módulos de teste.

### 🧬 Camada 3: Mutantes
- **`mutantes_maximo.py`** - Implementação dos 7 mutantes gerados
  - 3 mutantes ROR (Replacement of Relational Operators)
  - 3 mutantes VDL (Value/Decision List)
  - 1 mutante SDL (Statement Deletion)

**Benefício de manutenibilidade**: Mutantes isolados facilitam adição de novos tipos de mutação.

### ⚙️ Camada 4: Lógica de Teste (Reutilizável)
- **`logica_teste_mutacao.py`** - Motor independente para teste de mutação
  - `executar_teste_contra_funcao()` - Executa casos contra qualquer função
  - `testar_mutante()` - Testa um mutante
  - `calcular_mutation_score()` - Calcula métrica de qualidade

- **`logica_de_teste.py`** - Lógica de testes unitários reutilizável
  - `TestMaximoBasicos` - Suite para testes básicos
  - `TestMaximoValidacao` - Suite para testes de validação

**Benefício de manutenibilidade**: Lógica desacoplada permite reutilização em outros projetos.

### 🚀 Camada 5: Executores (Orquestração)

#### **ESTÁGIO 1: Testes Automatizados**
- **`executar_testes_maximo.py`** - Executa testes automatizados
  - Importa `logica_de_teste.py` para suite de testes
  - Importa `casos_de_teste_maximo.py` para dados
  - Gera relatório com taxa de sucesso
  - **Saída**: Validação se a função funciona corretamente

```bash
python executar_testes_maximo.py
```

#### **ESTÁGIO 2: Testes de Mutação (Testes dos Testes)**
- **`teste_mutacao_maximo.py`** - Valida se os testes conseguem detectar mutações
  - Importa `logica_teste_mutacao.py` para motor
  - Importa `mutantes_maximo.py` para mutantes
  - Importa `casos_de_teste_maximo.py` para casos
  - Gera relatório com **Mutation Score**
  - **Saída**: Qualidade dos testes (detecta fraquezas)

```bash
python teste_mutacao_maximo.py
```

---

## 🔄 Fluxo de Dois Estágios de Teste

```
┌─────────────────────────────────────────────────────────────┐
│  ESTÁGIO 1: Testes Automatizados                           │
│  (Valida: A função funciona corretamente?)                 │
├─────────────────────────────────────────────────────────────┤
│ executar_testes_maximo.py                                   │
│        ↓                                                     │
│ Importa: logica_de_teste.py + casos_de_teste_maximo.py    │
│        ↓                                                     │
│ Executa: 22 casos de teste contra maximo.py               │
│        ↓                                                     │
│ Resultado: ✅ Taxa de sucesso (%)                          │
└─────────────────────────────────────────────────────────────┘
                         ↓↓↓
┌─────────────────────────────────────────────────────────────┐
│  ESTÁGIO 2: Teste de Mutação                               │
│  (Valida: Os testes são de boa qualidade?)                 │
├─────────────────────────────────────────────────────────────┤
│ teste_mutacao_maximo.py                                     │
│        ↓                                                     │
│ Importa: logica_teste_mutacao.py + mutantes_maximo.py     │
│        ↓                                                     │
│ Executa: 22 casos de teste contra 7 mutantes              │
│        ↓                                                     │
│ Resultado: 📊 Mutation Score (%) - Qualidade dos Testes   │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Casos de Teste

**Total: 22 casos distribuídos em dois grupos**

### Básicos (8 casos)
- `CT-01` a `CT-08`: Testes de comparação entre números (positivos, negativos, iguais)

### Validação TDD (14 casos)
- `CT-09` a `CT-22`: Rejeição de tipos inválidos (string, float, boolean, None, list, dict)

---

## 🧬 Mutantes Gerados (7 total)

| ID | Nome | Tipo | Descrição |
|---|---|---|---|
| 1 | ROR: > → >= | ROR | Muta operador relacional |
| 2 | ROR: > → < | ROR | Inverte comparação |
| 3 | ROR: > → == | ROR | Muda lógica de comparação |
| 4 | VDL: retorna b no if | VDL | Altera valor de retorno |
| 5 | VDL: retorna a no else | VDL | Altera valor de retorno |
| 6 | SDL: remove else | SDL | Remove instrução |
| 7 | VDL: inverte retornos | VDL | Inverte múltiplos retornos |

---

## 🚀 Como Executar

### Pré-requisitos
```bash
Python 3.7+
```

### Instalação
```bash
git clone https://github.com/Edsonalex/portfolio_teste_de_software_unopar.git
cd portfolio_teste_de_software_unopar
```

### Execução - Estágio 1: Testes Automatizados
```bash
python executar_testes_maximo.py
```
**Verifica**: A função `maximo()` funciona corretamente?

### Execução - Estágio 2: Teste de Mutação
```bash
python teste_mutacao_maximo.py
```
**Verifica**: Os testes conseguem detectar defeitos?

---

## 💡 Benefícios da Arquitetura Modular

### ✅ Manutenibilidade
- Cada módulo tem responsabilidade única e bem definida
- Mudanças em casos de teste não afetam a lógica de teste
- Adição de mutantes não requer modificação de módulos existentes

### ✅ Reutilizabilidade
- `logica_teste_mutacao.py` pode ser reutilizado para outras funções
- `logica_de_teste.py` pode ser adaptado para novos testes
- `casos_de_teste_maximo.py` serve como exemplo de estrutura de dados

### ✅ Testabilidade
- Cada módulo pode ser testado independentemente
- Fácil identificar qual componente falhou
- Facilita debug e correção

### ✅ Escalabilidade
- Novos mutantes são adicionados sem refatoração
- Novos casos de teste não quebram código existente
- Padrão pode ser replicado para outras funções

---

## 📈 Interpretação dos Resultados

### Estágio 1 (Testes Automatizados)
```
✅ Taxa de Sucesso: 100% = Função implementada corretamente
❌ Taxa de Sucesso < 100% = Bugs na função
```

### Estágio 2 (Teste de Mutação)
```
📊 Mutation Score ≥ 70% = Testes de BOA qualidade
⚠️  Mutation Score < 70% = Testes FRÁGEIS - precisam melhorar
```

**Mutation Score** indica o percentual de mutantes detectados pelos testes. Mutantes "vivos" representam casos de teste faltando.

---

## 👤 Autor
**Edsonalex** - Portfolio UNOPAR

---

## 📝 Licença
Projeto desenvolvido para fins educacionais.
