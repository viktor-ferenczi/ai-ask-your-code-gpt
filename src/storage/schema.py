from typing import Dict

VERSION = 1

DROP = '''
DROP TABLE IF EXISTS public."Fragment" CASCADE;
DROP TYPE IF EXISTS public."FragmentType" CASCADE;
DROP TABLE IF EXISTS public."File" CASCADE;
DROP TABLE IF EXISTS public."Archive" CASCADE;
DROP TABLE IF EXISTS public."Projects" CASCADE;
DROP TYPE IF EXISTS public."ProjectState" CASCADE;
DROP TABLE IF EXISTS public."Inventory" CASCADE;
DROP TABLE IF EXISTS public."Task" CASCADE;
DROP TYPE IF EXISTS public."TaskState" CASCADE;
DROP TABLE IF EXISTS public."Properties" CASCADE;
'''

CREATE = '''
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


CREATE TYPE TaskState AS ENUM ('new', 'running', 'completed', 'failed', 'crashed');

CREATE TABLE "Task"
(
    name      varchar(50)  not null,
    project   varchar(36)  null,
    params    text  null,
    state     TaskState  default 'new',
    created   timestamp  default (current_timestamp at time zone 'utc')  not null  constraint tasks_pk  primary key,
    started   timestamp  null,
    finished  timestamp  null,ss
    message   text  null,
    traceback text  null
);

COMMENT ON COLUMN "Task".name IS 'Name (type) of the task.';
COMMENT ON COLUMN "Task".project IS 'Project identifier.';
COMMENT ON COLUMN "Task".params IS 'JSON encoded parameters, actual fields depend on the task.';
COMMENT ON COLUMN "Task".state IS 'Current state of the task.';
COMMENT ON COLUMN "Task".created IS 'When the task was created.';
COMMENT ON COLUMN "Task".started IS 'Processing start time.';
COMMENT ON COLUMN "Task".finished IS 'Processing finish time.';
COMMENT ON COLUMN "Task".message IS 'Message to send back to the user.';
COMMENT ON COLUMN "Task".traceback IS 'Traceback of an error in case of an unexpected failure.';

CREATE INDEX tasks_project ON "Task" (project);

ALTER TABLE "Task" OWNER TO askyourcode;


CREATE TYPE ProjectState AS ENUM ('new', 'downloading', 'extracting', 'indexing', 'ready');

CREATE TABLE Project 
(
    id varchar(36) not null constraint project_pk primary key,
    name varchar(80) not null default '',
    state ProjectState not null default 'new',
    created timestamp not null default (current_timestamp at time zone 'utc'),
    last_used timestamp not null default (current_timestamp at time zone 'utc')
);


CREATE TABLE Archive
(
    id varchar(36) not null constraint archive_pk primary key,
    url varchar(400) not null constraint archive_pk primary key,
    name varchar(400) not null,
    path varchar(400) not null,
    checksum varchar(64) not null,
    etag varchar(160),
    created timestamp not null default (current_timestamp at time zone 'utc'),
    last_used timestamp not null default (current_timestamp at time zone 'utc')
);


CREATE TABLE File
(
    id bigserial not null constraint file_pk primary key,
    archive_id varchar(36) null constraint file_archive_fk foreign key, 
    path varchar(400) not null,
    size bigint not null,
    checksum varchar(64) not null,
    mime_type varchar(80) not null,
    encoding varchar(80) not null,
    indexed boolean not null,
    created timestamp not null default (current_timestamp at time zone 'utc'),
    last_used timestamp not null default (current_timestamp at time zone 'utc')
);


CREATE TYPE FragmentType AS ENUM ('doc', 'namespace', 'interface', 'class', 'function', 'method', 'variable');

CREATE TABLE Fragment 
(
    id bigserial not null constraint fragment_pk primary key,
    file_id bigint null constraint fragment_file_fk foreign key,
    parent_id bigint null foreign key,
    offset_in_bytes bigint not null default 0,
    size_in_bytes integer not null,
    lineno integer not null default 1,
    length integer not null,
    tokens integer not null,
    depth integer not null default 0,
    type FragmentType not null,
    name varchar(80) not null,
    definition boolean not null,
    text text not null
);

''' % dict(VERSION=VERSION)

MIGRATIONS: Dict[int, str] = {
    0: CREATE,
    # Insert incremental migrations from each past version here
}
