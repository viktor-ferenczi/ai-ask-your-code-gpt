VERSION = 1

DROP = '''
DROP TABLE IF EXISTS public."Tasks" CASCADE;
DROP TABLE IF EXISTS public."Properties" CASCADE;
DROP TYPE IF EXISTS public."TaskState" CASCADE;

DROP TABLE IF EXISTS "tasks" CASCADE;
DROP TABLE IF EXISTS "properties" CASCADE;
DROP TYPE IF EXISTS "taskstate" CASCADE;
'''

CREATE = '''
CREATE TYPE TaskState AS ENUM ('new', 'running', 'completed', 'failed', 'crashed');

-- Properties
CREATE TABLE "Properties"
(
    name      varchar(50) not null constraint properties_pk primary key,
    text      varchar(50),
    number    bigint
);

COMMENT ON COLUMN "Properties".name IS 'Unique name';
COMMENT ON COLUMN "Properties".text IS 'Text value';
COMMENT ON COLUMN "Properties".number IS 'Numeric value';

INSERT INTO "Properties" (name, number) VALUES ('Version', %(VERSION)d);

ALTER TABLE "Properties" OWNER TO askyourcode;

-- Tasks
CREATE TABLE "Tasks"
(
    name      varchar(50)  not null,
    project   varchar(36)  null,
    params    text  null,
    state     TaskState  default 'new',
    created   timestamp  default (current_timestamp at time zone 'utc')  not null  constraint tasks_pk  primary key,
    started   timestamp  null,
    finished  timestamp  null,
    message   text  null,
    traceback text  null
);

COMMENT ON COLUMN "Tasks".name IS 'Name (type) of the task.';
COMMENT ON COLUMN "Tasks".project IS 'Project identifier.';
COMMENT ON COLUMN "Tasks".params IS 'JSON encoded parameters, actual fields depend on the task.';
COMMENT ON COLUMN "Tasks".state IS 'Current state of the task.';
COMMENT ON COLUMN "Tasks".created IS 'When the task was created.';
COMMENT ON COLUMN "Tasks".started IS 'Processing start time.';
COMMENT ON COLUMN "Tasks".finished IS 'Processing finish time.';
COMMENT ON COLUMN "Tasks".message IS 'Message to send back to the user.';
COMMENT ON COLUMN "Tasks".traceback IS 'Traceback of an error in case of an unexpected failure.';

CREATE INDEX tasks_project ON "Tasks" (project);

ALTER TABLE "Tasks" OWNER TO askyourcode;
''' % dict(VERSION=VERSION)

MIGRATIONS = {
    0: CREATE,
    # Insert incremental migrations from each past version here
    VERSION: '',
}
