IVA = 0.16  # Constante del IVA

def precio_final(costo: float) -> float:
    """Calcula el precio final de un producto con IVA incluido."""
    return costo * (1 + IVA)

costo_producto = 200
total = precio_final(costo_producto)

print(f"El costo del producto con IVA es: ${total:.2f}")
