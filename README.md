# GTA VI en PC / Xbox Series X — Informe de viabilidad

**Fecha de corte:** 24 de noviembre de 2026
**Caso:** intentar ejecutar en PC la build de Xbox Series X|S de GTA VI, con presupuesto mínimo y sin ordenador local.
**Documento:** investigación técnica, de mercado y legal. No es asesoramiento jurídico.

> **Aviso importante**
> En este informe **no incluyo enlaces ni instrucciones para descargar el ejecutable filtrado, descifrarlo, extraer claves ni eludir las protecciones de la consola**. Esa es exactamente la parte que Take-Two está persiguiendo con DMCA y demandas, y la que convierte el proyecto en delito en España y en EE. UU. El resto —qué existe, qué es real, qué se puede aprender y cómo jugar barato— sí está desarrollado.

---

## 0. Veredicto en 30 segundos

1. **GTA VI salió el 19-11-2026 en PS5 y Xbox Series X|S. No hay versión de PC anunciada.** El rumor más citado habla de Q1 2027, pero Rockstar no lo ha confirmado.
2. **No existe un emulador general de Xbox Series X|S.** Lo que hay son capas de compatibilidad y proyectos de recompilación experimentales que, en el mejor caso, arrancan el ejecutable filtrado y llegan a los menús. **Nada es jugable.**
3. **"La CPU es casi la misma" es cierto y a la vez irrelevante.** La CPU es x86-64 Zen 2, sí, pero el juego habla con un SO derivado de Windows, un hipervisor, las APIs `kernelx`/`d3d12_xs` del GDK y shaders RDNA2 propios. La compatibilidad de instrucciones es ~5 % del problema.
4. **El plan tal como lo planteas no se puede hacer con 0 € ni sin PC.** No por falta de talento, sino porque hace falta hardware Windows con GPU de 16 GB, el juego filtrado (ilegal) y meses/años de trabajo de un equipo.
5. **Lo que sí puedes hacer con 0 €:** aprender ingeniería inversa de verdad con herramientas libres y objetivos legales, y contribuir a proyectos open source compilando y pasando tests en la nube (sin hardware).
6. **Lo más barato para jugar GTA VI hoy en España:** Xbox One de segunda mano + el juego + horas de Xbox Cloud Gaming (la nube solo está habilitada en consolas Xbox), o una Series S usada. Desde un portátil puedes hacer **Remote Play** desde una consola que tenga el juego.

---

## 1. El vídeo: qué es y qué dice

| Dato | Valor |
|---|---|
| Título | *Is GTA 6 Really PORTED to PC? (fact checked)* |
| Canal | Code Bear (`@thecodebear`) |
| Publicación | 23-11-2026 |
| Views al analizarlo | ~13.940 |
| Enlace | https://www.youtube.com/watch?v=P0o-Fh-VSxo |

**Tesis del vídeo:** cuatro días después del lanzamiento, Internet se llenó de vídeos de "GTA 6 en PC". El grupo **Cyberleek/Cyberleak** había publicado el ejecutable de Xbox y varios equipos amateur competían por hacerlo arrancar en Windows. El autor divide el problema en **5 etapas** (arrancar, imagen, menús, mundo, jugable), revisa **41 clips virales** y concluye que algunos son reales, otros son falsos, y **los reales muestran mucho menos de lo que dicen los titulares**. No hay versión jugable. Los "descargas de GTA 6 PC" son malware.

**Capítulos:**

| Minuto | Capítulo |
|---|---|
| 0:00 | Ported to PC |
| 1:07 | One missing file |
| 2:12 | Why an Xbox game won't just run on PC |
| 4:33 | The race starts |
| 5:31 | Stage 1: does it start? |
| 5:58 | Stage 2: a picture |
| 6:28 | Stage 3: the menus |
| 7:12 | Stage 4: the world |
| 8:45 | Stage 5: playable? |
| 9:06 | Checking the viral clips |
| 12:29 | Leonida goes dark |
| 13:23 | Take-Two and the law |
| 14:40 | The scams |
| 15:25 | Where it really stands |

**Dos avisos sobre el propio vídeo:**

- YouTube lo etiqueta como **"Made with AI"** ("Sounds or visuals were altered or fully generated"). Úsalo como mapa y como lista de fuentes, no como prueba técnica definitiva.
- El vídeo dice que Take-Two no ha comentado el ejecutable, pero **sí hay una DMCA de Take-Two del 18-11-2026 en GitHub**. Ojo: esa DMCA **no es de GTA VI**, es del proyecto *Muguet* (un port de GTA V a iOS/macOS). Es igualmente relevante porque contiene la doctrina que te afecta: *"bring your own files" no te protege*. Lo detallo en la sección 5.

---

## 2. Todas las fuentes de la descripción del vídeo

Marqué con ✅ las que respondieron correctamente al comprobarlas y con ⚠️ las que bloquean bots o no pude verificar al 100 %.

### 2.1. Prensa y análisis

