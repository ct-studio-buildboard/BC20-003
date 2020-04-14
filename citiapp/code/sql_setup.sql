--creating company table
insert into corporates
select NULL,
		company_name,
		company_region,
		company_country,
		company_industry
from interactions_raw
where event_type in ('Non Deal Roadshow', 'Reverse Roadshow')
	and company_name is not null
group by 1, 2, 3, 4;

--add corporate_id to interactions table
create table interactions_raw_revised as
	select a.*,
			b.corporate_id
	from interactions_raw a
		left join corporates b on (a.company_name = b.company_name)
								and (a.company_region = b.company_region)
								and (a.company_country = b.company_country)
								and (a.company_industry = b.company_industry);

create table interactions_roadshow as
	select *
	from interactions_raw
	where event_type in ('Non Deal Roadshow', 'Reverse Roadshow');

create table company_roadshow_revised as
	select a.corporate_id,
			b.*
	from corporates a
		inner join roadshow_company b on (a.company_name = b.company_name)
										and (a.company_region = b.company_region);

