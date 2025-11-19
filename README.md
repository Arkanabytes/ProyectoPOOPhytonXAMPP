<div align="center">

# 🎓 Sistema de Gestión Universitaria
### POO Python + XAMPP + PyMySQL

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

# 🏗️ Arquitectura del Sistema

## Sistema de Gestión Universitaria - POO Python + XAMPP

</div>

---

## 📐 Arquitectura General en Capas

```mermaid
graph TB
    subgraph "🎨 Capa de Presentación"
        UI[Interface de Usuario<br/>main.py]
        CLI[Command Line Interface]
    end
    
    subgraph "🧠 Capa de Lógica de Negocio"
        subgraph "👥 Módulo Usuarios"
            U[Usuario<br/><<abstract>>]
            E[Estudiante]
            C[Conductor]
        end
        
        subgraph "🛒 Módulo Comercio"
            PED[Pedido]
            PROD[Producto]
        end
        
        subgraph "📚 Módulo Académico"
            ASG[Asignatura]
            HOR[Horario]
        end
    end
    
    subgraph "💾 Capa de Acceso a Datos"
        subgraph "🗄️ DAOs"
            EDAO[EstudianteDAO]
            PDAO[PedidoDAO]
            ADAO[AsignaturaDAO]
        end
        
        DBC[DatabaseConnection<br/><<Singleton>>]
    end
    
    subgraph "🗃️ Capa de Persistencia"
        DB[(MySQL Database<br/>XAMPP Server)]
    end
    
    UI --> E
    UI --> C
    UI --> PED
    CLI --> U
    
    E -.-> EDAO
    PED -.-> PDAO
    ASG -.-> ADAO
    
    EDAO --> DBC
    PDAO --> DBC
    ADAO --> DBC
    
    DBC --> DB
    
    U --> E
    U --> C
    
    E --> ASG
    E --> PED
    PED --> PROD
    HOR --> ASG
    
    style UI fill:#a855f7,stroke:#7e22ce,color:#fff
    style E fill:#3b82f6,stroke:#1e40af,color:#fff
    style C fill:#3b82f6,stroke:#1e40af,color:#fff
    style PED fill:#10b981,stroke:#059669,color:#fff
    style ASG fill:#f59e0b,stroke:#d97706,color:#fff
    style DBC fill:#ef4444,stroke:#dc2626,color:#fff
    style DB fill:#6366f1,stroke:#4f46e5,color:#fff
```

---

## 🔄 Arquitectura MVC Adaptada

```mermaid
graph LR
    subgraph "📱 View Layer"
        V1[main.py]
        V2[CLI Interface]
        V3[User Inputs]
    end
    
    subgraph "🎮 Controller Layer"
        C1[Business Logic]
        C2[Validators]
        C3[Handlers]
    end
    
    subgraph "📦 Model Layer"
        M1[Domain Models]
        M2[Entities]
        M3[Value Objects]
    end
    
    subgraph "💾 Data Layer"
        D1[DAOs]
        D2[Connection Pool]
        D3[MySQL DB]
    end
    
    V1 --> C1
    V2 --> C2
    V3 --> C3
    
    C1 --> M1
    C2 --> M2
    C3 --> M3
    
    M1 --> D1
    M2 --> D1
    M3 --> D1
    
    D1 --> D2
    D2 --> D3
    
    style V1 fill:#a855f7
    style C1 fill:#3b82f6
    style M1 fill:#10b981
    style D1 fill:#f59e0b
```

---

## 🧩 Diagrama de Componentes