| Fuente | Enlace | Qué aporta |
|---|---|---|
| XDA — el .exe filtrado y los proyectos de recompilación | https://www.xda-developers.com/gta-6-xbox-executable-leaked-opening-door-for-pc-recompilation-projects-begin-testing/ | ⚠️ Bloquea acceso automatizado; citado en el vídeo |
| GamesRadar — "the game almost boots" | https://www.gamesradar.com/games/grand-theft-auto/gta-6-pc-version-is-close-modders-say-after-cyberleek-releases-executable-the-game-almost-boots/ | ✅ Contexto y estado |
| TweakTown — arranca en 3 horas | https://www.tweaktown.com/news/114839/gta-6-boots-on-pc-only-3-hours-after-xbox-executable-leaked/index.html | ✅ El titular que viralizó todo |
| VGTimes — menús, no gameplay | https://vgtimes.com/gaming-news/175531-unverified-gta-6-pc-videos-show-menus-not-gameplay.html | ✅ Distingue menús de juego |
| Notebookcheck — release del .exe | https://www.notebookcheck.net/Cyberleek-releases-GTA-6-Xbox-build-exe-boosting-playable-PC-port-chances.1457977.0.html | ✅ Cronología |
| LevelUp — versión 1.0.2.1 | https://www.levelup.com/en/news/cyberleek-leaks-gta-6s-executable-file-and-modders-are-already-working-on-a-playable-pc-version/ | ✅ Build concreta |
| TwistedVoxel — el dev de Leonida abandona | https://twistedvoxel.com/gta-6-pc-recompilation-leonida-developer-quits/ | ✅ Clave para entender la sostenibilidad |
| MakeUseOf — "port no oficial en camino" | https://www.makeuseof.com/gta-6-unofficial-pc-port-on-its-way/ | ⚠️ Bloquea bots |
| XDA — el "port" viral era un hoax con footage de GTA V | https://www.xda-developers.com/that-viral-gta-6-pc-port-video-hoax-made-from-recycled-gta-5-footage/ | ⚠️ Clave para no creer clips |
| XDA — NotRexed / Hookshot | https://www.xda-developers.com/?s=GTA+6 | ⚠️ Enlace exacto no verificable; búsqueda en el sitio |
| Notebookcheck — PS5 Pro + DLSS 5 | https://www.notebookcheck.net/GTA-6-PS5-Pro-performance-jumps-to-280-fps-on-PC-with-DLSS-5-transforming-Lucia.1453555.0.html | ✅ Ejemplo de cifras marketing |
| Basic Tutorials — VirusTotal 34/68 | https://basic-tutorials.com/news/gta-6-pc-cyberleek-releases-xbox-exe-leonida-port-remains-unreleased/ | ✅ Seguridad |

### 2.2. Repositorios citados en el vídeo

| Proyecto | Enlace | Qué es |
|---|---|---|
| VIctory | https://github.com/marvisak/VIctory | Runtime GTA VI específico |
| XCL | https://github.com/ivall/xcl | Capa de compatibilidad Xbox Series → Windows |
| Xbox2Windows | https://github.com/R0Y00/Xbox2Windows | Recompilación estática x64 → C++ |
| GTA6-BootTest | https://github.com/OnlyMoisties/GTA6-BootTest | DLLs stand-in + harness |
| Leonida (continuación) | https://github.com/ubiquitarianism/leonida | Interfaz Xbox → PC, GPL-3.0 |
| Tracker de la "carrera" | https://vuyp.github.io/gta6-pc-race/ | Agregador de claims auto-reportados |

### 2.3. Legal

| Fuente | Enlace | Qué aporta |
|---|---|---|
| DMCA de Take-Two, 18-11-2026 | https://github.com/github/dmca/blob/master/2026/11/2026-11-18-take-two.md | ✅ **Es sobre Muguet (GTA V), no GTA VI**; contiene la doctrina "bring your own files no te protege" |
| DMCA de Take-Two a re3/reVC, 2021 | https://github.com/github/dmca/blob/master/2021/02/2021-02-19-take-two.md | ✅ Precedente directo |
| TorrentFreak — Take-Two demanda a re3/reVC | https://torrentfreak.com/take-two-sues-enthusiasts-behind-gta-fan-projects-re3-revc-210903/ | ✅ |
| Dexerto — advertencia de Zelnick | https://www.dexerto.com/gta/gta-6-boss-sends-warning-to-pirates-who-make-ai-generated-pc-version-before-official-release-3426850 | ✅ |
| RTÉ — condena al "GTA hacker" | https://www.rte.ie/news/2026/1123/1600335-gta-hacker/ | ✅ Caso penal reciente |

### 2.4. Seguridad y estafas

| Fuente | Enlace | Qué aporta |
|---|---|---|
| Cyber Security News — 355+ dominios falsos | https://cybersecuritynews.com/fake-gta-6-pc-launchers/ | ✅ |
| Netcraft — campaña alrededor del lanzamiento | https://www.netcraft.com/blog/how-attackers-are-capitalizing-on-the-hype-around-the-grand-theft-auto-vi-release | ✅ |
| MakeTechEasier — kit de estafa de 200 $ | https://maketecheasier.com/gta-6-pc-port-scam-kit/ | ✅ |

### 2.5. Referencias técnicas que cita el vídeo

| Proyecto | Enlace | Por qué importa |
|---|---|---|
| Xenia (Xbox 360) | https://github.com/xenia-project/xenia | Emulador real de la generación anterior |
| Zelda64Recomp | https://github.com/Zelda64Recomp/Zelda64Recomp | Ejemplo de recompilación estática |
| UnleashedRecomp | https://github.com/hedge-dev/UnleashedRecomp | Otro ejemplo de port por recompilación |

---

## 3. Estado real del ecosistema (24-11-2026)

### 3.1. Qué hay en GitHub, en números

Consultas hechas con la API de GitHub el 24-11-2026 (los números cambian cada hora):

| Búsqueda | Resultados |
|---|---:|
| `gta 6` (nombre, descripción, README) | 20.404 |
| `gta6` | 17.591 |
| `leonida` | 2.789 |
| `"grand theft auto vi"` | 486 |
| `topic:gta6` | 1.114 |
| `topic:xbox-series-x` | 61 |
| `topic:reverse-engineer-anything` | 19 |

**Traducción:** no hay 3.000 proyectos de port. Hay decenas de miles de coincidencias, y la inmensa mayoría son:

