# Atajos Neovim — LazyVim

`<Leader>` = **Espacio**

---

## Navegación básica

| Acción | Tecla |
|--------|-------|
| Moverse | `h` `j` `k` `l` |
| Palabra siguiente/anterior | `w` / `b` |
| Inicio/fin de línea | `0` / `$` |
| Inicio/fin de archivo | `gg` / `G` |
| Ir a línea específica | `:42` + Enter |

---

## Edición

| Acción | Tecla |
|--------|-------|
| Insertar modo | `i` |
| Insertar al inicio de línea | `I` |
| Insertar al final | `A` |
| Salir de insertar | `Esc` o `Ctrl+c` |
| Borrar carácter | `x` |
| Borrar línea | `dd` |
| Copiar línea | `yy` |
| Pegar abajo / arriba | `p` / `P` |
| Deshacer / Rehacer | `u` / `Ctrl+r` |
| Mover línea(s) abajo/arriba | `Alt+j` / `Alt+k` |
| Guardar | `Ctrl+s` |

---

## Selección (Visual)

| Acción | Tecla |
|--------|-------|
| Selección normal | `v` |
| Selección línea entera | `V` |
| Selección bloque/columna | `Ctrl+v` |
| Seleccionar todo | `gg V G` |

---

## Archivos

| Acción | Tecla |
|--------|-------|
| Explorador de archivos | `<Leader> e` |
| Buscar archivo | `<Leader><Leader>` (Espacio dos veces) |
| Buscar texto en proyecto | `<Leader> sg` |
| Archivos recientes | `<Leader> fr` |
| Abrir directorio padre | `-` (Oil.nvim) |
| Cerrar panel | `q` |

---

## Búsqueda y reemplazo

| Acción | Tecla |
|--------|-------|
| Buscar en archivo | `/texto` + Enter |
| Siguiente / anterior | `n` / `N` |
| Buscar y reemplazar | `:%s/viejo/nuevo/g` |
| Buscar texto en proyecto | `<Leader> sg` |

---

## LSP (errores, definiciones)

| Acción | Tecla |
|--------|-------|
| Ir a definición | `gd` |
| Ir a implementación | `gI` |
| Ver referencias | `gr` |
| Ver documentación | `K` |
| Renombrar variable | `<Leader> cr` |
| Lista de errores | `<Leader> xx` |
| Error en línea actual | `<Leader> ld` |
| Siguiente error | `]d` |
| Anterior error | `[d` |
| Vista previa definición | `gpd` |
| Cerrar previsualización | `gP` |

---

## Paneles y splits

| Acción | Tecla |
|--------|-------|
| Split horizontal | `<Leader> -` |
| Split vertical | `<Leader> \|` |
| Moverse entre splits | `Ctrl+w` + flecha |
| Cerrar split | `:q` |

---

## Tmux Navigation