```mermaid
graph TB
    subgraph "Sistema de Gestión Universitaria"
        subgraph "🎯 Core Components"
            APP[Application<br/>Entry Point]
            CONF[Configuration<br/>Manager]
        end
        
        subgraph "👥 User Management"
            UM[User Module]
            EST[Student Component]
            COND[Driver Component]
        end
        
        subgraph "🛒 Commerce System"
            CS[Commerce Module]
            CART[Shopping Cart]
            ORDER[Order Processing]
        end
        
        subgraph "📚 Academic System"
            AS[Academic Module]
            SUBJ[Subject Management]
            SCHED[Schedule Manager]
        end
        
        subgraph "💾 Data Access Layer"
            DAO[DAO Factory]
            CONN[Connection Manager]
            CACHE[Cache Layer]
        end
        
        subgraph "🔧 Utilities"
            VALID[Validators]
            LOG[Logger]
            UTILS[Helpers]
        end
    end
    
    subgraph "🗄️ External Systems"
        MYSQL[(MySQL<br/>Database)]
        XAMPP[XAMPP<br/>Server]
    end
    
    APP --> UM
    APP --> CS
    APP --> AS
    APP --> CONF
    
    UM --> EST
    UM --> COND
    
    CS --> CART
    CS --> ORDER
    
    AS --> SUBJ
    AS --> SCHED
    
    EST --> DAO
    COND --> DAO
    CART --> DAO
    ORDER --> DAO
    SUBJ --> DAO
    SCHED --> DAO
    
    DAO --> CONN
    CONN --> CACHE
    CONN --> MYSQL
    
    MYSQL --> XAMPP
    
    VALID -.-> EST
    VALID -.-> COND
    VALID -.-> ORDER
    
    LOG -.-> APP
    UTILS -.-> UM
    UTILS -.-> CS
    UTILS -.-> AS
    
    style APP fill:#a855f7,stroke:#7e22ce,color:#fff
    style UM fill:#3b82f6,stroke:#1e40af,color:#fff
    style CS fill:#10b981,stroke:#059669,color:#fff
    style AS fill:#f59e0b,stroke:#d97706,color:#fff
    style DAO fill:#ef4444,stroke:#dc2626,color:#fff
    style MYSQL fill:#6366f1,stroke:#4f46e5,color:#fff
```

---

## 🔀 Flujo de Datos Principal

```mermaid
flowchart TD
    START([👤 Usuario]) --> INPUT[📝 Ingresa Datos]
    INPUT --> VALID{✅ Validación}
    
    VALID -->|❌ Error| ERROR[⚠️ Mostrar Error]
    ERROR --> INPUT
    
    VALID -->|✓ OK| PROCESS[⚙️ Procesar Lógica<br/>de Negocio]
    
    PROCESS --> MODEL[📦 Crear/Actualizar<br/>Modelo]
    MODEL --> DAO[💾 Llamar DAO]
    
    DAO --> CHECK{🔍 Verificar<br/>Conexión}
    CHECK -->|❌ No conectado| CONNECT[🔌 Conectar a BD]
    CONNECT --> CHECK
    
    CHECK -->|✓ Conectado| QUERY[📊 Ejecutar Query SQL]
    QUERY --> RESULT{📈 Resultado}
    
    RESULT -->|❌ Error SQL| ROLLBACK[↩️ Rollback]
    ROLLBACK --> ERROR2[⚠️ Error BD]
    ERROR2 --> END1([🔚 Fin con Error])
    
    RESULT -->|✓ Éxito| COMMIT[✅ Commit]
    COMMIT --> RESPONSE[📤 Preparar Respuesta]
    RESPONSE --> DISPLAY[🖥️ Mostrar Resultado]
    DISPLAY --> END2([🎉 Fin Exitoso])
    
    style START fill:#a855f7,color:#fff
    style VALID fill:#3b82f6,color:#fff
    style PROCESS fill:#10b981,color:#fff
    style DAO fill:#f59e0b,color:#fff
    style QUERY fill:#ef4444,color:#fff
    style END2 fill:#22c55e,color:#fff
    style END1 fill:#dc2626,color:#fff
```

---

## 🎯 Patrón DAO en Acción

```mermaid
sequenceDiagram
    participant UI as 🖥️ UI/Main
    participant Model as 📦 Modelo
    participant DAO as 💾 DAO
    participant Conn as 🔌 Connection
    participant DB as 🗄️ MySQL
    
    UI->>Model: 1. Crear Objeto
    activate Model
    Model-->>UI: 2. Objeto Creado
    deactivate Model
    
    UI->>DAO: 3. insertar(objeto)
    activate DAO
    
    DAO->>Conn: 4. get_connection()
    activate Conn
    Conn-->>DAO: 5. Connection
    deactivate Conn
    
    DAO->>DB: 6. INSERT INTO...
    activate DB
    DB-->>DAO: 7. ID generado
    deactivate DB
    
    DAO-->>UI: 8. Éxito/Error
    deactivate DAO
    
    Note over UI,DB: 💡 Patrón Singleton asegura<br/>única instancia de conexión
```

---

## 🏛️ Arquitectura de Clases (Herencia)

