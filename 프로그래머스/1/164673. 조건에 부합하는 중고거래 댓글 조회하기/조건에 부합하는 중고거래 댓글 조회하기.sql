-- 코드를 입력하세요
SELECT b.title,B.board_id,r.reply_id,r.writer_id,r.contents,date_format(R.created_date,'%Y-%m-%d') as CREATED_DATE
from used_goods_board b
join used_goods_reply r
on b.board_id = r.board_id
where b.created_date between'2022-10-01' and '2022-10-31'
order by r.created_date asc, b.title asc; 