- herramientas de clipping para streamers ("convierte streams de GTA 6 en Shorts"),
- HUDs y mods para GTA V,
- repos de SEO/afiliación con IA, creados en masa,
- **falsos emuladores y "preloads"** que son malware o simplemente un ZIP vacío,
- forks duplicados de los mismos 4-5 proyectos reales.

De los 25 repos más populares que revisé, **menos de 10 tienen código técnico real**. El resto es ruido. Los números de estrellas tampoco son fiables: hay proyectos con 9.000 estrellas creados en 24 horas.

### 3.2. Las 5 etapas, y quién está en cada una

| Etapa | Qué significa | Estado real |
|---|---|---|
| 1. Arranca | El .exe se carga y ejecuta código | Varios lo consiguen |
| 2. Imagen | Se crea el dispositivo D3D12 y hay un frame | Algunos, con shaders traducidos |
| 3. Menús | UI navegable | XCL, VIctory, Leonida y forks |
| 4. Mundo | Carga de mundo y escena visible | **Solo parcial y oscuro**; 0,3–1,8 s por frame |
| 5. Jugable | Se puede jugar | **Nadie** |

Los propios autores lo dicen en sus README: "el juego no arranca", "no hay frame completo", "self-reported, una sola máquina". Trátalo como prototipos de laboratorio, no como producto.

### 3.3. Los proyectos que importan

> **Nota:** las estrellas son de la fecha de corte. "Estado" es lo que el proyecto **afirma**, no algo que yo haya reproducido. Varios repos han desaparecido en las últimas 48 horas.

| Proyecto | Qué es | Estado declarado | Stars | Nota |
|---|---|---|---:|---|
| **XCL** (`ivall/xcl`) | Capa de compatibilidad estilo Wine: ejecuta código x64 nativo y reimplementa `kernelx`, `d3d12_xs`, DirectStorage y XAudio2; traduce shaders RDNA2 a DXIL | Arranca en ~4 s, menús y ajustes, ~30 fps sin crash; **no llega a gameplay**; ~15 GB de RAM. También corre *Minecraft Preview* y *Unicorn Overlord* | 6.8k | El más creíble técnicamente. GPL-2.0 |
| **VIctory** (`marvisak/VIctory`) | Runtime específico de GTA VI: carga el x86-64 nativo, reimplementa APIs y recompila shaders a DXIL | Boot, intro con sonido, pantalla de inicio a 30 fps; carga el mundo pero la escena está oscura a 0,5–1,8 s/frame; puede colgar el driver | 9.1k | El "más lejos" en lo público, pero **no jugable** |
| **Leonida** (`ubiquitarianism/leonida`) | Continuación del mayor proyecto de recompilación estática; GPL-3.0 | Su README sigue diciendo que el juego no arranca; 675 issues abiertos | 1.3k | El original `ItsNotRexed/Leonida` cerró el 23-11 |
| `ProjectLeonidaL/leonida` | Continuación "oficial" del Proyecto Leonida | Recompilación estática, sin frame completo | 256 | Creado el 24-11 |
| `LeonidaReforge/Leonida` | Otra continuación | Idem | 379 | Fork con 354 MB de historia |
| `avivetech/Leonida` | Copia tras la caída de `ItsNotRexed` | Idem | 134 | "main = last upstream main" |
| `luizwidmer/palmetto` | Runtime "clean-room" | Su autor dice que llega más lejos en el render; sin frame | 118 | Continuación de Leonida |
| `IAmNotSiob/leonida-ce` | Community edition | Idem | 19 | Duplicado |
| `Cappi1998/LONDBackup` | Copia de seguridad del árbol | Idem | 20 | Duplicado |
| **Xbox2Windows** (`R0Y00/Xbox2Windows`) | Recompilación estática: x64 → C++ y gfx1013 → DXIL | Con una build **modificada** que salta asserts, reprodujo la intro y llegó a carga; el .exe sin modificar, los menús y el gameplay **no están verificados** | 1.8k | Investigación, no producto |
| **AnyXboxX** (`LooperSalty/AnyXboxX`) | HLE del GDK sobre Unicorn + runtime C++ | Créditos iniciales con escena negra a 0,3–0,5 fps | 147 | Prototipo |
| **OpenScarlett** (`californiaAlmonds/OpenScarlett`) | Capa de traducción Scarlett: loader PE32+, `d3d12_xs`, `kernelx`, RDNA2 → SPIR-V/DXIL | Corre 6 samples de Microsoft; *Minecraft Preview* jugable; GTA VI solo resuelve imports y crea render targets | 80 | No es específico de GTA |
| **XValkyrie** (`sammwyy/xvalkyrie`) | Capa de compatibilidad Xbox One + Series | 49 títulos en su tabla: 8 jugables, 12 llegan a menú; GTA VI no | 214 | La más "Wine-like" |
| **GTA6-BootTest** (`OnlyMoisties/GTA6-BootTest`) | DLLs stand-in, harness de debug y traductor de shaders | Arranca, stream de archivos, frame loop y primera UI; compute/texturas tiled/blending incompletos | 40 | "No game code" |
| **awesome-gta6-reverse-engineering** | Lista curada de herramientas de RE de GTA VI | Actualizada a 24-11 | 656 | **La mejor puerta de entrada** |

### 3.4. La saga Leonida: la lección más importante

- El proyecto **Leonida** nació el 20-21 de noviembre, acumuló miles de PRs y llegó a traducir **26.503 shaders RDNA2 a SPIR-V**, exportar modelos, texturas y audio.
- El autor **anunció que se marchaba el 23-11** y el repositorio y su Discord desaparecieron esa misma noche.
- En menos de 24 horas aparecieron **seis continuaciones** (`ubiquitarianism`, `ProjectLeonidaL`, `LeonidaReforge`, `avivetech`, `palmetto`, `leonida-ce`), varias con el árbol completo de 350 MB.
- **Ninguna ha publicado un frame completo.**

