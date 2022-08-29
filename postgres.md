### psql, base
- `psql -U <DB_USER> -d <DB_NAME> -f /file.sql` - прогнать sql скрипт
- `psql -h localhost -p 5432 -U postgres -W -d dbname` - подключиться к базе dbname на localhost:5432 под юзером postgres и prompt пароль (-W);
- [psql commands](https://www.postgresqltutorial.com/psql-commands/);
- когда в psql, то запрос вот так делать: `SELECT * FROM some_table;`

## show tables
- `\dt`
- `SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;`
- 

### Инфа о полях таблицы
```
select column_name, data_type, character_maximum_length
from INFORMATION_SCHEMA.COLUMNS
where table_name = '<table name>';
```
### count
- если `count(*)` дорого, то можно приблизительно
```
SELECT reltuples as approximate_row_count FROM pg_class WHERE relname = 'table_name';
(если выдало больше одной строки, то там есть нюансы https://wiki.postgresql.org/wiki/Count_estimate)
```
### dump, restore
- `pg_dump --column-inserts --data-only --host localhost --port 5432 -U user --format plain --verbose --table public.users db_name > users.sql` - this can last long; you can omit `--column-inserts` to make it faster
- `PGPASSWORD=qwerty psql -U user -d db_name -1 -h localhost -p 5432 -f users.sql` - this can last quite long

### misc
- `SELECT version()`
- [https://mydbanotebook.org/psql_tips_all.html](https://mydbanotebook.org/psql_tips_all.html)
- [https://uproger.com/postgresql-prodvinutye-komandy](https://uproger.com/postgresql-prodvinutye-komandy)
