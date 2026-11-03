# TB-RR · Benchmark peruano de predicción genómica de resistencia a tuberculosis

> Hackathon FACI 2026 · UPCH · Reto 1 · Página: https://ichisieben.github.io/tb-rr/

## Qué es

**No es un predictor de resistencia más.** Ya existen TB-Profiler (LSHTM, estándar de facto)
y GenTB (Harvard). TB-RR es la **primera evaluación del desempeño de esas herramientas sobre
aislados peruanos**, fármaco por fármaco:

| Competidor | Rol |
|---|---|
| TB-Profiler | Estándar de facto, abierto |
| Catálogo de mutaciones OMS, 2.ª ed. (2023) | Referencia normativa |
| Modelo propio por fármaco | Cuarto competidor, no protagonista |

La pregunta del jurado "¿por qué no usan TB-Profiler?" se invierte: **usamos TB-Profiler y
medimos dónde falla en el Perú.**

Entregable para el INS: *si adoptan secuenciación, esto es lo que pueden esperar en el Perú,
fármaco por fármaco, y en estos no confíen todavía.*

## Por qué

Las métricas publicadas de estas herramientas son promedios mundiales. No hay una evaluación
publicada restringida a aislados peruanos, y la decisión de adoptar secuenciación en el país
necesita números del país.

## Datos verificados hoy (2026-11-02)

Fuente: compendio CRyPTIC, datos abiertos sin registro
(`ftp.ebi.ac.uk/pub/databases/cryptic/release_june2022/`). Script: `src/01_count_peru.py`.

- La tabla `reuse` (`CRyPTIC_reuse_table_20240917.csv`) tiene **12 287 filas** (el artículo
  reporta 12 289 aislados).
- La tabla `reuse` **no trae país**, y los metadatos de ENA tampoco. El país sale de
  `SAMPLES.csv.gz` (`COUNTRY_WHERE_SAMPLE_TAKEN`) y `SITES.csv` (sitio 05 = UPCH, Lima).
- **Aislados peruanos: 2 638.**
- Linajes (Mykrobe): L4 = 2 259 (85,6 %), L2 = 340 (12,9 %), mixtos = 37, L1 = 1, bovis = 1.

Fenotipo binario en los 2 638 aislados peruanos:

| Fármaco | R | I | S |
|---|---:|---:|---:|
| Rifampicina (RIF) | 853 | 0 | 1 738 |
| Rifabutina (RFB) | 719 | 0 | 1 881 |
| Isoniazida (INH) | 1 151 | 0 | 1 424 |
| Etambutol (EMB) | 371 | 317 | 1 909 |
| Etionamida (ETH) | 289 | 129 | 2 198 |
| Levofloxacino (LEV) | 168 | 0 | 2 453 |
| Moxifloxacino (MXF) | 143 | 0 | 2 478 |
| Amikacina (AMI) | 159 | 0 | 2 460 |
| Kanamicina (KAN) | 179 | 0 | 2 432 |
| **Bedaquilina (BDQ)** | **3** | 0 | 2 588 |
| **Delamanid (DLM)** | **9** | 0 | 2 566 |
| **Linezolid (LZD)** | **1** | 0 | 2 617 |
| **Clofazimina (CFZ)** | **10** | 0 | 2 578 |

**Primer hallazgo, honesto:** con 1 a 10 aislados resistentes, la sensibilidad para
bedaquilina, delamanid, linezolid y clofazimina **no puede estimarse con precisión útil** en
el Perú con estos datos. Es justo el grupo que GenTB no cubre y el que más importa para los
esquemas nuevos. Aun con acierto perfecto, la cota inferior del IC 95 % (Wilson) de la
sensibilidad sería 43,8 % en BDQ, 70,1 % en DLM, 20,7 % en LZD y 72,2 % en CFZ (aritmética
sobre los conteos, no un resultado de desempeño). Conclusión: **el benchmark peruano es
posible en primera línea e inviable hoy en fármacos nuevos por escasez de fenotipos
resistentes en la cohorte peruana.** Para esos fármacos solo se estimará especificidad y se
describirán caso a caso los 23 resistentes; la prueba fenotípica sigue siendo imprescindible.