Eso no es un problema técnico: es un problema de **sostenibilidad, ego y riesgo legal**. Un proyecto que depende de un binario filtrado y de una sola persona no es un proyecto; es un incidente.

### 3.5. Cómo distinguir un repo real de una estafa

Checklist rápida:

- **Fecha de creación**: si el repo nació esta semana y promete "100 % working", desconfía.
- **Código vs. README**: abre `src/`, mira commits reales. Un README de 500 líneas con un ZIP no es un proyecto.
- **Estrellas**: 9.000 estrellas en 24 horas = hype o compra, no calidad.
- **Issues**: un proyecto real tiene bugs reproducibles, logs y discusión técnica. Uno falso tiene "not working" y nada más.
- **Releases**: binarios con hash, build reproducible, CI. Un `.exe` de 146 MB sin firma es una ruleta rusa.
- **Claims**: "GTA 6 PC 2026", "preload incluido", "no BIOS", "DLSS 5", "120 fps" → palabras clave de estafa.
- **Archivos del juego**: si el repo incluye el .exe, claves o assets, es infracción directa. Si dice "bring your own copy", sigue siendo riesgo legal (ver sección 5).
- **VirusTotal**: el propio vídeo cita un caso con **34/68 detecciones**.

---

## 4. Por qué "la CPU es la misma" no basta

### 4.1. Las specs sí se parecen

| | Xbox Series X | PC típico equivalente |
|---|---|---|
| CPU | AMD Zen 2, 8C/16T, 3,8 GHz (3,66 con SMT) | Ryzen 7 3700X / 5800X |
| GPU | RDNA 2, 52 CUs, 1,825 GHz, 12,15 TFLOPS | RX 6700 XT / RTX 4060 Ti |
| RAM | 16 GB GDDR6 (10 GB a 560 GB/s + 6 GB a 336 GB/s) | 16-32 GB DDR4/DDR5 |
| SO | Xbox OS derivado de Windows + hipervisor | Windows 11 |
| API gráfica | `d3d12_xs` (D3D12 de consola) + extensiones | D3D12 / Vulkan |
| Shaders | RDNA2 `gfx1013`, compilados para la consola | DXIL / SPIR-V |
| Paquete | MSIXVC firmado y cifrado | .exe / Steam / Epic |

### 4.2. Lo que falta de verdad

1. **El SO y el hipervisor.** Un juego de Xbox no corre "sobre Windows": corre sobre una partición de Xbox OS, con un hipervisor que gestiona memoria, GPU y seguridad. En PC no existe.
2. **Las APIs.** El binario importa `kernelx`, `d3d12_xs`, `xgameruntime`, `xmem`, DirectStorage, XAudio2/XMA2. Windows no tiene esas DLLs. Hay que reimplementarlas (eso es XCL/XValkyrie) o traducir el binario (recompilación).
3. **El formato del paquete.** MSIXVC está firmado y cifrado. No basta con copiar el .exe: hay que montar el paquete, y eso implica claves y protección.
4. **Los shaders.** No son DXIL de PC: son ISA de RDNA2 con extensiones de consola. Hay que traducir decenas de miles de programas (`shaders.rpf`). XCL dice haber traducido 26.698; Leonida, 26.503. Es un trabajo enorme y parcial.
5. **La memoria.** 16 GB unificados con dos pools de distinta velocidad y aliasing (`xmem`). Un PC con GPU dedicada tiene un modelo distinto; los bugs de memoria son la causa típica de los cuelgues.
6. **El I/O.** DirectStorage de consola, compresión BCPack, texturas tiled, Bink 2, AWC/ADAT. Todo eso hay que decodificarlo.

### 4.3. Por qué no hay un "emulador de Series X"

- **Xenia** emula Xbox 360 (PowerPC, 2005). **Xemu** emula la Xbox original (2001). **Ninguno** ejecuta juegos de Series X.
- **RPCS3** (PS3) y **shadPS4** (PS4) existen porque hay años de investigación, documentación y una comunidad enorme. De Series X no hay boot chain público, ni documentación del hipervisor, ni claves.
- Los proyectos que sí existen son **HLE** (reimplementar APIs) o **recompilación estática** (traducir código), no emulación completa. Es la diferencia entre "Wine" y "un emulador de PlayStation 3".
- **XEVOD, APKOD, "Xbox Series X Emulator for PC"**: no son emuladores. Son páginas de descarga con un ZIP, marketing y, en el mejor caso, un tema visual. El propio artículo que los lista reconoce que "no hay emulador oficial".

### 4.4. Lo que sí demuestra el estado actual

- Que un equipo pequeño **puede** llevar un binario de consola a mostrar menús en Windows en días. Eso es un logro real.
- Que "mostrar menús" y "jugar" están separados por un abismo: mundo, streaming, GPU, memoria, audio, input, físicas, misiones.
- Que el cuello de botella no es la CPU: es **la GPU, la memoria y el sistema**.

---

## 5. La parte legal (lo que nadie te cuenta en los vídeos)

### 5.1. Descargar y usar la build filtrada es infracción

- El juego es obra protegida. **Descargarlo, compartirlo o ejecutarlo sin licencia** es reproducción/comunicación pública no autorizada.
- En España, el artículo 270 del Código Penal castiga la reproducción, distribución o comunicación pública de obras protegidas sin autorización, con penas que pueden llegar a **4 años de prisión** en supuestos agravados (ánimo de lucro, daño relevante).
- La "copia privada" **no** cubre descargar de Internet una filtración, y **no** cubre eludir protecciones.

### 5.2. Eludir la protección es un delito adicional

