# TB-RR: primera evaluación del desempeño de las herramientas genómicas de predicción de resistencia a TB sobre aislados peruanos

**Hackathon FACI 2026 · UPCH · Reto 1**
**Integrantes:** [Integrantes: PENDIENTE]
**Repositorio:** https://github.com/IchiSieben/tb-rr
**Fecha de la ficha:** 2 de noviembre de 2026

> Formato de entrega: Arial 11, interlineado 1.5, máx. 10 páginas; exportar a PDF como Reto1_TB-RR.pdf.

> Convención de esta ficha: toda cifra presentada como resultado proviene de `src/01_count_peru.py`, ejecutado el 2026-11-02 sobre tablas abiertas de CRyPTIC. Todo análisis aún no ejecutado está marcado **[PENDIENTE]** y no constituye resultado.

---

## 1. Introducción

Varias herramientas genómicas predicen resistencia de *Mycobacterium tuberculosis* a partir del genoma del aislado: TB-Profiler (LSHTM), el catálogo de mutaciones de la OMS (2.ª edición, 2023) y otras como GenTB (Harvard). Se han validado sobre colecciones internacionales. No existe, hasta donde conocemos, una medición de su desempeño sobre aislados peruanos, fármaco por fármaco.

TB-RR no propone un predictor nuevo de resistencia. Es un **benchmark peruano**: aplica las herramientas existentes a genomas de aislados de Lima, con fenotipo conocido, y mide dónde aciertan y dónde fallan. Compara tres competidores: TB-Profiler, el catálogo OMS 2023 y un modelo propio. El modelo propio es el cuarto elemento de la comparación, no el protagonista.

El producto accionable para el Instituto Nacional de Salud (INS) es una respuesta concreta: *si adoptan secuenciación, esto es lo que pueden esperar en el Perú, fármaco por fármaco, y en estos fármacos no confíen todavía.*

Herramienta de apoyo a investigación y vigilancia. No diagnostica y no sustituye el cultivo, la prueba de sensibilidad fenotípica ni el criterio clínico.

## 2. Problematización

**Problema clínico.** El cultivo y la prueba de sensibilidad fenotípica tardan semanas. Mientras tanto, el paciente recibe un esquema empírico. Dato proporcionado por el equipo (fuente MINSA por confirmar): 29 292 casos de TB en el Perú en 2022, 56 % en Lima y Callao.

**Brecha de evidencia.** La secuenciación puede acortar ese intervalo, pero para decidir si conviene adoptarla se necesita saber cuánto se puede confiar en la predicción sobre la población local. Las herramientas se evalúan sobre colecciones globales; el desempeño en el Perú no se ha reportado fármaco por fármaco.

**Pregunta de partida y su inversión.** Una pregunta natural es "¿por qué no usan TB-Profiler?". La respuesta del proyecto es que sí se usa: TB-Profiler es uno de los competidores y se mide dónde falla en el Perú. GenTB se menciona como contexto: no cubre bedaquilina, delamanid, linezolid ni clofazimina, que son precisamente los fármacos de los esquemas nuevos.

**Hallazgo preliminar verificado.** El conteo de aislados peruanos en los datos abiertos de CRyPTIC muestra que, para los fármacos nuevos, la evidencia local es mínima: 3 aislados resistentes a bedaquilina, 9 a delamanid, 1 a linezolid y 10 a clofazimina (sección 5). Con esos números la sensibilidad no puede estimarse con precisión útil. Esto es en sí un mensaje para el INS: para esos cuatro fármacos la base de evidencia peruana es insuficiente y la prueba fenotípica sigue siendo necesaria.

**Corrección de una hipótesis inicial.** Se asumía que los promedios globales estarían dominados por el linaje 4 y que eso perjudicaba al Perú. Los datos muestran que los aislados peruanos son también mayoritariamente linaje 4 (85,6 %). El contraste relevante es otro: linaje 2 (Beijing; 340 aislados, 12,9 %) frente a linaje 4. Es una pregunta que se podrá responder con los datos disponibles.

## 3. Objetivos

**Objetivo general.** Evaluar el desempeño de herramientas genómicas de predicción de resistencia a TB sobre aislados peruanos y traducirlo en una guía fármaco por fármaco sobre qué se puede y qué no se puede esperar de la secuenciación en el Perú.

**Hallazgo que reordena los objetivos.** El benchmark peruano es **posible en primera línea y
fluoroquinolonas/aminoglucósidos, e inviable hoy en los fármacos nuevos** (bedaquilina,
delamanid, linezolid, clofazimina) por escasez de fenotipos resistentes en la cohorte peruana
(3, 9, 1 y 10 aislados). No es un defecto del proyecto que se esconda: es una conclusión en sí
misma, verificable y citable. Los objetivos se separan en consecuencia.

