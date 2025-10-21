================
Interface Design
================

The Interface Design section describes how users and system components interact within the Football Player Absence Tracking System.

Data Flow Diagram
-----------------

.. plantuml:: ./diagrams/data_flow.puml

Data Model Design
-----------------

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