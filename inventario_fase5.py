"""Fase 5: cálculo de cantidades para reabastecer un inventario."""


def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """Devuelve las unidades faltantes, o cero si hay suficiente inventario."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def mostrar_reporte(inventario):
    """Recorre la matriz e informa la cantidad a pedir de cada artículo."""
    print("REPORTE DE REABASTECIMIENTO")
    print("-" * 50)

    for articulo in inventario:
        codigo, nombre, stock_actual, stock_minimo = articulo
        cantidad = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        print(f"{nombre} ({codigo}): solicitar {cantidad} unidades")


def main():
    # Matriz: [código, nombre, stock actual, stock mínimo requerido].
    inventario = [
        ["A001", "Cuadernos", 4, 10],
        ["A002", "Lápices", 15, 12],
        ["A003", "Borradores", 3, 8],
        ["A004", "Carpetas", 6, 6],
        ["A005", "Marcadores", 2, 7],
    ]
    mostrar_reporte(inventario)


if __name__ == "__main__":
    main()
