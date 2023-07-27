-- Tasks
SELECT COUNT(1) FROM task;

-- Counts
SELECT COUNT(1) FROM file;
SELECT COUNT(1) FROM document;
SELECT COUNT(1) FROM fragment;

-- Rows to delete
SELECT COUNT(1)
FROM file f
WHERE NOT EXISTS (
    SELECT 1
    FROM project p
    WHERE p.id = f.project_id
);

SELECT COUNT(1)
FROM document d
WHERE NOT EXISTS (
    SELECT 1
    FROM file f
    WHERE f.document_cs = d.checksum AND left(f.document_cs, 2) = d.partition_key
);

SELECT COUNT(1)
FROM fragment fr
WHERE NOT EXISTS (
    SELECT 1
    FROM document d
    WHERE d.checksum = fr.document_cs AND left(d.checksum, 2) = fr.partition_key
);


DELETE FROM file f
WHERE NOT EXISTS (
    SELECT 1
    FROM project p
    WHERE p.id = f.project_id
);