- La build de consola está cifrada y firmada. Para ejecutarla hay que **sortear medidas tecnológicas de protección** (TPM/DRM).
- EE. UU.: **DMCA §1201** (anti-circumvention), además del §106 (copyright).
- UE: Directiva 2001/29/CE, art. 6; en España, la Ley de Propiedad Intelectual y el Código Penal.
- El EULA de Rockstar prohíbe expresamente **reverse engineering, decompilación y elusión**.

### 5.3. "No incluyo archivos del juego" no te salva

Esta es la parte más importante y la que el vídeo enseña con un caso real:

- La DMCA de Take-Two del **18-11-2026** no va contra GTA VI: va contra **Muguet**, un port de **GTA V** a iOS/macOS.
- Take-Two pidió tumbar el repo **y sus 263 forks**.
- Su argumento textual: *"Claiming that this repository does not directly provide game files and requires users to own the game files does not excuse blatant facilitation of an unauthorized reproduction"*.
- Es decir: **"bring your own files" no es un escudo**. Si el proyecto existe para ejecutar una copia no autorizada, te pueden tumbar igual.

### 5.4. Precedentes

- **re3/reVC (2021):** Take-Two demandó a los autores del port de GTA III/Vice City, aunque el código era "clean room" y no incluía assets. El proyecto se retiró.
- **Muguet (2026):** DMCA masiva, 263 forks.
- **Caso penal del "GTA hacker" (2026):** condena reciente, citada por RTÉ el 23-11-2026.
- **GitHub:** además de la retirada, tu cuenta puede ser suspendida. Si contribuyes a un repo infractor, tu nombre queda en el historial.

### 5.5. Lo que es legal (o mucho menos gris)

- **Reimplementar una API** (como Wine) es legal en sí.
- **Escribir herramientas de análisis de formatos** (RPF9, TTPF, BCPack) es legal en sí, siempre que no distribuyas claves ni contenido del juego.
- **Analizar tus propios binarios** (programas que has compilado, software libre, CTFs) es legal.
- **Volcar tu propio juego de consola** es una zona gris y, en la práctica, requiere eludir protecciones; en España no es una defensa clara. No lo recomiendo.
- **Jugar en una consola que posees** y hacer Remote Play a tu portátil es 100 % legal.

---

## 6. Ingeniería inversa: el topic que enviaste

### 6.1. Qué hay realmente en `github.com/topics/reverse-engineer-anything`

El topic tiene **19 repos**. La mayoría son **paquetes de skills para agentes de IA** ("REA" = *Reverse Engineer Anything*), listas de casos y prompts para Claude Code/Codex/Cursor. No es la comunidad clásica de RE, y no sustituye a Ghidra.

| Repo | Stars | Qué es |
|---|---:|---|
| `AIshihzong/awesome-reverse-engineer-anything` | 895 | Lista curada de casos de RE asistido por IA |
| `smartworldarafath/REA_Skill` | 43 | 21 skills + 500 prompts para agentes |
| `git-sanbu/awesome-rea` | 32 | Casos de estudio con fuentes |
| `jammyfu/reverse-engineering-atlas` | 19 | Mapa de decompilaciones y reimplementaciones existentes |
| `tonchovet/REA-Windows-Github` | 12 | Puente REA ↔ Hopper/Ghidra |
| `DrBellubins/DecompileAnything` | 6 | Decompilación x86 a fuente "byte-matching" (experimental) |
| `hieunguyenak92/rea-pro-max` | 3 | MCP/skill/CLI de RE |

**Mi lectura:** úsalos para **triaje y automatización**, nunca como sustituto de entender el binario. Un agente que "te explica" un decompilado sin que tú sepas x86-64 es una alucinación con barra de progreso.

### 6.2. El stack de RE que sí importa (todo gratis o con versión free)

| Herramienta | Enlace | Uso |
|---|---|---|
| **Ghidra** | https://github.com/NationalSecurityAgency/ghidra | Decompilador y framework; el estándar libre |
| **radare2** | https://github.com/radareorg/radare2 | CLI de análisis |
| **Rizin** | https://github.com/rizinorg/rizin | Fork moderno de radare2 |
| **Cutter** | https://github.com/rizinorg/cutter | GUI sobre Rizin |
| **x64dbg** | https://github.com/x64dbg/x64dbg | Debugger de usuario en Windows |
| **Frida** | https://github.com/frida/frida | Instrumentación dinámica y hooking |
| **Unicorn** | https://github.com/unicorn-engine/unicorn | Emulación de CPU por instrucciones |
| **Qiling** | https://github.com/qilingframework/qiling | Emulación de binarios + OS |
| **angr** | https://github.com/angr/angr | Análisis simbólico |
| **RetDec** | https://github.com/avast/retdec | Decompilador retargetable |
| **ImHex** | https://github.com/WerWolv/ImHex | Editor hexadecimal con patterns |
| **PE-bear** | https://github.com/hasherezade/pe-bear | Inspección de PE |
| **Detect It Easy** | https://github.com/horsicq/Detect-It-Easy | Identificación de binarios/packers |
| **capa** | https://github.com/mandiant/capa | Identificación de capacidades |
| **FLARE VM** | https://github.com/mandiant/flare-vm | VM de análisis en Windows |
| **LIEF** | https://github.com/lief-project/LIEF | Parseo/modificación de executables |
| **Binary Ninja API** | https://github.com/Vector35/binaryninja-api | Alternativa comercial con API pública |
| **crackmes.one** | https://crackmes.one | Retos legales para practicar |

### 6.3. Objetivos legales para practicar (y aprender de verdad)

