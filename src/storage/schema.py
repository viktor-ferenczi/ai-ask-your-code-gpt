from typing import Dict

VERSION = 1

DROP = '''

drop table public.property;
drop table public.task;
drop table public.archive;
drop table public.project;
drop table public.document;
drop table public.fragment;
drop table public.file;
drop table public.usage;

drop type public.task_state;

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
    created   timestamp  default (CURRENT_TIMESTAMP AT TIME ZONE 'utc'::text) not null
        constraint task_pk
            primary key,
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

create table public.archive
(
    checksum varchar(64)  not null
        constraint archive_pk
            primary key,
    path varchar(400) not null,
    size bigint not null,
    url  varchar(400) not null,
    etag varchar(80) not null,
    common_base_dir varchar(400) not null
);

alter table public.archive
    owner to askyourcode;

create index archive_path_index
    on public.archive (path);

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
    checksum      varchar(64)                                   not null,
    body          bytea                                         not null,
    length        integer                                       not null,
    doctype       varchar(40) default 'text'::character varying not null,
    constraint document_pk
        primary key (partition_key, checksum)
);

alter table public.document
    owner to askyourcode;

create table public.fragment
(
    partition_key char(2)               not null,
    document_cs   varchar(64)           not null,
    start         integer      not null,
    length        integer               not null,
    lineno        integer      not null,
    tokens        integer               not null,
    depth         integer      not null,
    parent_id     integer,
    category      varchar(24)           not null,
    definition    boolean               not null,
    summary       boolean  not null,
    name          varchar(80)           not null,
    body          text                  not null,
    constraint fragment_pk
        primary key (partition_key, document_cs, start)
);

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
    path_in_project varchar(400) not null,
    mime_type       varchar(40)  not null,
    size            bigint       not null,
    document_cs     varchar(64),
    archive_cs      varchar(64),
    constraint file_pk
        primary key (id)
);

alter table public.file
    owner to askyourcode;

create index file_path_in_project_index
    on public.file (project_id, path_in_project);
    
create table public.usage
(
    partition_key      char(2) not null,
    project_id         bigint  not null,
    definition_file_id bigint  not null,
    definition_start   integer not null,
    usage_file_id      bigint  not null,
    usage_start        integer not null,
    constraint usage_pk
        primary key (partition_key, project_id, definition_file_id, definition_start, usage_file_id, usage_start)
);

alter table public.usage
    owner to askyourcode;
    
create index usage_index
    on public.usage (usage_file_id, usage_start);

''' + f'''
insert into public.property (name, number) values ('Version', {VERSION});
'''

MIGRATIONS: Dict[int, str] = {
    0: CREATE,
    # Insert incremental migrations from each past version here
}
