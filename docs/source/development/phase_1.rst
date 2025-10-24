=====================================================
Phase 1 Validation Test Plan
=====================================================

**Project:** Absence System with Face Recognition  
**Phase:** Phase 1 — Core Integration & Foundational Validation  
**Role:** System Validator  
**Methodology:** Test-Driven Development (TDD)

-----------------------------------------------------
1. Objectives
-----------------------------------------------------

Phase 1 focuses on validating core functional integration between the system’s primary modules:

* Camera / Client → Server API → Face Recognition Service → Database

Goals:

1. Verify that core APIs comply with the high-level and interface design.  
2. Establish baseline tests for registration and attendance workflows.  
3. Ensure that data flows (images, embeddings, attendance records) follow correct structure and logic.  
4. Provide a repeatable validation suite for CI/CD.

-----------------------------------------------------
2. Scope of Phase 1
-----------------------------------------------------

+----------------+---------------------------------------------+------------------------------------------------+
| Layer          | Modules in Scope                            | Purpose                                        |
+================+=============================================+================================================+
| Unit           | ``face_recognition_service``, ``database``  | Confirm individual functions behave correctly. |
+----------------+---------------------------------------------+------------------------------------------------+
| Integration    | ``Server API`` ↔ ``Face Recognition`` ↔     | Verify inter-module contracts and response     |
|                | ``Database``                                | structure.                                     |
+----------------+---------------------------------------------+------------------------------------------------+
| System (light) | ``Client → API → DB`` flow (mock client)    | Validate end-to-end registration & check-in    |
|                |                                             | path.                                          |
+----------------+---------------------------------------------+------------------------------------------------+

Out of scope for Phase 1:

* User Interface / Web dashboard  
* Security (JWT / Auth)  
* Analytics and reporting

-----------------------------------------------------
3. Test Categories and Priorities
-----------------------------------------------------

+-----------------------------+-----------+--------------------------------------------------+
| Category                    | Priority  | Description                                      |
+=============================+===========+==================================================+
| Face Encoding & Matching    | High      | Validate recognition service correctness.        |
+-----------------------------+-----------+--------------------------------------------------+
| Player Registration API     | High      | Ensure player data and face embeddings stored.   |
+-----------------------------+-----------+--------------------------------------------------+
| Attendance Logging API      | High      | Validate recognized players create records.      |
+-----------------------------+-----------+--------------------------------------------------+
| Database Schema Tests       | Medium    | Confirm constraints and relations.               |
+-----------------------------+-----------+--------------------------------------------------+
| Error & Edge Case Tests     | Medium    | Handle unknown faces and invalid inputs.         |
+-----------------------------+-----------+--------------------------------------------------+

-----------------------------------------------------
4. Test Suite Structure
-----------------------------------------------------

::

   tests/
   ├── unit/
   │   ├── test_face_encoding.py
   │   ├── test_face_matching.py
   │   ├── test_database_models.py
   ├── integration/
   │   ├── test_api_register_player.py
   │   ├── test_api_check_in.py
   │   ├── test_api_error_cases.py
   ├── system/
   │   ├── test_end_to_end_attendance_flow.py
   ├── test_data/
   │   ├── sample_faces/
   │   │   ├── player_1.jpg
   │   │   ├── unknown.jpg
   │   ├── db_fixtures.json

-----------------------------------------------------
5. Test Descriptions
-----------------------------------------------------

**Unit Tests**

+------+-------------------+---------------------------------------------+---------------------------+
| ID   | Module            | Test Description                            | Expected Result           |
+======+===================+=============================================+===========================+
| U-01 | Face Service      | Encode valid face image → returns 128-dim   | Vector shape (128,)       |
|      |                   | vector                                      |                           |
+------+-------------------+---------------------------------------------+---------------------------+
| U-02 | Face Service      | Compare same face images → similarity > 0.9 | Pass                      |
+------+-------------------+-------------------------------------------+-----------------------------+
| U-03 | Face Service      | Compare different faces → similarity < 0.6  | Pass                      |
+------+-------------------+---------------------------------------------+---------------------------+
| U-04 | Database          | Insert + retrieve player record             | Data integrity maintained |
+------+-------------------+---------------------------------------------+---------------------------+
| U-05 | Database          | Foreign key Player → Attendance             | Constraint enforced       |
+------+-------------------+---------------------------------------------+---------------------------+