**Objetivos específicos.**

1. Caracterizar la base de aislados peruanos disponible en datos abiertos: tamaño, linajes y número de resistentes por fármaco. *(Logrado.)*
2. Cuantificar, por fármaco, si la cohorte peruana tiene potencia para estimar la sensibilidad, y declarar formalmente inviables los que no la tienen. *(Logrado: ver tabla de potencia en 5.1.)*
3. **Fármacos con potencia** (RIF, RFB, INH, EMB, ETH, LEV, MXF, AMI, KAN): ejecutar TB-Profiler y el catálogo OMS 2023, entrenar un modelo propio con partición por linaje, y estimar sensibilidad y especificidad con IC 95 % (Wilson), con contraste L2 frente a L4. *(Programado.)*
4. **Fármacos sin potencia** (BDQ, DLM, LZD, CFZ): no entrenar ni reportar sensibilidad. Solo describir caso a caso los aislados resistentes (qué mutación tienen, qué predice cada herramienta) y estimar especificidad, que sí tiene potencia (más de 2 500 susceptibles por fármaco). *(Programado.)*
5. Publicar los resultados en una aplicación Streamlit y un repositorio reproducible. *(Programado.)*

**Indicadores.**

| Indicador | Meta | Estado |
|---|---|---|
| Aislados peruanos identificados con país verificado | Cifra exacta, reproducible por script | **Logrado: 2 638** |
| Fármacos clasificados por potencia (estimable / inviable) | 13 de 13 | **Logrado: 9 estimables, 4 inviables** |
| Fármacos estimables con sensibilidad y especificidad + IC 95 %, por herramienta | 9 × 3 herramientas | [PENDIENTE] |
| Ancho del IC 95 % de la sensibilidad en fármacos estimables | ≤ 10 puntos porcentuales | [PENDIENTE] |
| Contraste L2 frente a L4 en RIF e INH | Diferencia con IC 95 % | [PENDIENTE] |
| Especificidad en BDQ, DLM, LZD, CFZ con IC 95 % | 4 fármacos × 3 herramientas | [PENDIENTE] |
| Descripción caso a caso de los 23 aislados resistentes a fármacos nuevos | 23 de 23 | [PENDIENTE] |
| App Streamlit pública | URL activa | [PENDIENTE] |

## 4. Objetivos de Desarrollo Sostenible

**ODS 3, Salud y bienestar. Meta 3.3:** poner fin a las epidemias de tuberculosis, entre otras enfermedades transmisibles. Conocer cuán confiable es la predicción genómica de resistencia en el Perú informa la decisión de incorporar secuenciación y, con ello, la elección oportuna de esquemas.

**ODS 9, Industria, innovación e infraestructura** (complementario). Evaluación abierta de herramientas bioinformáticas sobre datos locales, reutilizable por laboratorios de referencia.

**ODS 17, Alianzas para lograr los objetivos** (complementario). El proyecto se apoya en datos de un consorcio internacional (CRyPTIC) y en la articulación entre la UPCH y el INS.

## 5. Diseño del proyecto

### 5.1 Datos

Fuente: tablas abiertas del consorcio CRyPTIC, publicación de junio de 2022 (ftp.ebi.ac.uk/pub/databases/cryptic/release_june2022/). La tabla de reutilización `CRyPTIC_reuse_table_20240917.csv` tiene **12 287 filas**; el artículo reporta 12 289 aislados. No se ha resuelto la diferencia de 2 aislados y se reporta tal cual.

El país no figura en la tabla de reutilización ni en los metadatos de ENA. Se obtiene de `reproducibility/data_tables/cryptic-analysis-group/SAMPLES.csv.gz` (campo `COUNTRY_WHERE_SAMPLE_TAKEN`) y `SITES.csv` (sitio 05 = Universidad Peruana Cayetano Heredia, Lima).

**Aislados peruanos en la tabla de reutilización: 2 638**, todos del sitio 05. Otras 5 filas del sitio 05 no tienen país asignado en el cruce y quedan fuera del conteo.

**Linajes (Mykrobe) de los 2 638 aislados:**

| Linaje | Aislados | % |
|---|---|---|
| Linaje 4 | 2 259 | 85,6 |
| Linaje 2 (Beijing) | 340 | 12,9 |
| Mixto | 37 | 1,4 |
| Linaje 1 | 1 | <0,1 |
| *M. bovis* | 1 | <0,1 |

