import re
from typing import Dict

VERSION = 1

DROP = '''

drop table if exists public.property;
drop table if exists public.task;
drop table if exists public.archive;
drop table if exists public.project;
drop table if exists public.document;
drop table if exists public.fragment;
drop table if exists public.file;
drop table if exists public.usage;

drop type if exists public.task_state;

'''

CREATE = '''

create type public.task_state as enum ('pending', 'completed', 'failed', 'crashed');

alter type public.task_state owner to askyourcode;

create table public.property
(
    name   varchar(50) not null
        constraint property_pk
            primary key,
    text   varchar(50),
    number bigint
);

comment on column public.property.name is 'Unique name';

comment on column public.property.text is 'Text value';

comment on column public.property.number is 'Numeric value';

alter table public.property
    owner to askyourcode;

create table public.task
(
    id        bigserial  constraint task_pk primary key, 
    created   timestamp                                                       not null,
    started   timestamp,
    finished  timestamp,
    state     task_state default 'pending'::task_state                        not null,
    operation varchar(30)                                                     not null,
    params    text       default '{}'::text                                   not null,
    message   text
);

comment on column public.task.created is 'When the task was created.';

comment on column public.task.started is 'Processing start time.';

comment on column public.task.finished is 'Processing finish time.';

comment on column public.task.state is 'Current state of the task.';

comment on column public.task.operation is 'Operation to execute, "type" of the task.';

comment on column public.task.params is 'JSON encoded parameters to pass to the operation, the actual fields depend on the operation.';

comment on column public.task.message is 'Message explaining the error if failed or a full traceback if crashed.';
   
alter table public.task
    owner to askyourcode;
    
create index task_created_state_index
    on public.task (created, state);


create table public.archive
(
    checksum char(64)  not null
        constraint archive_pk
            primary key,
    size bigint not null,
    count bigint not null,
    url  varchar(400) not null,
    etag varchar(160) not null,
    common_base_dir varchar(400) not null
);

alter table public.archive
    owner to askyourcode;

create index archive_url_index
    on public.archive (url);

create table public.project
(
    id       bigserial
        constraint project_pk
            primary key,
    uid      varchar(80)                                                    not null,
    name     varchar(80)                                                    not null,
    created  timestamp default (CURRENT_TIMESTAMP AT TIME ZONE 'utc'::text) not null,
    accessed timestamp default (CURRENT_TIMESTAMP AT TIME ZONE 'utc'::text) not null,
    constraint project_uid_name_unique
        unique (uid, name)
);

alter table public.project
    owner to askyourcode;

create table public.document
(
    partition_key char(2)                                       not null,
    checksum      char(64)                                      not null,
    doc_type      varchar(40)                                   not null,
    mime_type     varchar(96)                                   not null,
    size          bigint                                        not null,
    body          bytea                                         not null,
    constraint document_pk
        primary key (partition_key, checksum)
) partition by range (partition_key);

CREATE TABLE document_0 PARTITION OF document FOR VALUES FROM ('00') TO ('10');
CREATE TABLE document_1 PARTITION OF document FOR VALUES FROM ('10') TO ('20');
CREATE TABLE document_2 PARTITION OF document FOR VALUES FROM ('20') TO ('30');
CREATE TABLE document_3 PARTITION OF document FOR VALUES FROM ('30') TO ('40');
CREATE TABLE document_4 PARTITION OF document FOR VALUES FROM ('40') TO ('50');
CREATE TABLE document_5 PARTITION OF document FOR VALUES FROM ('50') TO ('60');
CREATE TABLE document_6 PARTITION OF document FOR VALUES FROM ('60') TO ('70');
CREATE TABLE document_7 PARTITION OF document FOR VALUES FROM ('70') TO ('80');
CREATE TABLE document_8 PARTITION OF document FOR VALUES FROM ('80') TO ('90');
CREATE TABLE document_9 PARTITION OF document FOR VALUES FROM ('90') TO ('a0');
CREATE TABLE document_a PARTITION OF document FOR VALUES FROM ('a0') TO ('b0');
CREATE TABLE document_b PARTITION OF document FOR VALUES FROM ('b0') TO ('c0');
CREATE TABLE document_c PARTITION OF document FOR VALUES FROM ('c0') TO ('d0');
CREATE TABLE document_d PARTITION OF document FOR VALUES FROM ('d0') TO ('e0');
CREATE TABLE document_e PARTITION OF document FOR VALUES FROM ('e0') TO ('f0');
CREATE TABLE document_f PARTITION OF document FOR VALUES FROM ('f0') TO ('g0');

alter table public.document
    owner to askyourcode;

create table public.fragment
(
    id            bigserial,
    partition_key char(2)               not null,
    document_cs   char(64)              not null,
    lineno        integer               not null,
    tokens        integer               not null,
    depth         integer               not null,
    parent_id     integer,
    category      varchar(24)           not null,
    summary       boolean               not null,
    name          varchar(160)          not null,
    body          text                  not null,
    constraint fragment_pk
        primary key (id, partition_key)    
) partition by range (partition_key);

CREATE TABLE fragment_0 PARTITION OF fragment FOR VALUES FROM ('00') TO ('10');
CREATE TABLE fragment_1 PARTITION OF fragment FOR VALUES FROM ('10') TO ('20');
CREATE TABLE fragment_2 PARTITION OF fragment FOR VALUES FROM ('20') TO ('30');
CREATE TABLE fragment_3 PARTITION OF fragment FOR VALUES FROM ('30') TO ('40');
CREATE TABLE fragment_4 PARTITION OF fragment FOR VALUES FROM ('40') TO ('50');
CREATE TABLE fragment_5 PARTITION OF fragment FOR VALUES FROM ('50') TO ('60');
CREATE TABLE fragment_6 PARTITION OF fragment FOR VALUES FROM ('60') TO ('70');
CREATE TABLE fragment_7 PARTITION OF fragment FOR VALUES FROM ('70') TO ('80');
CREATE TABLE fragment_8 PARTITION OF fragment FOR VALUES FROM ('80') TO ('90');
CREATE TABLE fragment_9 PARTITION OF fragment FOR VALUES FROM ('90') TO ('a0');
CREATE TABLE fragment_a PARTITION OF fragment FOR VALUES FROM ('a0') TO ('b0');
CREATE TABLE fragment_b PARTITION OF fragment FOR VALUES FROM ('b0') TO ('c0');
CREATE TABLE fragment_c PARTITION OF fragment FOR VALUES FROM ('c0') TO ('d0');
CREATE TABLE fragment_d PARTITION OF fragment FOR VALUES FROM ('d0') TO ('e0');
CREATE TABLE fragment_e PARTITION OF fragment FOR VALUES FROM ('e0') TO ('f0');
CREATE TABLE fragment_f PARTITION OF fragment FOR VALUES FROM ('f0') TO ('g0');

alter table public.fragment
    owner to askyourcode;

create index fragment_parent_id_index
    on public.fragment (parent_id);

create index fragment_body_index
    on public.fragment using gin (to_tsvector('english'::regconfig, body));

create table public.file
(
    id              bigserial,
    project_id      bigint       not null,
    path            varchar(400) not null,
    depth           integer      not null,
    document_cs     char(64),
    archive_cs      char(64),
    constraint file_pk
        primary key (id)
);

alter table public.file
    owner to askyourcode;

create index file_path_index
    on public.file (project_id, path);
    
''' + f'''
insert into public.property (name, number) values ('Version', {VERSION});
'''

RX_ALTER_OWNER = re.compile(r'alter ([a-z]+) .*?owner to .*?;', re.IGNORECASE | re.DOTALL)
CREATE = RX_ALTER_OWNER.subn('', CREATE)[0]

MIGRATIONS: Dict[int, str] = {
    0: CREATE,
    # Insert incremental migrations from each past version here
}