```mermaid
classDiagram
    Usuario <|-- Estudiante
    Usuario <|-- Conductor
    Estudiante "1" --> "*" Asignatura : inscribe
    Estudiante "1" --> "*" Pedido : realiza
    Pedido "1" --> "*" Producto : contiene
    Horario "1" --> "*" Asignatura : programa
    
    class Usuario {
        <<abstract>>
        #int id_usuario
        #str nombre
        #str email
        #str telefono
        +mostrar_info()*
    }
    
    class Estudiante {
        -str carrera
        -int anio
        -float saldo_cuenta
        -list asignaturas
        +pagar_servicio(monto)
        +agregar_saldo(monto)
        +inscribir_asignatura(asignatura)
    }
    
    class Conductor {
        -str patente
        -str tipo_vehiculo
        -float calificacion
        -list viajes
        +calcular_tarifa(distancia, tiempo, pasajeros)
        +registrar_viaje(origen, destino, distancia, tiempo, pasajeros)
    }
    
    class Pedido {
        -int id_pedido
        -int id_estudiante
        -list productos
        -float precio_total
        -str estado
        +agregar_producto(producto, cantidad)
        +confirmar()
        +cambiar_estado(nuevo_estado)
    }
    
    class Producto {
        -str nombre
        -float precio
        -str categoria
    }
    
    class Asignatura {
        -int id_asignatura
        -str nombre
        -str profesor
        -int creditos
    }
    
    class Horario {
        -int id_horario
        -str dia
        -time hora_inicio
        -time hora_fin
        -list asignaturas
        +agregar_asignatura(asignatura)
        +verificar_choque(otro_horario)
    }
```
---

## 🔐 Patrón Singleton - DatabaseConnection

```mermaid
classDiagram
    class DatabaseConnection {
        <<Singleton>>
        - _instance : DatabaseConnection
        - _connection : MySQLConnection
        - _host : str
        - _user : str
        - _password : str
        - _database : str
        ___________
        - __new__()
        + connect(host, user, password, database) void
        + get_connection() MySQLConnection
        + close() void
        + execute_query(query, params) list
        + execute_update(query, params) int
    }
    
    class EstudianteDAO {
        - db : DatabaseConnection
        ___________
        + insertar(estudiante) int
        + obtener(id) Estudiante
        + actualizar(estudiante) bool
        + eliminar(id) bool
        + listar_todos() list
    }
    
    class PedidoDAO {
        - db : DatabaseConnection
        ___________
        + insertar(pedido) int
        + obtener(id) Pedido
        + actualizar(pedido) bool
        + eliminar(id) bool
        + obtener_por_estudiante(id) list
    }
    
    class AsignaturaDAO {
        - db : DatabaseConnection
        ___________
        + insertar(asignatura) int
        + obtener(id) Asignatura
        + actualizar(asignatura) bool
        + eliminar(id) bool
        + inscribir_estudiante(id_est, id_asg) bool
    }
    
    DatabaseConnection "1" <-- "*" EstudianteDAO : usa
    DatabaseConnection "1" <-- "*" PedidoDAO : usa
    DatabaseConnection "1" <-- "*" AsignaturaDAO : usa
    
    note for DatabaseConnection "Garantiza una única\ninstancia de conexión\nen toda la aplicación"
```

---

## 🔄 Ciclo de Vida de una Transacción

```mermaid
stateDiagram-v2
    [*] --> Inicio
    
    Inicio --> ValidarDatos : Usuario ingresa datos
    
    ValidarDatos --> CrearModelo : ✅ Datos válidos
    ValidarDatos --> MostrarError : ❌ Datos inválidos
    MostrarError --> Inicio
    
    CrearModelo --> ObtenerConexion : Modelo creado
    
    ObtenerConexion --> VerificarConexion
    
    VerificarConexion --> Conectar : No conectado
    VerificarConexion --> PrepararQuery : Conectado
    Conectar --> PrepararQuery
    
    PrepararQuery --> EjecutarQuery
    
    EjecutarQuery --> ValidarResultado
    
    ValidarResultado --> Commit : ✅ Éxito
    ValidarResultado --> Rollback : ❌ Error
    
    Commit --> ActualizarModelo
    Rollback --> ManejarError
    
    ActualizarModelo --> MostrarExito
    ManejarError --> MostrarError
    
    MostrarExito --> [*]
    MostrarError --> [*]
    
    note right of ValidarDatos
        Validación en capa
        de presentación
    end note
    
    note right of EjecutarQuery
        Transacción SQL
        con MySQL
    end note
    
    note right of Commit
        COMMIT en BD
        Cambios permanentes
    end note
```

---

## 📊 Flujo de Inscripción de Asignatura

