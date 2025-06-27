
# Projeto QA com Jenkins, Postman e Newman

Este projeto demonstra como integrar testes de API utilizando Postman + Newman com Jenkins, criando um pipeline de CI básico para automação de testes.

## 🔧 Tecnologias Utilizadas

- [Postman](https://www.postman.com/)
- [Newman](https://www.npmjs.com/package/newman)
- [Jenkins](https://www.jenkins.io/)
- Git e GitHub

## 📁 Estrutura do Projeto

```
qa-jenkins-project/
├── collections/
│   └── collection.postman.json      # Coleção Postman com testes de API
├── docs/
│   └── TEST-PLAN.md                 # Plano de testes
├── test-cases/
│   └── test-cases.xlsx              # Planilha com casos de teste
├── Jenkinsfile                      # Pipeline do Jenkins
└── README.md                        # Este arquivo
```

## ▶️ Como Executar os Testes Manualmente

1. Instale o [Node.js](https://nodejs.org/)
2. Instale o Newman:
   ```bash
   npm install -g newman
   ```
3. Execute a coleção:
   ```bash
   newman run collections/collection.postman.json -r cli,html --reporter-html-export resultado.html
   ```

## 🤖 Como Executar os Testes com Jenkins

1. Instale o Jenkins localmente
2. Instale os plugins:
   - Git Plugin
   - Pipeline
   - HTML Publisher Plugin

3. Crie um novo Pipeline no Jenkins
4. Configure o repositório GitHub do projeto
5. Use o `Jenkinsfile` incluído para automatizar:
   - Clonagem do repositório
   - Execução dos testes com Newman
   - Geração de relatório HTML

## 📋 Plano e Casos de Teste

- Plano de Testes: `docs/TEST-PLAN.md`
- Casos de Teste: `test-cases/test-cases.xlsx`
- Endpoint de exemplo: `GET /produtos`

## 📄 Relatório

O relatório HTML será gerado como `resultado.html` após a execução dos testes.

## 💡 Próximos passos

- Adicionar testes de login (API e Front-end)
- Integrar testes com Cypress
- Simular ambiente com Docker

---

Desenvolvido para fins educacionais e de portfólio na área de QA 🚀
