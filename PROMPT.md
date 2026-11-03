# PROMPT — TB-RR (Hackathon FACI 2026)

Estás en la raíz del proyecto. Haz `git init` aquí. Se entrega HOY, en menos de 20
minutos. Prioriza README + ficha técnica por encima del código.

## CONTEXTO CRÍTICO — LEE ESTO ANTES DE ESCRIBIR NADA

Ya existen **GenTB** (Harvard; web, gratis, random forest + red wide-and-deep, 13
fármacos, AGPLv3) y **TB-Profiler** (LSHTM; estándar de facto, abierto). Un
predictor más de resistencia NO aporta nada, y el jurado hará la pregunta asesina:
*"¿por qué no usan TB-Profiler?"*.

Por eso este proyecto **NO es un predictor**. Es un **benchmark peruano**:

> Primera evaluación del desempeño de las herramientas genómicas de predicción de
> resistencia a tuberculosis sobre aislados peruanos.

**Qué hacemos:** correr TB-Profiler, el catálogo de mutaciones de la OMS (2.ª ed.)
y un modelo propio sobre los aislados **peruanos** del compendio CRyPTIC, y medir
sensibilidad y especificidad **fármaco por fármaco, en linajes peruanos**. El
modelo propio es un cuarto competidor, no el protagonista.

**Por qué gana:** nadie ha publicado esto para Perú — las métricas publicadas son
promedios mundiales dominados por el linaje 4. El entregable es una frase
accionable para el INS: *"si adoptan secuenciación, esto es lo que pueden esperar
en el Perú, fármaco por fármaco, y en estos no confíen todavía"*.

Esto además invierte la pregunta asesina: ya no es "¿por qué no usan TB-Profiler?"
sino "usamos TB-Profiler, y medimos dónde falla en el Perú".

## DATOS (abiertos, sin registro)

- **Compendio CRyPTIC**: 12 289 aislados con fenotipo de resistencia a 13
  antibióticos. https://doi.org/10.1371/journal.pbio.3001721
  Tabla `reuse` en `ftp.ebi.ac.uk/pub/databases/cryptic/reuse/`; copia en Crick
  figshare.
- **Catálogo OMS, 2.ª ed.**:
  https://www.who.int/publications-detail-redirect/9789240082410
- **VERIFICA EN EL CSV** cuántos aislados son peruanos. No lo asumas: cuéntalo y
  reporta el número real. Si el FTP no responde, dilo — no inventes la cifra.
- Referencia del brazo peruano (INS + UPCH): Puyén et al., *BMC Infect Dis* 2022,
  https://doi.org/10.1186/s12879-022-07677-9

## CLAVE METODOLÓGICA

- La partición train/test va **por linaje, nunca al azar** (Billows et al. 2023,
  https://doi.org/10.1093/bioinformatics/btad428). Con partición aleatoria el
  desempeño se sobreestima.
- Reporta sensibilidad y especificidad con **IC 95 %**.
- Los 13 fármacos de CRyPTIC incluyen **bedaquilina, delamanid, linezolid y
  clofazimina** — justo los que GenTB **no** cubre. Ese es el foco del análisis de
  discrepancias.

## ENTREGABLES (en este orden de prioridad)

1. `README.md` en español: qué es, por qué, cómo correrlo, limitaciones honestas.
2. `docs/ficha-tecnica.md` siguiendo la plantilla oficial de la UPCH (apartados
   1–10: Introducción, Problematización, Objetivos, ODS, Diseño del proyecto,
   Resultados esperados, Colaboración, Plan de implementación, Declaración de uso
   de IA, Referencias). Arial 11, interlineado 1.5, máx. 10 páginas. Exportable a
   PDF como `Reto1_TB-RR.pdf`.
3. Notebook o script reproducible: descarga → tabla aislado × variante × fenotipo
   → modelos por fármaco con partición por linaje → comparación contra el catálogo
   OMS → tabla de discrepancias.
4. App web mínima (Streamlit): subes una lista de variantes → resultado por
   fármaco con la mutación responsable y su clase OMS; segunda vista con el
   benchmark. Despliegue en Streamlit Community Cloud (gratis, sin costo
   variable).

## REGLAS DE HONESTIDAD (no negociables — el jurado penaliza lo contrario)

- Si algo no está hecho, la ficha dice que está **programado**, no logrado.
- Ningún número inventado. Si no corriste el experimento, el campo va vacío y
  visible como `[PENDIENTE]`.
- La herramienta es **de apoyo a investigación y vigilancia**: no diagnostica, no
  sustituye el cultivo ni el criterio clínico. Dilo explícitamente.
- Incluye la declaración de uso de IA.

## URGENTE — 20 MINUTOS

Entrega en este orden y commitea apenas tengas cada uno:
1) `README.md` → 2) `docs/ficha-tecnica.md` → 3) lo que alcance de código.
No pulas nada hasta tener los tres. **Primer commit en los primeros 5 minutos.**

Al final, crea el repo:

```bash
gh repo create tb-rr --public --source=. --push
```

Avísame con la URL del repo apenas exista.
