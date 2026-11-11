from pathlib import Path # Ruta del sistema de archivos

def read_invoice(file_path: Path) -> dict:
    invoice = {}

    # open() permite abrir el documento
    with file_path.open('r', encoding='utf-8') as file:
        # enumerate permite recorrer lineas con su indice (line_number)
        for line_number, line in enumerate(file, start=1):

            line = line.strip()

            if not line:
                continue

            # validar que en cada linea este presente el caracter "=" (clave=valor)
            if "=" not in line:
                raise ValueError(
                    f"Formato inválido en la línea {line_number}"
                )

            # separar el nombre del campo y su valor
            key, value = line.split('=', maxsplit=1)

            key = key.strip()
            value = value.strip()

            # validar que la clave tenga un valor valido
            if not key:
                raise ValueError(
                    f"Campo vacío en la línea {line_number}"
                )

            # validar que la clave no este duplicada en la factura
            if key in invoice:
                raise ValueError(
                    f"Campo duplicado: {key}"
                )

            invoice[key] = value

        return invoice