-- select cr.r_name as region1, sr.r_name as region2, coalesce(round(sum(l_extendedprice * (1 - l_discount)*(1-l_tax))), 0) as revenue
-- from region as cr cross join region as sr
-- left join nation as cn on cr.r_regionkey = cn.n_regionkey
-- left join nation as sn on sr.r_regionkey = sn.n_regionkey
-- left join (
--     supplier as s
--     join lineitem as l on s.s_suppkey = l.l_suppkey
--     join orders as o on l.l_orderkey = o.o_orderkey
--     join customer as c on o.o_custkey = c.c_custkey
-- ) on s.s_nationkey = sn.n_nationkey and c.c_nationkey = cn.n_nationkey
-- group by region1, region2
-- order by revenue desc, region1 asc, region2 asc;
select n_name, max(c_acctbal) as max_acctbal, min(c_acctbal) as min_acctbal
from nation join customer on n_nationkey = c_nationkey 
group by n_name
order by n_name asc;