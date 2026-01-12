-- 코드를 입력하세요
SELECT book_id, date_format(published_date,'%Y-%m-%d') as PUBLISHED_DATE
from book
where published_date BETWEEN '2021-01-01' AND '2021-12-31' 
    and category='인문' 
order by published_date asc;