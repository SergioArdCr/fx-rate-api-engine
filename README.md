# API – Hyperautomation 

Este proyecto implementa un **sistema de obtención y procesamiento de tasas de cambio** con enfoque en **Hyperautomation**, diseñado para escenarios empresariales reales donde:

- Las APIs externas pueden fallar
- Existen límites de consumo (HTTP 429 – Rate Limit)
- Se requiere tolerancia a fallos y continuidad operativa
- Es necesario desacoplar proveedores externos de la lógica de negocio

El sistema permite definir **múltiples proveedores de divisas con prioridades**, manejar errores por moneda y activar **fallback automático** cuando sea necesario.

---

## 🏗️ Arquitectura

```
api-hyperautomation/
│
├── config/
├── data/
├── logs/
├── diagrams/
│
├── src/
│   ├── application/
│   ├── domain/
│   ├── infrastructure/
│   ├── integration/
│   ├── observability/
│   └── main.py
│
├── requirements.txt
└── README.md

Esta estructura facilita:
- Escalabilidad
- Mantenibilidad
- Sustitución de proveedores
- Integración con plataformas de automatización empresarial

```

---

## 🔄 Flujo de ejecución

1. Se define una moneda base
2. Se configura una lista dinámica de monedas destino
3. Para cada moneda:
   - Se intenta obtener la tasa usando el proveedor de mayor prioridad
   - Si falla, se intenta con el siguiente proveedor
4. Se validan y normalizan los datos
5. Se activa fallback si es necesario

---

## 🌐 Proveedores

- **CurrencyLayer** – `/convert` (requiere API Key)
- **Open Exchange Rates** – `/latest` (sin API Key)

---

## 📁 Salidas

### JSON
Incluye tasas, timestamp, fecha procesada y flag de fallback.

### Logs
Errores por proveedor, rate limits, fallback y ejecuciones exitosas.

---

## ▶️ Ejecución

```bash
python -m src.main
```

---

## 🚀 Mejoras futuras

- Cache y circuit breaker
- Métricas y monitoreo
- Persistencia en base de datos
- Tests unitarios

### 🔹 Integración con Power Platform

- Consumo desde Power Automate
- Notificaciones en Teams
- Registro en Dataverse
- Orquestación RPA (Python + Power Platform)

---

## 👤 Autor

**Sergio Andres Ardila Cruz**  
Ingeniero Mecatrónico  
Especialización en Sistemas Gerenciales de Ingeniería  

Perfil orientado a:
- Hyperautomation
- Integración de sistemas
- Automatización empresarial
- Arquitectura de soluciones