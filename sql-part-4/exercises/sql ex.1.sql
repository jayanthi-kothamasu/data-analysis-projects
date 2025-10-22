1.
/*
select top 1000 *
from booksdb.dbo.books
*/
2.
/*
select count(title)
from booksdb.dbo.books
*/

3.
/*
select count(book_id)
from booksdb.dbo.books
where original_publication_year <1800
*/

4.
/*
select distinct(authors)
from booksdb.dbo.books
*/

5.
/*
select count(book_id) 
from booksdb.dbo.books
where (language_code like 'eng%' or language_code like 'en-%')
*/

6.
/*
select COUNT(original_title)
from BooksDB.dbo.books
where original_publication_year BETWEEN 1914 and 1921
*/

7.
/*
select top 1000 *
from BooksDB.dbo.book_tags
ORDER BY tag_id
*/

8.
/*
select count(goodreads_book_id),tag_id
from BooksDB.dbo.book_tags
GROUP BY tag_id
*/

9./*
select count(goodreads_book_id) as count_goodreads_book_id,tag_id
from BooksDB.dbo.book_tags
GROUP BY tag_id
*/
10.
/*
SELECT top 1000 *
from BooksDB.dbo.ratings
ORDER BY rating desc
*/
11.
/*
select count(user_id)
from BooksDB.dbo.ratings
where rating<2
*/
12.
/*
select count(book_id)
from BooksDB.dbo.ratings
where rating >= 4
*/
13.
/*
select tag_name
from booksdb.dbo.tags
where tag_name like '%mystery%'
*/
14.
/*
 SELECT *
 FROM BooksDB.dbo.tags
WHERE tag_name < 'd' AND tag_name >= 'c';
*/
16./*
select count(book_id) as "Total Books To Read ", user_id
from BooksDB.dbo.to_read
GROUP BY [user_id]
ORDER BY [user_id]
*/

17.
/*
select count(book_id) as "Total Books To Read ", user_id
from BooksDB.dbo.to_read
GROUP BY [user_id]
ORDER BY count(book_id) DESC
*/



