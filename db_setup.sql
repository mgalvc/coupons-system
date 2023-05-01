-- public.coupon definition

-- Drop table

-- DROP TABLE public.coupon;

CREATE TABLE public.coupon (
	id serial4 NOT NULL,
	code varchar NOT NULL,
	expires_at timestamp NOT NULL,
	max_usage int4 NOT NULL,
	min_purchase float8 NOT NULL,
	discount_type varchar NOT NULL,
	discount_value float8 NOT NULL,
	created_at timestamp NOT NULL,
	CONSTRAINT coupon_code_key UNIQUE (code),
	CONSTRAINT coupon_pkey PRIMARY KEY (id)
);

-- public.burned_coupon definition

-- Drop table

-- DROP TABLE public.burned_coupon;

CREATE TABLE public.burned_coupon (
	id serial4 NOT NULL,
	coupon_id int4 NOT NULL,
	created_at timestamp NOT NULL,
	CONSTRAINT burned_coupon_pkey PRIMARY KEY (id)
);


-- public.burned_coupon foreign keys

ALTER TABLE public.burned_coupon ADD CONSTRAINT burned_coupon_coupon_id_fkey FOREIGN KEY (coupon_id) REFERENCES public.coupon(id);