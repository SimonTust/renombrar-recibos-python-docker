# Renombrador de recibos PDF

Automatización en Python y Docker para extraer el nombre de la primera página de cada PDF y proponer un nombre consistente.

## Uso seguro

1. Colocar PDFs ficticios en una carpeta montada como `/pdfs`.
2. Ejecutar con `DRY_RUN=1` (valor predeterminado) y revisar la vista previa.
3. Usar `DRY_RUN=0` solamente cuando los nombres sean correctos.

La versión pública no incluye recibos reales ni rutas de la empresa. La extracción usada aquí es de texto; OCR puede incorporarse como una mejora separada para PDFs escaneados.
