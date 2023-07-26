-- Counts
select count(1) from document;
select count(1) from file;
select count(1) from fragment;

-- Slow
SELECT count(1) FROM file WHERE project_id NOT IN (SELECT id FROM project);
SELECT count(1) FROM document WHERE checksum NOT IN (SELECT document_cs FROM file);
SELECT count(1) FROM fragment WHERE document_cs NOT IN (SELECT checksum FROM document);

-- Fixed (turn them to DELETE)
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
