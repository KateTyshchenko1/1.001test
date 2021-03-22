select AUTHOR_NAME, COUNT(DISTINCT BOOK_NAME) from BOOK_AUTHOR_PUBLISHER_RELATIONSHIP as R
left join books as B
on r.BOOK_ID = B.BOOK_ID
left join authors as A
on r.AUTHOR_ID = A.AUTHOR_ID
GROUP BY AUTHOR_NAME

select B.BOOK_NAME, COUNT(DISTINCT AUTHOR_NAME) from BOOK_AUTHOR_PUBLISHER_RELATIONSHIP as R
left join books as B
on r.BOOK_ID = B.BOOK_ID
left join authors as A
on r.AUTHOR_ID = A.AUTHOR_ID
GROUP BY BOOK_NAME

select AUTHOR_NAME, sum(ROYALTY_AMNT) AS TOTAL_ROYALTY from BOOK_AUTHOR_PUBLISHER_RELATIONSHIP as R
left join books as B
on r.BOOK_ID = B.BOOK_ID
left join authors as A
on r.AUTHOR_ID = A.AUTHOR_ID
GROUP BY AUTHOR_NAME

select AUTHOR_NAME, BOOK_NAME, sum(ROYALTY_AMNT) AS TOTAL_ROYALTY from BOOK_AUTHOR_PUBLISHER_RELATIONSHIP as R
left join books as B
on r.BOOK_ID = B.BOOK_ID
left join authors as A
on r.AUTHOR_ID = A.AUTHOR_ID
GROUP BY AUTHOR_NAME

select PUBLISHER_NAME, count(distinct BOOK_NAME) from BOOK_AUTHOR_PUBLISHER_RELATIONSHIP as R
left join books as B
on r.BOOK_ID = B.BOOK_ID
left join authors as A
on r.AUTHOR_ID = A.AUTHOR_ID
left join publishers as P
on P.Publisher_Id = R.Publisher_Id
GROUP BY AUTHOR_NAME


select EDITOR_NAME, count(distinct BOOK_NAME) from BOOK_EDITOR_RELATIONSHIP as E
left join books as B
on E.BOOK_ID = B.BOOK_ID
left join editors as ED
on ED.EDITOR_ID = E.EDITOR_ID
GROUP BY EDITOR_NAME


select BOOK_NAME, count(distinct EDITOR_NAME) as 'number of editors 'from BOOK_EDITOR_RELATIONSHIP as E
left join books as B
on E.BOOK_ID = B.BOOK_ID
left join editors as ED
on ED.EDITOR_ID = E.EDITOR_ID
GROUP BY BOOK_NAME

select ORDER_ID , sum(Quantity_SOLD) as 'books in order' from sales
group by ORDER_ID

select b.BOOK_NAME , sum(Quantity_SOLD) as 'sales per book' from sales as S
left join books as b
on b.BOOK_ID = s.BOOK_ID
group by BOOK_NAME

select CUSTOMER_NAME, ORDER_ID from customers as c
left join sales as s
on c.CUSTOMER_ID = s.CUSTOMER_ID

select CUSTOMER_NAME, count(ORDER_ID) as 'Orders per customer' from customers as c
left join sales as s
on c.CUSTOMER_ID = s.CUSTOMER_ID
group by CUSTOMER_NAME