========
Overview
========

The FPATS system allows players to mark their attendance automatically by facing a tablet camera.  
The system recognizes the player’s face, retrieves their data, prompts for confirmation,  
and records their attendance into an Excel-like absence sheet.

**Main Components:**

- **Client (Tablet/iPad/Web App):** Captures face images and provides the UI for confirmation.
- **Server (Backend API):** Handles face recognition, player management, and attendance logging.
- **Database:** Stores player data, embeddings, and attendance records.
- **Admin Web Dashboard:** Provides management and reporting features.
- **Export Module:** Generates attendance reports (Excel/CSV).


Requirements
------------

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