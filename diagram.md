```mermaid
graph TD;
    A[Rider / Driver (User)] -->|Interacts via browser| B[Frontend (React + TypeScript)];
    B -->|Sends HTTP requests| C[Backend (Django REST API)];
    C -->|Reads/Writes data| D[(PostgreSQL Database)];
    C -->|Returns JSON responses| B;
