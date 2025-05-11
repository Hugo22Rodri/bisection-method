import sympy as sp

def biseccion(datos):
    try:
        x = sp.Symbol("x")
        f = sp.sympify(datos["ecuacion"])
        a = float(datos["a"])  # Conversión explícita a float
        b = float(datos["b"])
        tol = float(datos["tolerancia"])

        # Validar que el intervalo sea válido
        if f.subs(x, a) * f.subs(x, b) >= 0:
            return {"error": "Intervalo inválido: no garantiza una raíz."}

        pasos = []
        while abs(b - a) > tol:
            c = (a + b) / 2
            fc = float(f.subs(x, c).evalf())  # Valor exacto como float
            pasos.append((a, b, c, fc))  # Sin redondeo

            # Actualización directa del intervalo
            a, b = (a, c) if f.subs(x, a) * fc < 0 else (c, b)

        return {"raiz": (a + b) / 2, "pasos": pasos}  # Resultado exacto
    except Exception as e:
        return {"error": f"Error: {str(e)}"}