**Integration Tests**

+------+--------------------+---------------------------------------------+-----------------------------+
| ID   | Component          | Test Description                            | Expected Result             |
+======+====================+=============================================+=============================+
| I-01 | ``/register_face`` | POST valid image + metadata → DB entry      | 201 Created, ``player_id``  |
|      | API                | created                                     | returned                    |
+------+--------------------+---------------------------------------------+-----------------------------+
| I-02 | ``/check_in`` API  | POST known face → attendance record         | 200 OK, ``status=present``  |
|      |                    | inserted                                    |                             |
+------+--------------------+---------------------------------------------+-----------------------------+
| I-03 | ``/check_in`` API  | POST unknown face                           | 404 Not Found               |
+------+--------------------+---------------------------------------------+-----------------------------+
| I-04 | ``/register_face`` | Invalid file format                         | 400 Bad Request             |
| API  |                    |                                             |                             |
+------+--------------------+---------------------------------------------+-----------------------------+

**System Tests (End-to-End)**

+------+-----------------------------+----------------------------------------------+--------------------------------+
| ID   | Scenario                    | Description                                  | Expected Result                |
+======+=============================+==============================================+================================+
| S-01 | Registration → Check-in flow| Simulate full flow using mock client         | Player registered and present  |
+------+-----------------------------+----------------------------------------------+--------------------------------+
| S-02 | Duplicate check-in          | Same player checks in twice                  | Only one record created        |
+------+-----------------------------+----------------------------------------------+--------------------------------+
| S-03 | Database persistence        | Restart API and re-check player data         | Data retained in database      |
+------+-----------------------------+----------------------------------------------+--------------------------------+

-----------------------------------------------------
6. Tooling and Environment
-----------------------------------------------------

+----------------------------+-----------------------------+
| Purpose                    | Tool                        |
+============================+=============================+
| Testing framework          | ``pytest``                  |
+----------------------------+-----------------------------+
| HTTP client                | FastAPI ``TestClient``      |
+----------------------------+-----------------------------+
| Mocking                    | ``pytest-mock``             |
+----------------------------+-----------------------------+
| Test database              | SQLite (in-memory)          |
+----------------------------+-----------------------------+
| Face recognition mock      | Fixed sample embeddings     |
+----------------------------+-----------------------------+
| CI/CD pipeline             | GitHub Actions              |
+----------------------------+-----------------------------+

-----------------------------------------------------
7. Workflow Between Validator and Developer
-----------------------------------------------------

1. **Validator Phase**
   * Write tests according to this plan.
   * Ensure tests initially fail.
   * Commit under branch ``tests/phase1``.

2. **Developer Phase**
   * Pull tests and implement minimal code to make them pass.
   * Push passing code for review.

3. **Validation Phase**
   * Run tests in CI pipeline.
   * Update coverage and traceability matrix.

4. **Iteration**
   * Extend tests for new modules after Phase 1 passes.

-----------------------------------------------------
8. Traceability Matrix (Partial)
-----------------------------------------------------

+---------+-------------------------------+------------------------------+---------------------------+
| Req ID  | Description                   | Test IDs                     | Coverage Type             |
+=========+===============================+==============================+===========================+
| FR-001  | Player registration           | I-01, S-01                   | Integration, System       |
+---------+-------------------------------+------------------------------+---------------------------+
| FR-002  | Face recognition accuracy     | U-01 – U-03                  | Unit                      |
+---------+-------------------------------+------------------------------+---------------------------+
| FR-003  | Attendance logging            | I-02, S-01, S-02             | Integration, System       |
+---------+-------------------------------+------------------------------+---------------------------+
| FR-004  | Data consistency              | U-04, U-05, S-03             | Unit, System              |
+---------+-------------------------------+------------------------------+---------------------------+
| FR-005  | Error handling                | I-03, I-04                   | Integration               |
+---------+-------------------------------+------------------------------+---------------------------+

-----------------------------------------------------
9. Expected Outcomes
-----------------------------------------------------

* All unit and integration tests pass.  
* End-to-end check-in scenario functions with test data.  
* Code coverage ≥ 85 %.  
* Database schema and API routes validated against design.
