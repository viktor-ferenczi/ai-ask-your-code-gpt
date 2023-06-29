from typing import Optional, Any

from asyncpg import Connection


async def read(conn: Connection, name: str, *, for_update: bool = False) -> Optional[Any]:
    row = await conn.fetchrow(f'''
        SELECT text, number 
        FROM property 
        WHERE name = $1
        {'FOR UPDATE' if for_update else ''}                    
    ''', name)

    if row is None:
        return None

    number = row['number']
    if number is not None:
        return number

    return row['text']


async def write(conn: Connection, name: str, value: Any):
    if isinstance(value, str):
        await conn.execute('''
            UPDATE property 
            SET text = $2, number = NULL
            WHERE name = $1                  
        ''', name, value)

    elif isinstance(value, int):
        await conn.execute('''
            UPDATE property 
            SET text = NULL, number = $2
            WHERE name = $1                  
        ''', name, value)

    else:
        raise ValueError(f'Invalid value {value!r} for property {name!r}')