| Proyecto | Enlace | Qué aprendes |
|---|---|---|
| **OpenRW** | https://github.com/rwengine/openrw | Reimplementación de un motor de mundo abierto (GTA III), sin assets |
| **N64Recomp** | https://github.com/N64Recomp/N64Recomp | Recompilación estática |
| **Zelda64Recomp** | https://github.com/Zelda64Recomp/Zelda64Recomp | Recompilación + port |
| **UnleashedRecomp** | https://github.com/hedge-dev/UnleashedRecomp | Port por recompilación estática |
| **Xenia** | https://github.com/xenia-project/xenia | Emulación de Xbox 360 |
| **Xemu** | https://github.com/xemu-project/xemu | Emulación de Xbox original |
| **RPCS3** | https://github.com/RPCS3/rpcs3 | Emulación de PS3 |
| **shadPS4** | https://github.com/shadps4-emu/shadPS4 | Emulación de PS4 |
| **Kyty** | https://github.com/InoriRus/Kyty | PS4/PS5, HLE |
| **XCL / XValkyrie** | https://github.com/ivall/xcl · https://github.com/sammwyy/xvalkyrie | Capas de compatibilidad de consola |

**Regla de oro:** practica con binarios que puedas analizar legalmente. Un CTF, un juego open source, tu propio código. No empieces por el binario más protegido del año.

### 6.4. Currículo de 12 semanas (6-8 h/semana, 0 €)

| Semanas | Objetivo | Entregable |
|---|---|---|
| 1-2 | x86-64, PE/COFF, calling conventions, memoria, C/C++ | Un `hello world` compilado y diseccionado a mano |
| 3-4 | Ghidra: decompilador, scripts, headless | Script que liste funciones y strings de un binario |
| 5-6 | Formato de archivo: parsea ZIP/PNG y luego un formato propio | Parser en Python/Rust con tests |
| 7-8 | Unicorn/Qiling: emula una función, hookea APIs | Test que ejecute una función sin el binario completo |
| 9-10 | Shaders: DXIL/SPIR-V, LLVM AMDGPU, RenderDoc | Traducir un shader pequeño y validarlo |
| 11-12 | Contribuir a un proyecto open source | PR con test + CI en verde |

**Dónde contribuir sin hardware:** issues de documentación, tests unitarios, parsers de formato, herramientas de CLI, CI. Los proyectos tipo XCL tienen cientos de issues; muchos no requieren GPU.

---

## 7. Cómo llevarlo a cabo con 0 € y sin PC

Tu pregunta esconde **tres proyectos distintos**. Los separo porque tienen respuestas muy diferentes.

### Ruta A — Quiero **jugar** GTA VI sin PC

| Opción | Coste orientativo | Requisitos | Calidad | Veredicto |
|---|---|---|---|---|
| Esperar al port de PC | 0 € ahora; ~80 € el juego; PC de 800-1.500 € después | PC | La mejor | Lo más sensato si no hay prisa |
| **Xbox One usada + juego + cloud** | 80-150 € consola + 80 € juego + horas/Game Pass (15-20 €/mes) | 20+ Mbps, cuenta Xbox, mando | 1080p, ajustes de Series S, colas | **La vía más barata para jugar ya** |
| **Series S usada + juego** | 180-250 € + 80 € = **260-330 €** | TV/monitor, HDMI | 1080p/30 aprox. | **Mejor relación calidad/precio** |
| Series X usada + juego | 320-400 € + 80 € = **400-480 €** | TV 4K | 4K/30 aprox. | Si quieres la mejor consola |
| PS5 + juego | 400-500 € + 80 € | TV | Similar | Misma idea, otra plataforma |
| Consola de un amigo/familiar + **Remote Play** | 0 € si te la dejan | Su consola encendida + tu portátil/móvil | La de su consola | Legal y gratis, pero depende de otro |
| Alquiler / centro de gaming | 10-25 €/sesión | — | Alta | Para probarlo un fin de semana |
| GeForce NOW / Shadow PC | 20-40 €/mes | — | — | **No sirve: no hay versión PC** |
| "GTA 6 PC" de GitHub/Discord/Telegram | 0 € | — | — | **Estafa/malware + delito** |

**Datos clave:**

- Xbox Cloud Gaming para GTA VI está habilitado **solo en consolas Xbox** (Xbox One y Series X|S), a ajustes de Series S. **No** está disponible en PC, móvil, TV ni navegador, al menos al lanzamiento. Lo confirmó Xbox el 10-11-2026 y lo repitieron Matthew Ball y la propia Xbox Wire.
- **Remote Play** sí funciona desde una consola que tenga el juego hacia PC, Mac, móvil o Steam Deck. Es la única forma legal de ver GTA VI en la pantalla de un ordenador hoy.
- El juego cuesta **79,99 €** (estándar) y **99,99 €** (Ultimate) en España. La edición física es un código, no un disco.
- Una **Series S** usada está en **180-250 €**; una **Series X**, en **320-400 €**; una **Xbox One**, bastante menos.

**Mi recomendación concreta:** si el objetivo es jugar ya y gastar lo mínimo, **Xbox One usada + GTA VI + una suscripción de cloud por horas**. Si puedes estirar, **Series S usada**: no dependes de la nube, y puedes hacer Remote Play a tu portátil.

### Ruta B — Quiero **aprender ingeniería inversa** de verdad (0 €)

1. Haz el currículo de 12 semanas de la sección 6.4.
2. Elige un proyecto legal: OpenRW, N64Recomp, Xenia, shadPS4.
3. Empieza por issues de documentación/tests, no por el core.
4. Configura **GitHub Codespaces** (60 h/mes gratis en el plan free, 2 núcleos/8 GB) para trabajar desde cualquier sitio.
5. Usa **Oracle Cloud Always Free** (4 núcleos ARM Ampere, 24 GB RAM) para Ghidra headless: Ghidra es Java y funciona en ARM64. Es la mejor VM gratis para análisis estático.
6. Publica tus write-ups. Eso vale más que 9.000 estrellas en un repo de 24 horas.

