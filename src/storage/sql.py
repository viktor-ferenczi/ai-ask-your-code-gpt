GET_VERSION: str = """
    SELECT number FROM "Properties" WHERE name = 'Version' FOR UPDATE
"""

CREATE_TASK: str = """
    INSERT INTO "Tasks" (name, project, params)
    VALUES ($1, $2, $3)
    RETURNING created;
"""

LIST_PROJECT_TASKS: str = """
    SELECT created, started, finished, name, project, params, message, traceback 
    FROM "Tasks"
    WHERE name = $1 AND project = $2
    ORDER BY created;
"""

LIST_PENDING_TASKS: str = """
    SELECT created, started, finished, name, project, params, message, traceback 
    FROM "Tasks"
    WHERE name = $1 AND state = 'new'
    ORDER BY created;
"""

FETCH_NEXT_TASK_FOR_UPDATE: str = """
    SELECT * FROM "Tasks"
    WHERE name = $1 AND state = 'new'
    ORDER BY created
    LIMIT 1 FOR UPDATE SKIP LOCKED;
"""

FETCH_TASK_FOR_UPDATE: str = """
    SELECT * FROM "Tasks"
    WHERE created = $1
    LIMIT 1 FOR UPDATE SKIP LOCKED;
"""

SET_TASK_RUNNING: str = """
    UPDATE "Tasks"
    SET state = 'running',
        started = current_timestamp at time zone 'utc'
    WHERE created = $1 AND state = 'new'
    RETURNING state;
"""

SET_TASK_COMPLETED: str = """
    UPDATE "Tasks"
    SET state = 'completed',
        finished = current_timestamp at time zone 'utc'
    WHERE created = $1 AND state = 'running'
    RETURNING state;
"""

SET_TASK_FAILED: str = """
    UPDATE "Tasks"
    SET state = 'failed',
        message = $2,
        finished = current_timestamp at time zone 'utc'
    WHERE created = $1 AND state = 'running'
    RETURNING state;
"""

SET_TASK_CRASHED: str = """
    UPDATE "Tasks"
    SET state = 'crashed',
        traceback = $2,
        finished = current_timestamp at time zone 'utc'
    WHERE created = $1 AND state = 'running'
    RETURNING state;
"""

DELETE_TASK: str = """
    DELETE FROM "Tasks"
    WHERE created = $1
"""

RETRY_TASKS: str = """
    UPDATE "Tasks" SET started = NULL WHERE state = 'running'
"""

TRUNCATE_TASKS: str = """
    TRUNCATE "Tasks"
"""

GET_TASK: str = """
    SELECT * FROM "Tasks" WHERE created = $1
"""

UPDATE_TASK: str = """
    UPDATE "Tasks" SET project=$2 WHERE created = $1
"""
