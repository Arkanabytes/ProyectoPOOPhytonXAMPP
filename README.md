<div align="center">

# 🎓 Sistema de Gestión Universitaria
### POO Python + XAMPP + MySQL

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&duration=2800&pause=2000&color=A855F7&center=true&vCenter=true&width=940&lines=Sistema+Integral+de+Gesti%C3%B3n+Universitaria;Desarrollado+con+Python+%F0%9F%90%8D;Arquitectura+POO+%E2%9C%A8;Base+de+Datos+MySQL+%F0%9F%92%BE" alt="Typing SVG" />

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![XAMPP](https://img.shields.io/badge/XAMPP-Server-FB7A24?style=for-the-badge&logo=xampp&logoColor=white)](https://www.apachefriends.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

</div>

---

## 🌟 Características Principales

<table>
<tr>
<td width="50%">

### 👥 Gestión de Usuarios
```python
class Usuario:
    """Clase base abstracta"""
    🔐 Sistema de autenticación
    👤 Perfiles personalizados
    📊 Información completa
```

### 🎓 Módulo Estudiantes
```python
✅ Gestión académica completa
💰 Billetera virtual
📚 Inscripción de asignaturas
💳 Pago de servicios
📈 Historial académico
```

</td>
<td width="50%">

### 🚗 Módulo Conductores
```python
🚘 Registro de vehículos
⭐ Sistema de calificación
💵 Cálculo automático de tarifas
🗺️ Historial de viajes
📍 Registro de rutas
```

### 🛒 Sistema de Pedidos
```python
🛍️ Carrito de compras
📦 Catálogo de productos
✔️ Estados de pedido
💰 Cálculo de totales
📜 Historial de compras
```

</td>
</tr>
</table>

---

<div align="center">

## 🏗️ Arquitectura del Sistema

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

</div>

### 🎯 Patrones de Diseño Implementados

```mermaid
graph LR
    A[🎨 Singleton] --> B[💾 Database Connection]
    C[🗂️ DAO Pattern] --> D[📊 Data Access Layer]
    E[🔄 Herencia] --> F[👥 Usuario Base]
    G[🧩 Composición] --> H[🔗 Relaciones]
    
    style A fill:#a855f7
    style C fill:#3b82f6
    style E fill:#10b981
    style G fill:#f59e0b
```

<div align="center">

### 📊 Diagrama de Clases UML

</div>

```mermaid
classDiagram
    class Usuario {
        <<abstract>>
        -int id_usuario
        -str nombre
        -str email
        -str telefono
        +__init__(id_usuario, nombre, email, telefono)
        +mostrar_info()
    }
    
    class Estudiante {
        -str carrera
        -int anio
        -float saldo_cuenta
        -list asignaturas
        +__init__(...)
        +mostrar_info()
        +pagar_servicio(monto)
        +agregar_saldo(monto)
        +inscribir_asignatura(asignatura)
    }
    
    class Conductor {
        -str patente
        -str tipo_vehiculo
        -float calificacion
        -list viajes
        +__init__(...)
        +mostrar_info()
        +calcular_tarifa(distancia, tiempo, pasajeros) float
        +registrar_viaje(origen, destino, distancia, tiempo, pasajeros)
    }
    
    class Producto {
        -str nombre
        -float precio
        -str categoria
        +__init__(nombre, precio, categoria)
        +__str__()
    }
    
    class Pedido {
        -int id_pedido
        -int id_estudiante
        -list productos
        -float precio_total
        -str estado
        +__init__(id_pedido, id_estudiante)
        +agregar_producto(producto, cantidad)
        +confirmar()
        +cambiar_estado(nuevo_estado)
        +mostrar_detalle()
    }
    
    class Asignatura {
        -int id_asignatura
        -str nombre
        -str profesor
        -int creditos
        +__init__(id_asignatura, nombre, profesor, creditos)
        +__str__()
    }
    
    class Horario {
        -int id_horario
        -str dia
        -time hora_inicio
        -time hora_fin
        -list asignaturas
        +__init__(id_horario, dia, hora_inicio, hora_fin)
        +agregar_asignatura(asignatura)
        +verificar_choque(otro_horario) bool
        +__str__()
    }
    
    class DatabaseConnection {
        <<Singleton>>
        -DatabaseConnection _instance
        -MySQLConnection connection
        +connect(host, user, password, database)
        +get_connection() MySQLConnection
        +close()
    }
    
    class EstudianteDAO {
        +insertar(estudiante)
        +obtener(id_estudiante) Estudiante
        +actualizar(estudiante)
        +eliminar(id_estudiante)
    }
    
    class PedidoDAO {
        +insertar(pedido)
        +obtener(id_pedido) Pedido
        +actualizar(pedido)
        +eliminar(id_pedido)
    }
    
    class AsignaturaDAO {
        +insertar(asignatura)
        +obtener(id_asignatura) Asignatura
        +actualizar(asignatura)
        +eliminar(id_asignatura)
        +inscribir_estudiante(id_estudiante, id_asignatura)
    }
    
    Usuario <|-- Estudiante
    Usuario <|-- Conductor
    Estudiante "1" o-- "*" Asignatura
    Estudiante "1" o-- "*" Pedido
    Pedido "1" o-- "*" Producto
    Horario "1" o-- "*" Asignatura
    DatabaseConnection <-- EstudianteDAO : usa
    DatabaseConnection <-- PedidoDAO : usa
    DatabaseConnection <-- AsignaturaDAO : usa
    EstudianteDAO ..> Estudiante : gestiona
    PedidoDAO ..> Pedido : gestiona
    AsignaturaDAO ..> Asignatura : gestiona
```

---

<div align="center">

## 🚀 Instalación y Configuración

<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100">

</div>

### 📋 Requisitos Previos

| Tecnología | Versión | Descripción |
|------------|---------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | 3.8+ | Lenguaje principal |
| ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white) | 8.0+ | Base de datos |
| ![XAMPP](https://img.shields.io/badge/XAMPP-FB7A24?style=flat&logo=xampp&logoColor=white) | Latest | Servidor local |

### 🔧 Paso 1: Clonar el Repositorio

```bash
# Clonar el proyecto
git clone https://github.com/Arkanabytes/ProyectoPOOPhytonXAMPP.git

# Navegar al directorio
cd ProyectoPOOPhytonXAMPP

# Cambiar a la rama Pseint
git checkout Pseint
```

### 🔧 Paso 2: Configurar XAMPP

```bash
# 1. Descargar XAMPP desde: https://www.apachefriends.org/
# 2. Instalar XAMPP
# 3. Abrir el Panel de Control de XAMPP
# 4. Iniciar Apache y MySQL
```

<div align="center">

![XAMPP](https://img.shields.io/badge/✅-Apache%20Running-success?style=for-the-badge)
![MySQL](https://img.shields.io/badge/✅-MySQL%20Running-success?style=for-the-badge)

</div>

### 🔧 Paso 3: Crear la Base de Datos

```sql
-- Acceder a phpMyAdmin: http://localhost/phpmyadmin

CREATE DATABASE sistema_universitario;
USE sistema_universitario;

-- Las tablas se crearán automáticamente 🎯
```

### 🔧 Paso 4: Instalar Dependencias Python

```bash
# Instalar mysql-connector-python
pip install mysql-connector-python

# O usar requirements.txt
pip install -r requirements.txt
```

### 🔧 Paso 5: Configurar Conexión

```python
# Editar archivo de configuración
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Vacío por defecto en XAMPP
    'database': 'sistema_universitario'
}
```

---

<div align="center">

## 📁 Estructura del Proyecto

</div>

```
📦 ProyectoPOOPhytonXAMPP/
┣ 📂 models/
┃ ┣ 📜 usuario.py          # 👤 Clase abstracta Usuario
┃ ┣ 📜 estudiante.py       # 🎓 Clase Estudiante
┃ ┣ 📜 conductor.py        # 🚗 Clase Conductor
┃ ┣ 📜 producto.py         # 📦 Clase Producto
┃ ┣ 📜 pedido.py          # 🛒 Clase Pedido
┃ ┣ 📜 asignatura.py      # 📚 Clase Asignatura
┃ ┗ 📜 horario.py         # ⏰ Clase Horario
┣ 📂 dao/
┃ ┣ 📜 database_connection.py  # 💾 Singleton de conexión
┃ ┣ 📜 estudiante_dao.py       # 🗄️ DAO Estudiante
┃ ┣ 📜 pedido_dao.py          # 🗄️ DAO Pedido
┃ ┗ 📜 asignatura_dao.py      # 🗄️ DAO Asignatura
┣ 📂 sql/
┃ ┗ 📜 schema.sql         # 🗃️ Script de creación
┣ 📜 main.py              # 🚀 Punto de entrada
┣ 📜 config.py            # ⚙️ Configuración
┣ 📜 requirements.txt     # 📦 Dependencias
┗ 📜 README.md           # 📖 Este archivo
```

---

<div align="center">

## 💻 Ejemplos de Uso

<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="100">

</div>

### 🎓 Crear un Estudiante

```python
from models.estudiante import Estudiante
from dao.estudiante_dao import EstudianteDAO

# ✨ Crear instancia de estudiante
estudiante = Estudiante(
    id_usuario=1,
    nombre="Juan Pérez",
    email="juan.perez@universidad.cl",
    telefono="+56912345678",
    carrera="Ingeniería Civil Informática",
    anio=3
)

# 💾 Guardar en la base de datos
dao = EstudianteDAO()
dao.insertar(estudiante)

# 💰 Agregar saldo a la cuenta
estudiante.agregar_saldo(50000)
print(f"💵 Saldo actual: ${estudiante.saldo_cuenta}")

# 📚 Inscribir asignatura
from models.asignatura import Asignatura
asignatura = Asignatura(1, "Programación Orientada a Objetos", "Dr. Smith", 8)
estudiante.inscribir_asignatura(asignatura)
print("✅ Asignatura inscrita exitosamente")
```

### 🛒 Crear un Pedido

```python
from models.pedido import Pedido
from models.producto import Producto

# 🆕 Crear nuevo pedido
pedido = Pedido(id_pedido=1, id_estudiante=1)

# 📦 Agregar productos al carrito
producto1 = Producto("Laptop", 500000, "Electrónica")
producto2 = Producto("Mouse", 15000, "Accesorios")
producto3 = Producto("Teclado", 35000, "Accesorios")

pedido.agregar_producto(producto1, 1)
pedido.agregar_producto(producto2, 2)
pedido.agregar_producto(producto3, 1)

# ✅ Confirmar pedido
pedido.confirmar()
print(f"🎉 Pedido confirmado - Total: ${pedido.precio_total}")

# 📊 Mostrar detalle
pedido.mostrar_detalle()
```

### 🚗 Calcular Tarifa de Conductor

```python
from models.conductor import Conductor

# 🚘 Crear conductor
conductor = Conductor(
    id_usuario=2,
    nombre="María González",
    email="maria.gonzalez@email.com",
    telefono="+56987654321",
    patente="ABCD12",
    tipo_vehiculo="Sedan"
)

# 💵 Calcular tarifa del viaje
tarifa = conductor.calcular_tarifa(
    distancia=10.5,  # 📏 kilómetros
    tiempo=25,       # ⏱️ minutos
    pasajeros=3      # 👥 número de pasajeros
)

print(f"💰 Tarifa calculada: ${tarifa:,.0f}")

# 📝 Registrar el viaje
conductor.registrar_viaje(
    origen="Campus Universidad",
    destino="Metro Baquedano",
    distancia=10.5,
    tiempo=25,
    pasajeros=3
)
print("✅ Viaje registrado exitosamente")
```

### 📚 Gestionar Horarios

```python
from models.horario import Horario
from models.asignatura import Asignatura
from datetime import time

# ⏰ Crear horario
horario = Horario(
    id_horario=1,
    dia="Lunes",
    hora_inicio=time(8, 30),
    hora_fin=time(10, 0)
)

# 📖 Agregar asignaturas
asignatura1 = Asignatura(1, "POO", "Dr. Smith", 8)
horario.agregar_asignatura(asignatura1)

# 🔍 Verificar choques de horario
horario2 = Horario(2, "Lunes", time(9, 0), time(10, 30))
if horario.verificar_choque(horario2):
    print("⚠️ Conflicto de horario detectado!")
else:
    print("✅ Sin conflictos de horario")
```

---

<div align="center">

## 🗄️ Base de Datos

<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="100">

</div>

### 📊 Diagrama Entidad-Relación

```mermaid
erDiagram
    USUARIOS ||--o{ ESTUDIANTES : es
    USUARIOS ||--o{ CONDUCTORES : es
    ESTUDIANTES ||--o{ PEDIDOS : realiza
    ESTUDIANTES }o--o{ ASIGNATURAS : inscribe
    PEDIDOS ||--o{ DETALLE_PEDIDOS : contiene
    PRODUCTOS ||--o{ DETALLE_PEDIDOS : incluido_en
    HORARIOS }o--o{ ASIGNATURAS : programadas_en
    
    USUARIOS {
        int id_usuario PK
        string nombre
        string email
        string telefono
        string tipo
    }
    
    ESTUDIANTES {
        int id_estudiante PK
        int id_usuario FK
        string carrera
        int anio
        float saldo_cuenta
    }
    
    CONDUCTORES {
        int id_conductor PK
        int id_usuario FK
        string patente
        string tipo_vehiculo
        float calificacion
    }
    
    PEDIDOS {
        int id_pedido PK
        int id_estudiante FK
        float precio_total
        string estado
        datetime fecha
    }
    
    PRODUCTOS {
        int id_producto PK
        string nombre
        float precio
        string categoria
    }
    
    ASIGNATURAS {
        int id_asignatura PK
        string nombre
        string profesor
        int creditos
    }
    
    HORARIOS {
        int id_horario PK
        string dia
        time hora_inicio
        time hora_fin
    }
```

### 📋 Tablas Principales

<table>
<tr>
<td>

#### 👥 USUARIOS
```sql
id_usuario (PK)
nombre
email
telefono
tipo
fecha_registro
```

#### 🎓 ESTUDIANTES
```sql
id_estudiante (PK)
id_usuario (FK)
carrera
anio
saldo_cuenta
```

</td>
<td>

#### 🚗 CONDUCTORES
```sql
id_conductor (PK)
id_usuario (FK)
patente
tipo_vehiculo
calificacion
```

#### 🛒 PEDIDOS
```sql
id_pedido (PK)
id_estudiante (FK)
precio_total
estado
fecha
```

</td>
</tr>
</table>

---

<div align="center">

## 🎯 Principios SOLID Aplicados

</div>

| Principio | Implementación | Ejemplo |
|-----------|---------------|---------|
| **S**ingle Responsibility | Cada clase tiene una única responsabilidad | `Usuario`, `Pedido`, `DatabaseConnection` |
| **O**pen/Closed | Clases abiertas para extensión, cerradas para modificación | Herencia de `Usuario` → `Estudiante`, `Conductor` |
| **L**iskov Substitution | Las subclases pueden sustituir a sus clases base | Cualquier `Usuario` puede ser `Estudiante` o `Conductor` |
| **I**nterface Segregation | Interfaces específicas para cada cliente | DAOs especializados por entidad |
| **D**ependency Inversion | Depender de abstracciones, no de concreciones | Uso de clase abstracta `Usuario` |

---

<div align="center">

## 🤝 Contribuir

<img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="100">

</div>

¡Las contribuciones son bienvenidas! Si quieres mejorar este proyecto:

1. 🍴 **Fork** el proyecto
2. 🌿 **Crea** una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. 💾 **Commit** tus cambios (`git commit -m 'Add: AmazingFeature'`)
4. 📤 **Push** a la rama (`git push origin feature/AmazingFeature`)
5. 🔃 **Abre** un Pull Request

### 📝 Guías de Estilo

- ✅ Seguir **PEP 8** para código Python
- 📖 Documentar todas las clases y métodos
- 🧪 Escribir tests para nuevas funcionalidades
- 🧩 Mantener el código modular y reutilizable
- 💬 Commits descriptivos y en español

---

<div align="center">

## 🏆 Características Destacadas

![Static Badge](https://img.shields.io/badge/POO-Orientado_a_Objetos-purple?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/Patrones-Singleton_+_DAO-blue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/SOLID-Principios_Aplicados-green?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/MySQL-Base_de_Datos-orange?style=for-the-badge)

</div>

---

<div align="center">

## 📞 Contacto y Soporte

<a href="https://github.com/Arkanabytes">
  <img src="https://img.shields.io/badge/GitHub-Arkanabytes-181717?style=for-the-badge&logo=github" />
</a>

### 💬 ¿Necesitas ayuda?

- 🐛 [Reportar un Bug](https://github.com/Arkanabytes/ProyectoPOOPhytonXAMPP/issues)
- 💡 [Solicitar una Feature](https://github.com/Arkanabytes/ProyectoPOOPhytonXAMPP/issues)
- 📧 Contacto directo vía GitHub

</div>

---

<div align="center">

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">

### 🙏 Agradecimientos

Gracias a todos los que han contribuido a este proyecto 💜

**Si este proyecto te ha sido útil, considera darle una ⭐**

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

---

**Desarrollado con 💜 por [Arkanabytes](https://github.com/Arkanabytes)**

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" width="100%">

</div>