**Lo que NO puedes verificar sin PC:** que el juego renderice, que vaya a 30 fps, que no cuelgue el driver. Eso requiere Windows + GPU + el juego. No hay atajo legal.

### Ruta C — "Aun así quiero intentar el port" (no recomendado)

Si insistes, esto es lo que realmente costaría:

| Recurso | Mínimo realista | Coste |
|---|---|---|
| Equipo | 3-10 personas con experiencia en x86-64, GPU, D3D12/Vulkan, shaders | 0 € si son voluntarios; años de tiempo |
| Hardware | Windows 11, 8-16 núcleos, 32-64 GB RAM, GPU 16 GB VRAM, 2 TB NVMe | 1.500-2.500 € |
| GPU cloud (si no hay PC) | RTX 3090/4090 por horas | 0,30-0,80 €/h; 4 h/día × 12 meses ≈ 600-1.500 € |
| Legal | Abogado, DMCA, posible demanda | Miles de euros |
| Tiempo | 1-3 años para algo "jugable", con suerte | — |

Y todo eso **sin** contar con el binario legal, que no existe: la única copia disponible es la filtrada.

**Conclusión:** no es un proyecto de 0 € ni de una persona. Es un proyecto de equipo, con hardware, con abogado y con años. Lo que sí puedes hacer es **contribuir a la parte legal del ecosistema** (herramientas de formato, tests, documentación) y aprender.

---

## 8. Mitos frecuentes

| Mito | Realidad |
|---|---|
| "La CPU es la misma, así que es fácil" | La ISA es el 5 %. Falta SO, hipervisor, GDK, GPU, memoria y DRM |
| "Es x86, debería correr como en Wine" | Wine reimplementa Win32. Xbox usa `kernelx`, `d3d12_xs` y paquetes cifrados |
| "Ya hay emulador de Series X" | No. Hay capas HLE y prototipos; XEVOD/APKOD son páginas de descarga, no emuladores |
| "Si el repo no incluye archivos del juego, es legal" | Take-Two ya ha tumbado 263 forks con ese argumento |
| "Los vídeos de gameplay lo prueban" | 41 clips revisados; muchos son GTA V reciclado o menús. Menús ≠ juego |
| "3.000 repos = comunidad enorme" | 20.000 coincidencias, pero <10 proyectos técnicos reales |
| "Con 0 € y un portátil se puede" | Puedes aprender y compilar; no puedes ejecutar ni verificar el juego |
| "La nube de Xbox sirve en PC" | Para GTA VI, no: solo consolas Xbox al lanzamiento |

---

## 9. Anexo: enlaces completos

### 9.1. Vídeo y fuentes originales

- Vídeo: https://www.youtube.com/watch?v=P0o-Fh-VSxo
- Canal: https://www.youtube.com/@thecodebear
- XDA (exe): https://www.xda-developers.com/gta-6-xbox-executable-leaked-opening-door-for-pc-recompilation-projects-begin-testing/
- GamesRadar: https://www.gamesradar.com/games/grand-theft-auto/gta-6-pc-version-is-close-modders-say-after-cyberleek-releases-executable-the-game-almost-boots/
- TweakTown: https://www.tweaktown.com/news/114839/gta-6-boots-on-pc-only-3-hours-after-xbox-executable-leaked/index.html
- VGTimes: https://vgtimes.com/gaming-news/175531-unverified-gta-6-pc-videos-show-menus-not-gameplay.html
- Notebookcheck (exe): https://www.notebookcheck.net/Cyberleek-releases-GTA-6-Xbox-build-exe-boosting-playable-PC-port-chances.1457977.0.html
- LevelUp: https://www.levelup.com/en/news/cyberleek-leaks-gta-6s-executable-file-and-modders-are-already-working-on-a-playable-pc-version/
- TwistedVoxel: https://twistedvoxel.com/gta-6-pc-recompilation-leonida-developer-quits/
- MakeUseOf: https://www.makeuseof.com/gta-6-unofficial-pc-port-on-its-way/
- XDA (hoax): https://www.xda-developers.com/that-viral-gta-6-pc-port-video-hoax-made-from-recycled-gta-5-footage/
- Notebookcheck (DLSS 5): https://www.notebookcheck.net/GTA-6-PS5-Pro-performance-jumps-to-280-fps-on-PC-with-DLSS-5-transforming-Lucia.1453555.0.html
- Tracker: https://vuyp.github.io/gta6-pc-race/

### 9.2. Repos del ecosistema

- https://github.com/marvisak/VIctory
- https://github.com/ivall/xcl
- https://github.com/R0Y00/Xbox2Windows
- https://github.com/OnlyMoisties/GTA6-BootTest
- https://github.com/ubiquitarianism/leonida
- https://github.com/ProjectLeonidaL/leonida
- https://github.com/LeonidaReforge/Leonida
- https://github.com/avivetech/Leonida
- https://github.com/luizwidmer/palmetto
- https://github.com/IAmNotSiob/leonida-ce
- https://github.com/Cappi1998/LONDBackup
- https://github.com/LooperSalty/AnyXboxX
- https://github.com/californiaAlmonds/OpenScarlett
- https://github.com/sammwyy/xvalkyrie
- https://github.com/TrinitronClient/zenith-x
- https://github.com/fablinoo/palmwave
- https://github.com/ubiquitarianism/leonida
- https://github.com/Ahmet-Dedeler/awesome-gta6-reverse-engineering
- https://github.com/TrinitronClient/GTA6-Asset-Info
- https://github.com/breadbbbb/rpf9-explorer
- https://github.com/rpatty-dev/PercyStar
- https://github.com/holdmysocks/SixNG
- https://github.com/Ahmet-Dedeler/bcpack-rs

### 9.3. Búsquedas para reproducir el barrido

