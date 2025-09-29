from entities.category import Category

def print_events_timeline(category):
    print("\n=== Timeline de Eventos ===")
    for idx, event in enumerate(category.events, start=1):
        event_name = event.__class__.__name__
        timestamp = getattr(event, "timestamp", "N/A")
        changed_fields = getattr(event, "changed_fields", "")
        if changed_fields:
            print(f"{idx}. {timestamp} - {event_name}: {changed_fields}")
        else:
            print(f"{idx}. {timestamp} - {event_name}")
    print("===========================\n")

# -------------------
# Criação da categoria
# -------------------
cat = Category(id=None, name="Eletrônicos", description="Produtos eletrônicos diversos")
print("Categoria criada:", cat.to_dict())
print_events_timeline(cat)

# -------------------
# Atualização
# -------------------
cat.update(name="Eletrônicos e Gadgets", description="Produtos eletrônicos e gadgets")
print("Após atualização:", cat.to_dict())
print_events_timeline(cat)

# -------------------
# Desativação
# -------------------
cat.deactivate()
print("Após desativação:", cat.to_dict())
print_events_timeline(cat)

# -------------------
# Ativação
# -------------------
cat.activate()
print("Após ativação:", cat.to_dict())
print_events_timeline(cat)

# -------------------
# Serialização e reconstrução
# -------------------
serialized = cat.to_dict()
cat_copy = Category.from_dict(serialized)
print("Categoria reconstruída a partir de dict:", cat_copy.to_dict())
