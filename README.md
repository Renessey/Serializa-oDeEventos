# Projeto Category 

Este projeto implementa a **entidade `Category`** com funcionalidades de **serialização** e **eventos de domínio**, seguindo conceitos de **Domain-Driven Design (DDD)** e boas práticas de Python.

Ele foi desenvolvido como parte da **Prova P1 – Parte 2**, incluindo testes de criação, atualização e gerenciamento de eventos.

---

## Objetivo do Projeto

- Evoluir a entidade `Category` adicionando:
  1. **Serialização**: exportar e reconstruir a entidade de forma simples.
  2. **Eventos de Domínio**: registrar acontecimentos importantes no ciclo de vida da categoria (criação, atualização, ativação/desativação).
- Demonstrar conceitos de **@staticmethod, dataclasses, decoradores e DDD**.

---

## Funcionalidades Implementadas

### 1. Serialização
Permite converter a entidade para dicionário e reconstruí-la posteriormente.

- **`to_dict()`**: retorna um dicionário com todos os atributos da entidade, incluindo `class_name`.
- **`from_dict(data)`**: cria uma instância de `Category` a partir de um dicionário.

**Exemplo de uso:**

```python
cat_dict = cat.to_dict()
cat_copy = Category.from_dict(cat_dict)
```