- https://github.com/search?q=gta+6&type=repositories&s=stars&o=desc
- https://github.com/search?q=gta6&type=repositories&s=stars&o=desc
- https://github.com/search?q=leonida&type=repositories&s=stars&o=desc
- https://github.com/topics/gta6
- https://github.com/topics/leonida
- https://github.com/topics/xbox-series-x
- https://github.com/topics/reverse-engineer-anything

### 9.4. Legal y seguridad

- https://github.com/github/dmca/blob/master/2026/11/2026-11-18-take-two.md
- https://github.com/github/dmca/blob/master/2021/02/2021-02-19-take-two.md
- https://torrentfreak.com/take-two-sues-enthusiasts-behind-gta-fan-projects-re3-revc-210903/
- https://www.dexerto.com/gta/gta-6-boss-sends-warning-to-pirates-who-make-ai-generated-pc-version-before-official-release-3426850
- https://www.rte.ie/news/2026/1123/1600335-gta-hacker/
- https://cybersecuritynews.com/fake-gta-6-pc-launchers/
- https://www.netcraft.com/blog/how-attackers-are-capitalizing-on-the-hype-around-the-grand-theft-auto-vi-release
- https://maketecheasier.com/gta-6-pc-port-scam-kit/
- https://basic-tutorials.com/news/gta-6-pc-cyberleek-releases-xbox-exe-leonida-port-remains-unreleased/

### 9.5. Jugar barato / oficial

- https://news.xbox.com/en-us/2026/11/10/grand-theft-auto-6-comes-to-xbox-cloud-gaming-november-19
- https://news.xbox.com/en-us/2026/11/23/grand-theft-auto-vi-xbox-cloud-and-remote-play
- https://www.xbox.com/es-es/games/grand-theft-auto-vi
- https://www.playstation.com/en-us/support/subscriptions/psportal-cloud-game-streaming
- https://www.xbox.com/play

### 9.6. Herramientas de RE y aprendizaje

- https://github.com/NationalSecurityAgency/ghidra
- https://github.com/radareorg/radare2
- https://github.com/rizinorg/rizin
- https://github.com/rizinorg/cutter
- https://github.com/x64dbg/x64dbg
- https://github.com/frida/frida
- https://github.com/unicorn-engine/unicorn
- https://github.com/qilingframework/qiling
- https://github.com/angr/angr
- https://github.com/avast/retdec
- https://github.com/WerWolv/ImHex
- https://github.com/hasherezade/pe-bear
- https://github.com/horsicq/Detect-It-Easy
- https://github.com/mandiant/capa
- https://github.com/mandiant/flare-vm
- https://github.com/lief-project/LIEF
- https://github.com/Vector35/binaryninja-api
- https://crackmes.one

### 9.7. Proyectos legales para estudiar/reutilizar

- https://github.com/rwengine/openrw
- https://github.com/N64Recomp/N64Recomp
- https://github.com/Zelda64Recomp/Zelda64Recomp
- https://github.com/hedge-dev/UnleashedRecomp
- https://github.com/xenia-project/xenia
- https://github.com/xemu-project/xemu
- https://github.com/RPCS3/rpcs3
- https://github.com/shadps4-emu/shadPS4
- https://github.com/InoriRus/Kyty

### 9.8. Topic `reverse-engineer-anything`

- https://github.com/topics/reverse-engineer-anything
- https://github.com/AIshihzong/awesome-reverse-engineer-anything
- https://github.com/smartworldarafath/REA_Skill
- https://github.com/git-sanbu/awesome-rea
- https://github.com/jammyfu/reverse-engineering-atlas
- https://github.com/tonchovet/REA-Windows-Github
- https://github.com/DrBellubins/DecompileAnything
- https://github.com/hieunguyenak92/rea-pro-max

---

## 10. Qué haría yo, en orden

1. **No descargar nada** de "GTA 6 PC". Ni el .exe, ni el "preload", ni el "emulador". El riesgo de malware y legal no compensa.
2. **Decidir el objetivo real**: ¿jugar, aprender o presumir de proyecto? Si es jugar, Ruta A. Si es aprender, Ruta B.
3. **Si es jugar**: buscar una Xbox One/Series S usada y el juego. Probar Remote Play en tu portátil. Presupuesto cerrado: 260-330 € con Series S.
4. **Si es aprender**: empezar el currículo de 12 semanas esta semana, con OpenRW o un CTF. Crear cuenta de GitHub y Codespaces.
5. **Si es investigar**: seguir el tracker y leer los README de XCL/VIctory, pero **no ejecutar** el binario filtrado. Guarda los enlaces y espera al port oficial.
6. **Si en 2027 sale el port de PC**: cómpralo. Habrá valido la pena esperar.

---

## 11. Nota final

La intuición técnica del principio —"la CPU es la misma"— no es una tontería: es la razón por la que estos proyectos existen y por la que XCL puede ejecutar código x64 nativo. Pero confundir "misma ISA" con "mismo sistema" es como decir que un motor diésel y uno de gasolina son iguales porque ambos tienen pistones.

Lo que ha pasado en noviembre de 2026 es fascinante: en cuatro días, una comunidad consiguió llevar un binario de consola a los menús en Windows. También es un buen ejemplo de por qué el hype es peligroso: 9.000 estrellas, 26.000 shaders traducidos, seis forks... y ni un frame jugable. La distancia entre "arranca" y "juego" es la distancia entre un prototipo y un producto.

Con 0 € y sin PC puedes aprender muchísimo. Lo que no puedes es saltarte la física, el derecho y 20 años de ingeniería de consolas.

---

*Documento generado el 24-11-2026. Los datos de repos, estrellas y estados cambian a diario; vuelve a verificar antes de tomar decisiones.*
