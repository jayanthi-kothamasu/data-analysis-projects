
1.

SELECT a.title,a.authors
FROM booksdb.dbo.books as a
WHERE authors = (SELECT a.authors WHERE authors LIKE '%,%')


2.

SELECT title
FROM BooksDB.dbo.books AS b
WHERE book_id IN(
    SELECT goodreads_book_id
    FROM BooksDB.dbo.book_tags AS bt
    WHERE tag_id In(

        SELECT tag_id 
        FROM BooksDB.dbo.tags AS t
        WHERE tag_name LIKE '%meditation%'
    )
)


3.

SELECT title, original_title, average_rating
FROM BooksDB.dbo.books
WHERE title = original_title
INTERSECT
SELECT title, original_title, average_rating
FROM BooksDB.dbo.books
WHERE average_rating >= '4.2'
ORDER BY average_rating DESC


4.

SELECT  b.original_publication_year, b.title, b.average_rating,

(
    SELECT AVG(rating)
    FROM BooksDB.dbo.ratings r
    where r.book_id = b.book_id
) as readers_avg_rating  
FROM booksdb.dbo.books b
WHERE (SELECT AVG(rating)
    FROM BooksDB.dbo.ratings r
    where r.book_id = b.book_id) > b.average_rating
ORDER BY original_publication_year, title


select b.title, b.original_publication_year, b.average_rating,

(
     SELECT avg(rating)
     from booksdb.dbo.ratings r
      where r.book_id = b.book_id
) as readers_avg_reading
from booksdb.dbo.books b
where (  b.average_rating < (select avg(rating)
        from booksdb.dbo.ratings as r
        where r.book_id = b.book_id
) 
)
ORDER BY original_publication_year,title

    
    
    
    
    from booksdb.dbo.books as b

