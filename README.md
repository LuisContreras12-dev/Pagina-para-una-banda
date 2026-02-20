# Pagina-para-una-banda - Foo Fighters

Página web para la banda **Foo Fighters** desarrollada con **Flask** y **Bootstrap-Flask**.

---

## Tecnologías Utilizadas

| Tecnología | Uso |
|---|---|
| **Python 3** | Lenguaje de programación |
| **Flask 3.0** | Framework web |
| **Bootstrap-Flask 2.3** | Integración de Bootstrap 5 con Flask |
| **Bootstrap 5** | Framework CSS para diseño responsivo |
| **Bootstrap Icons** | Iconografía |
| **JSON** | Almacenamiento de datos |

## Estructura del Proyecto

```
Pagina-para-una-banda/
├── app.py                      # Aplicación principal de Flask
├── requirements.txt            # Dependencias de Python
├── data/                       # Datos en formato JSON
│   ├── tour.json               # Fechas del tour
│   ├── discografia.json        # Álbumes y canciones
│   ├── media.json              # Fotos y videos
│   └── social.json             # Redes sociales
├── templates/                  # Plantillas HTML (Jinja2)
│   ├── base.html               # Plantilla base con navbar y footer
│   ├── inicio.html             # Página de inicio
│   ├── tour.html               # Fechas del tour
│   ├── discografia.html        # Discografía completa
│   ├── media.html              # Galería de fotos y videos
│   └── redes.html              # Redes sociales
└── static/                     # Archivos estáticos
    └── css/
        └── style.css           # Estilos personalizados
```

## Secciones de la Página

1. **Inicio** — Presentación de la banda, miembros y estadísticas.
2. **Tour** — Listado de fechas de presentaciones con disponibilidad de boletos.
3. **Discografía** — Álbumes de estudio con imágenes, descripción y canciones destacadas.
4. **Fotos / Videos** — Galería de imágenes y videos musicales embebidos de YouTube.
5. **Redes Sociales** — Enlaces a todas las plataformas sociales de la banda.

## Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/LuisContreras12-dev/Pagina-para-una-banda.git
cd Pagina-para-una-banda
```

### 2. Crear un entorno virtual (recomendado)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python app.py
```

### 5. Abrir en el navegador
```
http://127.0.0.1:5000
```

## Rutas Disponibles

| Ruta | Descripción |
|---|---|
| `/` | Página de inicio |
| `/tour` | Fechas del tour 2026 |
| `/discografia` | Discografía completa |
| `/media` | Fotos y videos |
| `/redes` | Redes sociales |

## Almacenamiento de Datos

Los datos se almacenan en archivos **JSON** dentro de la carpeta `data/`. Esto permite modificar el contenido de la página fácilmente sin necesidad de cambiar el código fuente de Python.

---

Desarrollado con Flask & Bootstrap-Flask
Elaborar una página usando el framework para python de Flask, Bootstrap-Flask, para la banda musical que sea de su agrado.   Pueden poner las siguientes opciones:  Tour (listado de fechas en que se presentarán) Discografía (Pueden poner imágenes con descripción) Fotos / Videos Redes sociales   Y usar json o SQL Alchemy. 
