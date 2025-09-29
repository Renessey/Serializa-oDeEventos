# PROVA P1 - PARTE 2

Este repositório contém a implementação da **entidade `Category`** com funcionalidades avançadas de **serialização** e **eventos de domínio**, conforme solicitado na Prova P1 – Parte 2.

O projeto foi desenvolvido utilizando **Python**, **dataclasses**, e conceitos de **Domain-Driven Design (DDD)**.

---

## Funcionalidades Ministradas

### 1. `@staticmethod`
- Um método estático é um método que **não depende da instância** da classe.
- Pode ser chamado diretamente pela classe, sem precisar criar um objeto.
- Exemplo:

```python
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

print(MathHelper.add(5, 3))  # Saída: 8
