import gzip
import sqlite3
con=sqlite3.connect("openlibrary_search.db")
with con:
    con.execute("create table if not exists works(type,olid,edition_num,last_edit,json_data)")
    with gzip.open("../ol_dump_2021-05-13/ol_dump_works_2021-05-13.txt.gz","rt") as f:
        for i,row in enumerate(f):
            book=row.split("\t")
            query=f"insert into works values ({'?,'*(len(book)-1)}?)"
            con.execute(query,book)
            print(i)

