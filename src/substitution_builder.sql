CREATE USER $ROLE WITH PASSWORD '$PASSWORD';

-- GRANT readwrite TO $ROLE;

CREATE TYPE public.loan_status_type_enum AS ENUM (
    'Active',
    'Closed',
    'Deleted'
);


ALTER TYPE public.loan_status_type_enum OWNER TO postgres;


CREATE TYPE public.loan_term_frequency_enum AS ENUM (
    'monthly',
    'bi-weekly',
    'weekly'
);


ALTER TYPE public.loan_term_frequency_enum OWNER TO postgres;


CREATE TYPE public.loan_type_enum AS ENUM (
    'Primary',
    'Home Equity',
    'Refinance'
);


ALTER TYPE public.loan_type_enum OWNER TO postgres;

--
-- Create some sequences and tables
--
CREATE SEQUENCE public.loan_loanid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.loan_loanid_seq OWNER TO postgres;

-- loan table
CREATE TABLE public.loan (
    loanid bigint DEFAULT nextval('public.loan_loanid_seq'::regclass) NOT NULL,
    holpropertyid bigint NOT NULL,
    lendercompany text,
    loantype public.loan_type_enum,
    loanamount double precision,
    loanbalance double precision,
    startdate date,
    duedate date,
    loanterm integer,
    loantermfrequency public.loan_term_frequency_enum NOT NULL DEFAULT 'monthly'::loan_term_frequency_enum,
    loaninterest double precision,
    loaninteresttype text,
    deedtype text,
    isloanrefinance boolean DEFAULT false NOT NULL,
    isloanequity boolean DEFAULT false NOT NULL,
    titlecompany text,
    loanpayment double precision,
    iscorporation boolean DEFAULT false NOT NULL,
    lastname text,
    firstname text,
    loanstatus public.loan_status_type_enum
);

ALTER TABLE public.loan OWNER TO postgres;

CREATE SEQUENCE IF NOT EXISTS public.mortgageratetypes_ratetypeid_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.mortgageratetypes_ratetypeid_seq
    OWNER TO postgres;

-- DROP SEQUENCE IF EXISTS public.mortgagerates_mortgageid_seq;

CREATE SEQUENCE IF NOT EXISTS public.mortgagerates_mortgageid_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.mortgagerates_mortgageid_seq OWNER TO postgres;

-- DROP TABLE IF EXISTS public.mortgageratetypes;

CREATE TABLE IF NOT EXISTS public.mortgageratetypes
(
    ratetypeid integer NOT NULL DEFAULT nextval('mortgageratetypes_ratetypeid_seq'::regclass),
    ratename character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT mortgageratetypes_pkey PRIMARY KEY (ratetypeid)
);

ALTER TABLE IF EXISTS public.mortgageratetypes OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.mortgagerates
(
    mortgageid integer NOT NULL DEFAULT nextval('mortgagerates_mortgageid_seq'::regclass),
    ratetypeid integer NOT NULL,
    currentrate double precision NOT NULL,
    currentratedate date NOT NULL,
    previousrate double precision NOT NULL,
    previousratedate date NOT NULL,
    precentchange double precision NOT NULL,
    datasource character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT mortgagerates_pkey PRIMARY KEY (mortgageid),
    CONSTRAINT fk_mortgageratetype FOREIGN KEY (ratetypeid)
        REFERENCES public.mortgageratetypes (ratetypeid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

ALTER TABLE IF EXISTS public.mortgagerates OWNER to postgres;
