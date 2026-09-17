"""Renombra PDFs a partir del texto extraído de su primera página.
Usar DRY_RUN=1 para revisar cambios sin modificar archivos.
"""
import os, re
from pathlib import Path
import pdfplumber

PDF_DIR = Path(os.getenv("PDF_DIR", "/pdfs"))
DRY_RUN = os.getenv("DRY_RUN", "1") != "0"

def nombre_desde_pdf(path: Path) -> str:
    with pdfplumber.open(path) as pdf:
        texto = pdf.pages[0].extract_text() or ""
    # Ajustar este patrón al formato real del recibo; no depende del orden de glob.
    match = re.search(r"(?:apellido\s+y\s+nombre|nombre)\s*:?\s*([A-Za-zÁÉÍÓÚÜÑáéíóúüñ .'-]+)", texto, re.I)
    if not match:
        raise ValueError(f"No se encontró el nombre en {path.name}")
    nombre = re.sub(r"\s+", " ", match.group(1)).strip()
    return re.sub(r"[^A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9 ._-]", "", nombre).title()

def main() -> None:
    archivos = sorted(PDF_DIR.glob("*.pdf"))
    cambios = []
    for archivo in archivos:
        nombre = nombre_desde_pdf(archivo)
        destino = archivo.with_name(f"{archivo.stem} - {nombre}{archivo.suffix}")
        cambios.append((archivo, destino))
    for origen, destino in cambios:
        print(f"{origen.name} -> {destino.name}")
        if not DRY_RUN and origen != destino:
            destino = destino.with_name(destino.name if not destino.exists() else f"{destino.stem} (copia){destino.suffix}")
            origen.rename(destino)
    print(f"Procesados: {len(cambios)} | modo: {'simulación' if DRY_RUN else 'escritura'}")

if __name__ == "__main__":
    main()