**Fenotipos binarios en aislados peruanos (R / I / S):**

| Fármaco | R | I | S |
|---|---|---|---|
| Rifampicina (RIF) | 853 | 0 | 1 738 |
| Rifabutina (RFB) | 719 | 0 | 1 881 |
| Isoniacida (INH) | 1 151 | 0 | 1 424 |
| Etambutol (EMB) | 371 | 317 | 1 909 |
| Etionamida (ETH) | 289 | 129 | 2 198 |
| Levofloxacino (LEV) | 168 | 0 | 2 453 |
| Moxifloxacino (MXF) | 143 | 0 | 2 478 |
| Amikacina (AMI) | 159 | 0 | 2 460 |
| Kanamicina (KAN) | 179 | 0 | 2 432 |
| Bedaquilina (BDQ) | 3 | 0 | 2 588 |
| Delamanid (DLM) | 9 | 0 | 2 566 |
| Linezolid (LZD) | 1 | 0 | 2 617 |
| Clofazimina (CFZ) | 10 | 0 | 2 578 |

**Lectura: análisis de potencia.** La tabla siguiente no es un resultado de desempeño: es
aritmética sobre los conteos. Muestra la cota inferior del IC 95 % (Wilson) de la sensibilidad
**en el mejor caso posible**, es decir, si una herramienta detectara el 100 % de los
resistentes.

| Fármaco | Resistentes peruanos | Cota inferior del IC 95 % si sensibilidad observada = 100 % | Veredicto |
|---|---:|---:|---|
| RIF | 853 | 99,6 % | Estimable |
| INH | 1 151 | 99,7 % | Estimable |
| LEV | 168 | 97,8 % | Estimable |
| MXF | 143 | 97,4 % | Estimable |
| AMI | 159 | 97,6 % | Estimable |
| KAN | 179 | 97,9 % | Estimable |
| CFZ | 10 | 72,2 % | **Inviable** |
| DLM | 9 | 70,1 % | **Inviable** |
| BDQ | 3 | 43,8 % | **Inviable** |
| LZD | 1 | 20,7 % | **Inviable** |

Aun con un acierto perfecto, en bedaquilina solo se podría afirmar que la sensibilidad está
por encima del 44 %, y en linezolid por encima del 21 %. Ninguna decisión de salud pública
puede apoyarse en eso. Conclusión: **el benchmark peruano es posible en primera línea e
inviable hoy en fármacos nuevos por escasez de fenotipos resistentes en la cohorte peruana.**
Lo que se necesita para cerrarlo no es un modelo mejor sino más aislados peruanos resistentes
a fármacos nuevos con fenotipo, que solo puede generar la vigilancia del INS.

**Limitaciones de los datos.** Los aislados provienen de un único sitio (Lima, UPCH). Los datos son de CRyPTIC, no del INS; la coincidencia con la población que atiende el INS no está verificada. No se usan datos de pacientes ni datos no públicos.

### 5.2 Método (planificado)

1. **Predicción.** TB-Profiler y catálogo OMS 2023 sobre los genomas peruanos. **[PENDIENTE]**
2. **Modelo propio.** Partición entrenamiento/prueba **por linaje, nunca aleatoria**, siguiendo Billows et al. (2023), para evitar que la proximidad filogenética infle las métricas. **[PENDIENTE]**
3. **Métricas.** Sensibilidad y especificidad por fármaco, con intervalo de confianza de 95 % de Wilson, por herramienta y estratificadas por linaje (L2 frente a L4). **[PENDIENTE]**
4. **Análisis de discrepancias.** Casos donde las herramientas discrepan entre sí o con el fenotipo, con foco en BDQ, DLM, LZD y CFZ. **[PENDIENTE]**
5. **Tratamiento de intermedios.** Para EMB y ETH, que tienen aislados intermedios (317 y 129), se definirá y declarará el criterio antes de calcular métricas. **[PENDIENTE]**

Tabla de métricas (a completar tras la ejecución):

| Fármaco | Herramienta | Sensibilidad (IC 95 % Wilson) | Especificidad (IC 95 % Wilson) |
|---|---|---|---|
| RIF | TB-Profiler | [PENDIENTE] | [PENDIENTE] |
| RIF | Catálogo OMS 2023 | [PENDIENTE] | [PENDIENTE] |
| RIF | Modelo propio | [PENDIENTE] | [PENDIENTE] |
| (resto de fármacos) | (ídem) | [PENDIENTE] | [PENDIENTE] |

### 5.3 Arquitectura