```mermaid
sequenceDiagram
    participant U as 👤 Usuario
    participant UI as 🖥️ Interfaz
    participant E as 🎓 Estudiante
    participant EDAO as 💾 EstudianteDAO
    participant ADAO as 💾 AsignaturaDAO
    participant DB as 🗄️ MySQL
    
    U->>UI: Selecciona asignatura
    UI->>E: obtener_estudiante(id)
    
    E->>EDAO: obtener(id_estudiante)
    EDAO->>DB: SELECT * FROM estudiantes
    DB-->>EDAO: Datos estudiante
    EDAO-->>E: Estudiante
    
    E->>ADAO: obtener(id_asignatura)
    ADAO->>DB: SELECT * FROM asignaturas
    DB-->>ADAO: Datos asignatura
    ADAO-->>E: Asignatura
    
    E->>E: verificar_requisitos()
    
    alt ✅ Requisitos cumplidos
        E->>ADAO: inscribir_estudiante()
        ADAO->>DB: INSERT INTO estudiante_asignatura
        DB-->>ADAO: ✓ Inscripción exitosa
        ADAO-->>E: true
        E->>E: agregar_a_lista(asignatura)
        E-->>UI: ✅ Inscripción exitosa
        UI-->>U: Mostrar confirmación
    else ❌ Requisitos no cumplidos
        E-->>UI: ⚠️ Error: Requisitos no cumplidos
        UI-->>U: Mostrar error
    end
```

---

## 🗺️ Diagrama de Despliegue

```mermaid
graph TB
    subgraph "💻 Cliente / Desarrollador"
        DEV[Python Application<br/>main.py]
        CLI[Command Line<br/>Interface]
    end
    
    subgraph "🖥️ Servidor Local (XAMPP)"
        subgraph "🌐 Apache Server"
            PHP[phpMyAdmin<br/>:80]
        end
        
        subgraph "🗄️ MySQL Server"
            MYSQL[(Database<br/>sistema_universitario<br/>:3306)]
        end
    end
    
    subgraph "📦 Módulos Python"
        MODELS[models/<br/>├─ usuario.py<br/>├─ estudiante.py<br/>├─ conductor.py<br/>└─ ...]
        
        DAOS[dao/<br/>├─ database_connection.py<br/>├─ estudiante_dao.py<br/>└─ ...]
    end
    
    DEV --> CLI
    CLI --> MODELS
    MODELS --> DAOS
    
    DAOS -->|mysql-connector-python<br/>Port: 3306| MYSQL
    
    PHP -->|Administración| MYSQL
    
    DEV -.->|Monitoreo| PHP
    
    style DEV fill:#a855f7,color:#fff
    style MYSQL fill:#4479A1,color:#fff
    style PHP fill:#FB7A24,color:#fff
    style MODELS fill:#3b82f6,color:#fff
    style DAOS fill:#10b981,color:#fff
```

---

## 🎨 Arquitectura de Paquetes

```mermaid
graph LR
    subgraph "📦 Proyecto Root"
        subgraph "models"
            M1[usuario.py]
            M2[estudiante.py]
            M3[conductor.py]
            M4[pedido.py]
            M5[producto.py]
            M6[asignatura.py]
            M7[horario.py]
        end
        
        subgraph "dao"
            D1[database_connection.py]
            D2[estudiante_dao.py]
            D3[pedido_dao.py]
            D4[asignatura_dao.py]
        end
        
        subgraph "sql"
            S1[schema.sql]
            S2[data.sql]
        end
        
        subgraph "utils"
            U1[validators.py]
            U2[helpers.py]
        end
        
        MAIN[main.py]
        CONFIG[config.py]
    end
    
    MAIN --> M2
    MAIN --> M3
    MAIN --> M4
    
    M2 --> M1
    M3 --> M1
    M2 --> M6
    M2 --> M4
    M4 --> M5
    M7 --> M6
    
    M2 --> D2
    M4 --> D3
    M6 --> D4
    
    D2 --> D1
    D3 --> D1
    D4 --> D1
    
    D1 --> CONFIG
    
    M2 -.-> U1
    M3 -.-> U1
    M4 -.-> U2
    
    style MAIN fill:#a855f7,color:#fff
    style D1 fill:#ef4444,color:#fff
    style CONFIG fill:#f59e0b,color:#fff
```

---

<div align="center">

## 📚 Leyenda de Símbolos

| Símbolo | Significado |
|---------|-------------|
| `-->` | Dependencia directa / Herencia |
| `-.->` | Dependencia débil / Uso ocasional |
| `===>` | Flujo de datos |
| `subgraph` | Agrupación lógica |
| `<<abstract>>` | Clase abstracta |
| `<<Singleton>>` | Patrón Singleton |

</div>

---

<div align="center">

**🏗️ Arquitectura diseñada con principios SOLID y Patrones de Diseño**

*Desarrollado por [Arkanabytes](https://github.com/Arkanabytes)*

</div>

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
