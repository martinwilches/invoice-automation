from datetime import datetime

REQUIRED_FILES = {
    "invoice_number",
    "supplier",
    "date",
    "subtotal",
    "tax",
    "total"
}

def validate_invoice(invoice: dict) -> list[str]:
    errors = []

    missing_fields = REQUIRED_FILES - invoice.keys()

    if missing_fields:
        errors.append(
            f"faltan campos obligatorios : {', '.join(sorted(missing_fields))}"
        )

    if not invoice["invoice_number"].strip():
        errors.append("El numero de factura esta vacio")

    if not invoice["supplier"]:
        errors.append("El proveedor esta vacio")

    try:
        datetime.fromisoformat(invoice["date"])
    except ValueError:
        errors.append("La fecha no tiene un formato valido")

    amounts = {}

    for field in ("subtotal", "tax", "total"):
        try:
            value = int(invoice[field])

            if value < 0:
                errors.append(f"{field} no puede ser negativo")
            else:
                amounts[field] = value
        except ValueError:
            errors.append(f"{field} debe ser un numero entero")

    if len(amounts) == 3:
        expected_total = amounts["subtotal"] + amounts["tax"]

        if amounts["total"] != expected_total:
            errors.append(
                f"Total incorrecto: se esperaba {expected_total}"
            )

    return errors