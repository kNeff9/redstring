--
-- PostgreSQL database dump
--

\restrict AnQTxCVrysao7JAGmpPvck1LltZN2Ovs1U2Dp40NuGYoQkye6faBtTdEQgDdaiF

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: vector; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS vector WITH SCHEMA public;


--
-- Name: EXTENSION vector; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION vector IS 'vector data type and ivfflat and hnsw access methods';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: seen_urls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.seen_urls (
    url text NOT NULL,
    added_at timestamp without time zone DEFAULT now()
);


ALTER TABLE public.seen_urls OWNER TO postgres;

--
-- Name: stories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stories (
    id uuid NOT NULL,
    timeline_id uuid,
    content text,
    centroid public.vector(768),
    date timestamp without time zone DEFAULT now()
);


ALTER TABLE public.stories OWNER TO postgres;

--
-- Name: timelines; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.timelines (
    id uuid NOT NULL,
    title text NOT NULL,
    centroid public.vector(768)
);


ALTER TABLE public.timelines OWNER TO postgres;

--
-- Name: seen_urls seen_urls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.seen_urls
    ADD CONSTRAINT seen_urls_pkey PRIMARY KEY (url);


--
-- Name: stories stories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stories
    ADD CONSTRAINT stories_pkey PRIMARY KEY (id);


--
-- Name: timelines timelines_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.timelines
    ADD CONSTRAINT timelines_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict AnQTxCVrysao7JAGmpPvck1LltZN2Ovs1U2Dp40NuGYoQkye6faBtTdEQgDdaiF

