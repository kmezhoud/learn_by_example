CREATE TABLE customer (
	cid integer PRIMARY KEY AUTOINCREMENT,
	cname varchar,
	cmail varchar,
	cmobile integer,
	caddress varchar,
	cpassword varchar
);

CREATE TABLE restadmin (
	rid integer PRIMARY KEY AUTOINCREMENT,
	rname varchar,	
	rmail varchar,
	rmobile integer,
	raddress varchar,
	rpassword varchar
);

CREATE TABLE diginadmin (
	amail varchar,
	apassword varchar
);

CREATE TABLE items (
	iid integer,
	iname varchar,
	iprice integer,
	rid integer
);

CREATE TABLE orders (
	oid integer,
	cid integer,
	rid integer,
	iid integer,
	ostatus text
);

