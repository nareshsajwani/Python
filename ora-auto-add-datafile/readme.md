# Oracle Tablespace Auto Datafile Management

## Overview

Oracle database environments often contain hundreds of databases spread across multiple application domains and storage layouts. Manually identifying tablespaces requiring growth and determining the appropriate filesystem for additional datafiles is time-consuming and error-prone.

This project automates discovery, analysis, SQL generation, validation, and future execution of Oracle datafile additions across large database estates.

The solution supports both:

* Non-CDB databases
* Oracle Multitenant (CDB/PDB) databases

and follows standardized filesystem naming conventions used across enterprise environments.

---

## Objectives

Automate the following activities:

1. Identify tablespaces exceeding utilization thresholds.
2. Select appropriate filesystem targets.
3. Generate standardized ADD DATAFILE statements.
4. Support both application and index tablespaces.
5. Support large-scale execution across hundreds of databases.
6. Produce auditable reports and exception logs.

---

## Environment Assumptions

### Non-CDB

Datafiles follow:

```text
/data01/<instance_name>/users_01.dbf
/index01/<instance_name>/users_idx_01.dbf
```

### CDB/PDB

PDB-specific storage groups:

```text
/data_a22_01/<pdb_name>/users_01.dbf
/index_a22_01/<pdb_name>/users_idx_01.dbf
```

Example:

PDB:

```text
AWSCDBPDA22
```

Storage group:

```text
/data_a22_*
/index_a22_*
```

---

# Project Phases

## Phase 1A – Discovery Framework

### Goals

Validate connectivity and inventory collection.

### Features

* Read input file
* Detect CDB / Non-CDB
* Oracle connectivity validation
* SSH filesystem discovery
* PDB discovery
* Parallel processing
* Exception reporting

### Deliverables

* discovery_report.csv
* pdb_report.csv
* filesystem_report.csv
* exceptions.csv

---

## Phase 1B – Tablespace Analysis

### Goals

Identify growth candidates.

### Features

* Query DBA_TABLESPACE_USAGE_METRICS
* Ignore:

  * SYSTEM
  * SYSAUX
  * TEMP*
  * UNDO*
* Identify tablespaces > 85% utilized
* Capture tablespace size

### Deliverables

* tablespace_candidate_report.csv

---

## Phase 1C – SQL Generation

### Goals

Generate ADD DATAFILE statements.

### Features

* Determine latest datafile naming pattern
* Extract filename prefix
* Determine next sequence number
* Filesystem selection based on least utilization
* Lowercase path enforcement

### Rules

#### Tablespace <= 500 GB

Generate:

```sql
ALTER TABLESPACE USERS
ADD DATAFILE '/data02/finprd/users_08.dbf'
SIZE 30G;
```

#### Tablespace > 500 GB

Generate two datafiles across separate filesystems.

### Deliverables

* generated_datafiles.sql
* sql_generation_report.csv

---

## Phase 2 – Validation Framework

### Goals

Perform pre-execution validation.

### Features

* Verify filesystem capacity
* Validate naming conventions
* Validate generated SQL
* Capacity forecasting

### Deliverables

* validation_report.csv

---

## Phase 3 – Automated Execution

### Goals

Execute generated SQL safely.

### Features

* Controlled execution mode
* Rollback logging
* Execution audit trail
* Success / failure tracking
* Parallel execution controls

### Deliverables

* execution_report.csv
* execution_logs/

---

# Technical Design

## Database Detection

Configured through:

```python
CDB_IDENTIFIER = "dvc"
```

Examples:

DEV:

```python
CDB_IDENTIFIER = "dvc"
```

PROD:

```python
CDB_IDENTIFIER = "pdc"
```

---

## Oracle Users

### Non-CDB

```text
dba
```

### CDB

```text
C##dba
```

---

## SSH User

```text
cloud-user
```

---

## Parallelism

Initial execution:

```python
MAX_WORKERS = 2
```

Designed for gradual scaling after validation.

---

# Future Enhancements

* ASM support
* ServiceNow ticket integration
* Email notifications
* REST API interface
* Grafana dashboard integration
* AI-assisted capacity forecasting

---

# Author

Naresh Sajwani

Senior Oracle DBA | Automation | DevOps Learning Journey

This project is part of a broader effort to modernize Oracle DBA operations through automation and Python-based tooling.
