-- It creates table id_not_null on my MySQL server
-- If table id_not_null already exists, your script should not fail

CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id`   INT          DEFAULT 1,
    `name` VARCHAR(256));