Matiz: el Perú también es mayoritariamente linaje 4, así que el contraste relevante no es
"Perú vs. mundo L4" sino **L2 (Beijing, 340 aislados) frente a L4 dentro del Perú**.

## Método (programado)

1. Descarga → tabla aislado × variante × fenotipo (VCF regenotipados de CRyPTIC).
2. TB-Profiler y catálogo OMS 2.ª ed. aplicados a cada aislado peruano.
3. Modelo propio por fármaco con **partición train/test por linaje, nunca al azar**
   (Billows et al. 2023, doi:10.1093/bioinformatics/btad428).
4. Sensibilidad y especificidad por fármaco con **IC 95 % (Wilson)**.
5. Tabla de discrepancias, foco en BDQ, DLM, LZD y CFZ.
6. App Streamlit: subes variantes → resultado por fármaco con la mutación responsable y su
   clase OMS; segunda vista con el benchmark.

## Estado

| Pieza | Estado |
|---|---|
| Conteo de aislados peruanos, linajes y fenotipos | **Logrado** (`src/01_count_peru.py`) |
| Página pública (`index.html`) | **Logrado** |
| Ficha técnica (`docs/ficha-tecnica.md`) | **Logrado** (borrador) |
| TB-Profiler sobre aislados peruanos | Programado · métricas [PENDIENTE] |
| Catálogo OMS sobre aislados peruanos | Programado · métricas [PENDIENTE] |
| Modelo propio con partición por linaje | Programado · métricas [PENDIENTE] |
| Tabla de discrepancias | Programado [PENDIENTE] |
| App Streamlit + despliegue | Programado [PENDIENTE] |

## Cómo correrlo

```bash
python -m venv .venv && .venv/Scripts/activate   # Windows; en Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
python src/01_count_peru.py   # descarga ~6 MB y escribe data/peru_summary.csv y data/peru_isolates.csv
```

## Limitaciones

- **No es una herramienta diagnóstica.** Es de apoyo a investigación y vigilancia; no
  sustituye el cultivo, la prueba de sensibilidad fenotípica ni el criterio clínico.
- Los aislados peruanos de CRyPTIC vienen de un solo sitio (UPCH, Lima) y fueron
  seleccionados para el consorcio, con sobrerrepresentación de resistencia (RIF-R ≈ 33 %):
  no son una muestra representativa de los casos del país.
- Muy pocos resistentes a BDQ, DLM, LZD y CFZ: las métricas para esos fármacos tendrán
  intervalos de confianza muy anchos.
- Ninguna métrica de desempeño está calculada todavía. Las que faltan están marcadas
  `[PENDIENTE]`.

## Uso de IA

Claude (Anthropic, vía Claude Code) redactó el README, la ficha, la página y el script de
conteo; el equipo los revisó. Todas las cifras salen del script ejecutado sobre datos
abiertos. No se usaron datos de pacientes. Lo no ejecutado figura como `[PENDIENTE]`.

## Referencias

- The CRyPTIC Consortium (2022). *PLoS Biol* 20(8): e3001721. doi:10.1371/journal.pbio.3001721
- OMS (2023). Catálogo de mutaciones del complejo *M. tuberculosis*, 2.ª ed. ISBN 9789240082410
- Billows N. et al. (2023). *Bioinformatics*. doi:10.1093/bioinformatics/btad428
- Puyén Z.M. et al. (2022). *BMC Infect Dis*. doi:10.1186/s12879-022-07677-9
- Phelan J.E. et al. (2019). *Genome Med* 11:41 (TB-Profiler)
- Gröschel M.I. et al. (2021). *Genome Med* 13:138 (GenTB)

## Licencia

Código: MIT. Datos: de CRyPTIC, bajo sus términos; citar el artículo del compendio.
