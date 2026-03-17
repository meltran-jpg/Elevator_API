# already uploaded to the classroom repository but reuploaded just in case :)

# Melinda Tran

#elevator control api 

## Overview

Elevator control api provides a structured interface for managing a multi elevator system within a building

it abstracts elevator control, scheduling, and safety logic behind a clean extensible API


No implementation or hardware control is included

## features
- Elevator request handling
- Elevator state tracking
- Door and emergency control
- Clear separation of API, logic, and storage layers
## Architecture
- **API Layer**: Accepts requests from clients
- **Service Layer**: Contains business and scheduling logic
- **Models**: Define elevator and request data
- **Storage**: Maintains system state
- **Errors**: Centralized error definitions
## Design Goals
- Separation of concerns
- Testability
- Extensibility
- Hardware agnostic design
## Non-Goals
- Motor-level control
- Real-time guarantees
- UI implementation
## Intended Clients
- Elevator panels
- Building management systems
- Simulation tools
- Monitoring dashboards
