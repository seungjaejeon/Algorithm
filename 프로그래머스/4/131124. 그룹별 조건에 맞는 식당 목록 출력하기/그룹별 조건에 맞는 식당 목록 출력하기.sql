with best_member as (
    select member_id
    from rest_review
    group by member_id
    order by count(*) desc
    limit 1
)


select member_name, review_text, date_format(review_date, '%Y-%m-%d') as review_date
from member_profile inner join rest_review using(member_id) inner join best_member using(member_id)
order by review_date asc, review_text asc