| Acción | Tecla |
|--------|-------|
| Ir al panel izquierdo | `Ctrl+h` |
| Ir al panel abajo | `Ctrl+j` |
| Ir al panel arriba | `Ctrl+k` |
| Ir al panel derecho | `Ctrl+l` |
| Último panel activo | `Ctrl+\` |
| Siguiente panel | `Ctrl+Space` |

---

## Terminal (snacks.nvim)

| Acción | Tecla |
|--------|-------|
| Terminal flotante | `<Leader> ft` |
| Terminal directorio raíz | `<Leader> fT` |
| Toggle terminal | `<C-/>` |
| Salir al modo normal (sin cerrar) | `Ctrl+\ Ctrl+n` |
| Cerrar terminal | `:q!` |

---

## Copilot

| Acción | Tecla |
|--------|-------|
| Aceptar sugerencia | `Tab` |
| Siguiente sugerencia | `Alt+]` |
| Anterior sugerencia | `Alt+[` |
| Descartar sugerencia | `Ctrl+]` |

---

## Git

| Acción | Tecla |
|--------|-------|
| Status | `<Leader> gs` |
| Diff | `<Leader> gd` |
| Commit | `<Leader> gc` |
| Log | `<Leader> gl` |
| Blame | `<Leader> gb` |
| Abrir en GitHub | `<Leader> go` |

---

## Obsidian

| Acción | Tecla |
|--------|-------|
| Check checkbox | `<Leader> oc` |
| Insertar template | `<Leader> ot` |
| Abrir en app | `<Leader> oo` |
| Backlinks | `<Leader> ob` |
| Links | `<Leader> ol` |
| Nota nueva | `<Leader> on` |
| Buscar | `<Leader> os` |
| Quick switch | `<Leader> oq` |

---

## Archivos (Oil.nvim)

| Acción | Tecla |
|--------|-------|
| Abrir directorio padre | `-` |
| Crear archivo | `%` (en Oil) |
| Crear directorio | `d` (en Oil) |
| Renombrar | `R` (en Oil) |
| Borrar | `dd` (en Oil) |
| Copiar | `c` (en Oil) |
| Mover | `m` (en Oil) |

---

## Buffers

| Acción | Tecla |
|--------|-------|
| Siguiente buffer | `]b` |
| Buffer anterior | `[b` |
| Cerrar buffer | `<Leader> bd` |
| Nuevo buffer | `<Leader> bn` |
| Buscar buffers | `<Leader> fb` |
| Cerrar todos menos actual | `<Leader> bq` |

---

## Python (venv-selector.nvim)

| Acción | Tecla |
|--------|-------|
| Seleccionar venv | `,v` |
| Ver venv activo | `:VenvSelectCurrent` |

---

## Marcas

| Acción | Tecla |
|--------|-------|
| Crear marca | `m + a-z` |
| Ir a marca | `' + a-z` |
| Ir a marca (línea exacta) | `` ` + a-z `` |
| Ver marcas | `:marks` |

---

## Macros

| Acción | Tecla |
|--------|-------|
| Grabar macro | `q + a-z` |
| Ejecutar macro | `@ + a-z` |
| Repetir última macro | `@@` |
| Ejecutar macro N veces | `N @ + a-z` |

---

## Text Objects

| Acción | Tecla |
|--------|-------|
| Dentro de palabra | `iw` |
| Alrededor de palabra | `aw` |
| Dentro de paréntesis | `i(` |
| Alrededor de paréntesis | `a(` |
| Dentro de corchetes | `i[` |
| Dentro de comillas | `i"` |
| Dentro de bloque | `i{` |

---

## Formato

| Acción | Tecla |
|--------|-------|
| Formatear selección | `=` |
| Indentar línea | `>>` |
| Reducir indent | `<<` |
| Unir líneas | `J` |
| Comentar línea | `<Leader> cc` |
| Descomentar línea | `<Leader> cu` |

---

## Selección y búsqueda

| Acción | Tecla |
|--------|-------|
| Grep texto seleccionado (visual) | `<Leader> sg` |
| Grep en raíz del proyecto (visual) | `<Leader> sG` |
| Borrar todas las marcas | `<Leader> md` |

---

## Varios

| Acción | Tecla |
|--------|-------|
| Zen Mode (sin distracción) | `<Leader> z` |
| Buscar buffers abiertos | `<Leader> fb` |
| Cerrar todos los buffers menos actual | `<Leader> bq` |
| Abrir Cambios de Harpoon | `Ctrl+h/j/k/l` (tmux) |
| Atajos disponibles | Esperar 1s después de `<Leader>` |
| Screenkey (ver teclas) | `<Leader> uk` |
| Guardar archivo | `Ctrl+s` |
| Salir insertar rápido | `Ctrl+c` |

---

## Salir

| Acción | Tecla |
|--------|-------|
| Cerrar archivo | `:q` + Enter |
| Cerrar sin guardar | `:q!` + Enter |
| Guardar y cerrar | `:wq` + Enter |
| Cerrar todo | `:qa` + Enter |