- `src/01_count_peru.py`: conteo de aislados peruanos, linajes y fenotipos desde datos abiertos (ejecutado).
- Scripts de predicción y evaluación (TB-Profiler, catálogo OMS, modelo propio, métricas): **[PENDIENTE]**.
- Aplicación Streamlit con tabla por fármaco y mensaje de confianza ("confiar / no confiar todavía"): **[PENDIENTE]**.
- Todo el código y las tablas derivadas en el repositorio público; sin datos de pacientes.

## 6. Resultados esperados

Resultados ya obtenidos (sección 5.1): tamaño de la base peruana (2 638 aislados), distribución de linajes, número de resistentes por fármaco y **clasificación de potencia: 9 fármacos estimables y 4 inviables (BDQ, DLM, LZD, CFZ)**. Este último es un resultado citable por sí mismo: el benchmark peruano es posible en primera línea e inviable hoy en fármacos nuevos por escasez de fenotipos resistentes.

Resultados esperados al cierre del proyecto (no obtenidos aún):

1. Tabla de desempeño por fármaco y herramienta sobre aislados peruanos, con IC de Wilson.
2. Contraste de desempeño entre linaje 2 y linaje 4.
3. Una clasificación fármaco por fármaco para el INS en tres categorías: fármacos con evidencia suficiente y desempeño estimable; fármacos con evidencia insuficiente, donde se mantiene la prueba fenotípica; y discrepancias a revisar.
4. Aplicación Streamlit y repositorio reproducible.

No se anticipan cifras de desempeño: dependen de la ejecución pendiente.

## 7. Colaboración

- **UPCH:** origen de los aislados peruanos (sitio 05 de CRyPTIC) y de la convocatoria. Rol propuesto: validación de la interpretación de los datos locales.
- **INS:** destinatario de la guía fármaco por fármaco. Puyén et al. (2022) documentan el brazo peruano de CRyPTIC (INS + UPCH). Contacto y rol en el proyecto: [PENDIENTE de confirmar].
- **CRyPTIC, LSHTM (TB-Profiler) y OMS:** proveedores de datos y herramientas abiertas; no participan en el proyecto.
- **Equipo:** [Integrantes: PENDIENTE].

## 8. Plan de implementación

| Actividad | Entregable | Estado |
|---|---|---|
| Conteo de aislados peruanos, linajes y fenotipos en datos abiertos | `src/01_count_peru.py` y cifras de la sección 5.1 | Logrado |
| Definición de la pregunta como benchmark y de los competidores | Esta ficha | Logrado |
| Descarga de genomas/variantes de los 2 638 aislados | Conjunto local de trabajo | Programado |
| Ejecución de TB-Profiler | Predicciones por aislado | Programado |
| Aplicación del catálogo OMS 2023 | Predicciones por aislado | Programado |
| Modelo propio con partición por linaje | Modelo y predicciones | Programado |
| Sensibilidad/especificidad con IC de Wilson, por fármaco y linaje | Tabla de métricas | Programado |
| Análisis de discrepancias (BDQ, DLM, LZD, CFZ) | Tabla de discrepancias | Programado |
| Aplicación Streamlit | App desplegada | Programado |
| Guía para el INS y presentación final | Documento y demo | Programado |

## 9. Declaración de uso de IA

Se usó Claude (Anthropic, mediante Claude Code) para redactar el README, esta ficha, la página web del proyecto y el script de conteo de datos. El equipo revisó el material generado. Todas las cifras presentadas como resultado provienen de la ejecución del script sobre datos abiertos. No se usaron datos de pacientes. La IA no inventó resultados: los análisis aún no ejecutados están marcados como **[PENDIENTE]**.

## 10. Referencias

1. The CRyPTIC Consortium (2022). A data compendium associating the genomes of 12,289 *Mycobacterium tuberculosis* isolates with quantitative resistance phenotypes to 13 antibiotics. *PLoS Biology* 20(8): e3001721. doi:10.1371/journal.pbio.3001721
2. World Health Organization (2023). *Catalogue of mutations in Mycobacterium tuberculosis complex and their association with drug resistance*, 2.ª ed. ISBN 9789240082410.
3. Billows N. et al. (2023). *Bioinformatics*. doi:10.1093/bioinformatics/btad428
4. Puyén Z.M. et al. (2022). *BMC Infectious Diseases*. doi:10.1186/s12879-022-07677-9
5. Phelan J.E. et al. (2019). TB-Profiler. *Genome Medicine* 11:41.
6. Gröschel M.I. et al. (2021). GenTB. *Genome Medicine* 13:138.
7. Hunt M. et al. (2019). Mykrobe. *Wellcome Open Research*.
