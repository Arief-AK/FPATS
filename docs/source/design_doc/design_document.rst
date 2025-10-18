System Design
=============

1. System Overview
------------------

The FPATS system allows players to mark their attendance automatically by facing a tablet camera.  
The system recognizes the player’s face, retrieves their data, prompts for confirmation,  
and records their attendance into an Excel-like absence sheet.

**Main Components:**

- **Client (Tablet/iPad/Web App):** Captures face images and provides the UI for confirmation.
- **Server (Backend API):** Handles face recognition, player management, and attendance logging.
- **Database:** Stores player data, embeddings, and attendance records.
- **Admin Web Dashboard:** Provides management and reporting features.
- **Export Module:** Generates attendance reports (Excel/CSV).

2. System Goals and Requirements
--------------------------------

**Functional Requirements**

1. Register new players with reference images.
2. Perform facial recognition against registered embeddings.
3. Display player information for confirmation.
4. Record attendance upon confirmation.
5. Export attendance logs as Excel or CSV files.

**Non-Functional Requirements**

- **Accuracy:** ≥ 90% under typical lighting.
- **Latency:** < 5 seconds from capture to recognition.
- **Scalability:** Support up to 50 players and multiple clients.
- **Security:** Use HTTPS and data protection for face data.
- **Portability:** Deployable on Jetson Orin/RaspberryPi or local server.

**Attendance Flow**

.. plantuml:: ./diagrams/attendance_flow.puml

3. High-Level Architecture
--------------------------
.. plantuml:: ./diagrams/architecture.puml

4. Module Breakdown
-------------------

+---------------------------+-------------------------------------------+----------------------------------+
| **Module**                | **Responsibilities**                      | **Technology Options**           |
+===========================+===========================================+==================================+
| Client Application        | Capture player face, send image, display  | React, Vue, or HTML5 + JS        |
|                           | match result, confirm attendance          |                                  |
+---------------------------+-------------------------------------------+----------------------------------+
| Recognition Service       | Extract embeddings, match against database| Python + ``face_recognition`` or |
|                           | embeddings                                | DeepFace                         |
+---------------------------+-------------------------------------------+----------------------------------+
| Player Management API     | CRUD for players, embedding storage       | FastAPI + SQLAlchemy             |
+---------------------------+-------------------------------------------+----------------------------------+
| Attendance Logging API    | Record attendance entries                 | FastAPI + SQLite/PostgreSQL      |
+---------------------------+-------------------------------------------+----------------------------------+
| Data Exporter             | Generate Excel/CSV reports                | Pandas + openpyxl                |
+---------------------------+-------------------------------------------+----------------------------------+
| Admin Dashboard           | Manage players and attendance data        | React or Streamlit               |
+---------------------------+-------------------------------------------+----------------------------------+
| Database Layer            | Persistent storage for players and logs   | SQLite (dev), PostgreSQL (prod)  |
+---------------------------+-------------------------------------------+----------------------------------+
| Object Storage            | Store face images                         | Local FS or MinIO/S3             |
+---------------------------+-------------------------------------------+----------------------------------+

5. Data Flow Diagram
--------------------

.. plantuml:: ./diagrams/data_flow.puml

6. Data Model Design
--------------------

``players``
~~~~~~~~~~~~

+--------------+---------------+---------------------------------+
| **Field**    | **Type**      | **Description**                 |
+==============+===============+=================================+
| id           | INT (PK)      | Unique player ID                |
+--------------+---------------+---------------------------------+
| name         | TEXT          | Player’s full name              |
+--------------+---------------+---------------------------------+
| team         | TEXT          | Team or group name              |
+--------------+---------------+---------------------------------+
| image_url    | TEXT          | Path to stored face image       |
+--------------+---------------+---------------------------------+
| face_encoding| BLOB/JSON     | Serialized facial embedding     |
+--------------+---------------+---------------------------------+
| created_at   | DATETIME      | Registration timestamp          |
+--------------+---------------+---------------------------------+


``attendance``
~~~~~~~~~~~~~~

+--------------+---------------+---------------------------------+
| **Field**    | **Type**      | **Description**                 |
+==============+===============+=================================+
| id           | INT (PK)      | Unique record ID                |
+--------------+---------------+---------------------------------+
| player_id    | INT (FK)      | Reference to players table      |
+--------------+---------------+---------------------------------+
| timestamp    | DATETIME      | Recognition time                |
+--------------+---------------+---------------------------------+
| status       | TEXT          | Example: “Present”              |
+--------------+---------------+---------------------------------+
| session_id   | TEXT          | Optional session identifier     |
+--------------+---------------+---------------------------------+

7. Technology Stack
-------------------

+--------------------+---------------------------+----------------------------------------+
| **Layer**          | **Technology**            | **Reason**                             |
+====================+===========================+========================================+
| Frontend (Client)  | React / HTML5 + JS        | Fast iteration and camera access       |
+--------------------+---------------------------+----------------------------------------+
| Backend (API)      | FastAPI (Python)          | Lightweight, async, ML-friendly        |
+--------------------+---------------------------+----------------------------------------+
| Face Recognition   | ``face_recognition`` or   | Established, accurate, easy to use     |
|                    | DeepFace                  |                                        |
+--------------------+---------------------------+----------------------------------------+
| Database           | SQLite / PostgreSQL       | Lightweight → scalable                 |
+--------------------+---------------------------+----------------------------------------+
| Storage            | Local FS / MinIO          | For player images and exports          |
+--------------------+---------------------------+----------------------------------------+
| Export             | Pandas + openpyxl         | Easy Excel/CSV generation              |
+--------------------+---------------------------+----------------------------------------+
| Deployment         | Docker Compose            | Modular and portable                   |
+--------------------+---------------------------+----------------------------------------+

8. Security and Privacy
-----------------------

- Use HTTPS for all client–server communication.
- Store embeddings instead of raw face images where possible.
- Obtain player consent before registration (GDPR compliance).