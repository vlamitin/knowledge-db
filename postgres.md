- `psql -U <DB_USER> -d <DB_NAME> -f /file.sql` - прогнать sql скрипт
- `psql -h localhost -p 5432 -U postgres -W -d dbname` - подключиться к базе dbname на localhost:5432 под юзером postgres и prompt пароль (-W);
- [psql commands](https://www.postgresqltutorial.com/psql-commands/);
- когда в psql, то запрос вот так делать: `SELECT * FROM some_table;`
- Инфа о полях таблицы
```
select column_name, data_type, character_maximum_length
from INFORMATION_SCHEMA.COLUMNS
where table_name = '<table name>';
```
