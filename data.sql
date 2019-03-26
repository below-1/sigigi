-- Adminer 4.7.1 PostgreSQL dump

\connect "db_gigi";

DROP TABLE IF EXISTS "gejala";
DROP SEQUENCE IF EXISTS gejala_id_seq;
CREATE SEQUENCE gejala_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."gejala" (
    "id" integer DEFAULT nextval('gejala_id_seq') NOT NULL,
    "nama" character varying(250) NOT NULL,
    "keterangan" text,
    "deleted" boolean NOT NULL,
    CONSTRAINT "gejala_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "gejala" ("id", "nama", "keterangan", "deleted") VALUES
(1,	'demam',	'',	'0'),
(2,	'sakit gigi',	'',	'0'),
(3,	'dentin terlihat',	'',	'0'),
(4,	'Gigi berubang',	'',	'0'),
(5,	'Bau mulut tak sedap',	'',	'0'),
(6,	'infeksi jaringan pulpa',	'',	'0'),
(7,	'gigi ngilu saat terkena ransangan (panas atau dingin)',	'',	'0'),
(8,	'gigi berwarna coklat, hitam atau putih pada permukaan gigi',	'',	'0'),
(9,	'gusi nyeri',	'',	'0'),
(10,	'gusi gatal',	'',	'0'),
(11,	'gusi bengkak',	'',	'0'),
(12,	'gusi mudah berdarah',	'',	'0'),
(13,	'gusi merah terang',	'',	'0'),
(14,	'terdapat endapan plak',	'',	'0'),
(15,	'terdapat karag gigi',	'',	'0'),
(16,	'rongga terbentuk di antara gigi (nanah terbentuk)',	'',	'0'),
(17,	'nanah pada pangkal gusi',	'',	'0'),
(18,	'nyeri saat mengunyah',	'',	'0'),
(19,	'lubang sangat besarpada gigi',	'',	'0'),
(20,	'ruang pulpa terbuka',	'',	'0'),
(21,	'gigi tampak lebih kuning',	'',	'0'),
(22,	'tepi gigi menjadi tidak teratur dan kasar',	'',	'0'),
(23,	'Gigi goyang',	'',	'0');

DROP TABLE IF EXISTS "gejala_slot";
DROP SEQUENCE IF EXISTS gejala_slot_id_seq;
CREATE SEQUENCE gejala_slot_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."gejala_slot" (
    "id" integer DEFAULT nextval('gejala_slot_id_seq') NOT NULL,
    "gejala_id" integer,
    "rule_id" integer,
    "weight" double precision NOT NULL,
    "vorder" integer DEFAULT '0',
    CONSTRAINT "gejala_slot_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "gejala_slot_gejala_id_fkey" FOREIGN KEY (gejala_id) REFERENCES gejala(id) NOT DEFERRABLE,
    CONSTRAINT "gejala_slot_rule_id_fkey" FOREIGN KEY (rule_id) REFERENCES rule(id) ON DELETE CASCADE NOT DEFERRABLE
) WITH (oids = false);

INSERT INTO "gejala_slot" ("id", "gejala_id", "rule_id", "weight", "vorder") VALUES
(62,	5,	9,	0.1,	1),
(63,	9,	9,	0.2,	2),
(64,	10,	9,	0.4,	3),
(65,	11,	9,	0.1,	4),
(66,	12,	9,	0.7,	5),
(67,	13,	9,	0.5,	6),
(68,	14,	9,	0.5,	7),
(69,	15,	9,	0.6,	8),
(70,	1,	10,	0.8,	1),
(71,	2,	10,	0.4,	2),
(72,	3,	10,	0.2,	3),
(73,	4,	10,	0.9,	4),
(74,	5,	10,	0.1,	5),
(75,	6,	10,	0.5,	6),
(76,	7,	10,	0.8,	7),
(77,	8,	10,	0.2,	8),
(78,	5,	11,	0.1,	1),
(79,	9,	11,	0.2,	2),
(80,	11,	11,	0.1,	3),
(81,	12,	11,	0.7,	4),
(82,	13,	11,	0.5,	5),
(83,	14,	11,	0.5,	6),
(84,	15,	11,	0.6,	7),
(85,	16,	11,	0.1,	8),
(86,	23,	11,	0.3,	9),
(87,	1,	12,	0.6,	1),
(88,	5,	12,	0.1,	2),
(89,	11,	12,	0.1,	3),
(90,	12,	12,	0.7,	4),
(91,	13,	12,	0.5,	5),
(92,	14,	12,	0.5,	6),
(93,	15,	12,	0.6,	7),
(94,	17,	12,	0.8,	8),
(95,	18,	12,	0.7,	9),
(96,	2,	13,	0.4,	1),
(97,	4,	13,	0.9,	2),
(98,	6,	13,	0.5,	3),
(99,	12,	13,	0.7,	4),
(100,	18,	13,	0.7,	5),
(101,	19,	13,	0.4,	6),
(102,	20,	13,	0.9,	7),
(103,	2,	14,	0.4,	1),
(104,	7,	14,	0.8,	2),
(105,	21,	14,	0.6,	3),
(106,	22,	14,	0.8,	4);

DROP TABLE IF EXISTS "medic_record";
DROP SEQUENCE IF EXISTS medic_record_id_seq;
CREATE SEQUENCE medic_record_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."medic_record" (
    "id" integer DEFAULT nextval('medic_record_id_seq') NOT NULL,
    "waktu" timestamp,
    "keterangan" text,
    "user_id" integer,
    "meta" json,
    CONSTRAINT "medic_record_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "medic_record_user_id_fkey" FOREIGN KEY (user_id) REFERENCES "user"(id) NOT DEFERRABLE
) WITH (oids = false);

INSERT INTO "medic_record" ("id", "waktu", "keterangan", "user_id", "meta") VALUES
(1,	'2019-03-26 12:54:59.881625',	NULL,	3,	'{"vucr": [{"penyakit": 2, "slots": [{"id": 62, "gejala_id": 5, "weight": 0.1, "vorder": 1, "vur": 0.125, "vur_norm": 0.027777777777777776, "credit": 1.1, "credit_norm": 0.09909909909909911, "vur_baru": 0.011261261261261262, "vur_baru_norm": 0.02777777777777778}, {"id": 63, "gejala_id": 9, "weight": 0.2, "vorder": 2, "vur": 0.25, "vur_norm": 0.05555555555555555, "credit": 1.2, "credit_norm": 0.10810810810810811, "vur_baru": 0.022522522522522525, "vur_baru_norm": 0.05555555555555556}, {"id": 64, "gejala_id": 10, "weight": 0.4, "vorder": 3, "vur": 0.375, "vur_norm": 0.08333333333333333, "credit": 1.4, "credit_norm": 0.12612612612612611, "vur_baru": 0.033783783783783786, "vur_baru_norm": 0.08333333333333333}, {"id": 65, "gejala_id": 11, "weight": 0.1, "vorder": 4, "vur": 0.5, "vur_norm": 0.1111111111111111, "credit": 1.1, "credit_norm": 0.09909909909909911, "vur_baru": 0.04504504504504505, "vur_baru_norm": 0.11111111111111112}, {"id": 66, "gejala_id": 12, "weight": 0.7, "vorder": 5, "vur": 0.625, "vur_norm": 0.1388888888888889, "credit": 1.7, "credit_norm": 0.15315315315315314, "vur_baru": 0.05630630630630631, "vur_baru_norm": 0.1388888888888889}, {"id": 67, "gejala_id": 13, "weight": 0.5, "vorder": 6, "vur": 0.75, "vur_norm": 0.16666666666666666, "credit": 1.5, "credit_norm": 0.13513513513513514, "vur_baru": 0.06756756756756757, "vur_baru_norm": 0.16666666666666666}, {"id": 68, "gejala_id": 14, "weight": 0.5, "vorder": 7, "vur": 0.875, "vur_norm": 0.19444444444444445, "credit": 1.5, "credit_norm": 0.13513513513513514, "vur_baru": 0.07882882882882883, "vur_baru_norm": 0.19444444444444442}, {"id": 69, "gejala_id": 15, "weight": 0.6, "vorder": 8, "vur": 1.0, "vur_norm": 0.2222222222222222, "credit": 1.6, "credit_norm": 0.14414414414414414, "vur_baru": 0.0900900900900901, "vur_baru_norm": 0.22222222222222224}], "nurj": 0.5625, "rur": 0.0703125, "total_VUR": 4.5, "believe": 0.5624203821656051, "total_vur": 3.5, "total_vur_baru": 0.5303030303030303, "total_vur_baru_norm": 1.0, "total_credit": 6.6000000000000005, "total_credit_norm": 1.0}, {"penyakit": 1, "slots": [{"id": 70, "gejala_id": 1, "weight": 0.8, "vorder": 1, "vur": 0.125, "vur_norm": 0.024390243902439025, "credit": 1.8, "credit_norm": 0.15126050420168066, "vur_baru": 0.010504201680672268, "vur_baru_norm": 0.024390243902439025}, {"id": 71, "gejala_id": 2, "weight": 0.4, "vorder": 2, "vur": 0.25, "vur_norm": 0.04878048780487805, "credit": 1.4, "credit_norm": 0.1176470588235294, "vur_baru": 0.021008403361344536, "vur_baru_norm": 0.04878048780487805}, {"id": 72, "gejala_id": 3, "weight": 0.2, "vorder": 3, "vur": 0.375, "vur_norm": 0.07317073170731707, "credit": 1.2, "credit_norm": 0.10084033613445377, "vur_baru": 0.031512605042016806, "vur_baru_norm": 0.07317073170731708}, {"id": 73, "gejala_id": 4, "weight": 0.9, "vorder": 4, "vur": 0.5, "vur_norm": 0.0975609756097561, "credit": 1.9, "credit_norm": 0.15966386554621848, "vur_baru": 0.04201680672268907, "vur_baru_norm": 0.0975609756097561}, {"id": 74, "gejala_id": 5, "weight": 0.1, "vorder": 5, "vur": 1.25, "vur_norm": 0.24390243902439024, "credit": 1.1, "credit_norm": 0.09243697478991597, "vur_baru": 0.10504201680672269, "vur_baru_norm": 0.24390243902439027}, {"id": 75, "gejala_id": 6, "weight": 0.5, "vorder": 6, "vur": 0.75, "vur_norm": 0.14634146341463414, "credit": 1.5, "credit_norm": 0.12605042016806722, "vur_baru": 0.06302521008403361, "vur_baru_norm": 0.14634146341463417}, {"id": 76, "gejala_id": 7, "weight": 0.8, "vorder": 7, "vur": 0.875, "vur_norm": 0.17073170731707318, "credit": 1.8, "credit_norm": 0.15126050420168066, "vur_baru": 0.07352941176470588, "vur_baru_norm": 0.17073170731707318}, {"id": 77, "gejala_id": 8, "weight": 0.2, "vorder": 8, "vur": 1.0, "vur_norm": 0.1951219512195122, "credit": 1.2, "credit_norm": 0.10084033613445377, "vur_baru": 0.08403361344537814, "vur_baru_norm": 0.1951219512195122}], "nurj": 0.640625, "rur": 0.080078125, "total_VUR": 5.125, "believe": 0.7563706563706566, "total_vur": 3.5, "total_vur_baru": 0.5303030303030303, "total_vur_baru_norm": 1.0, "total_credit": 6.6000000000000005, "total_credit_norm": 1.0}, {"penyakit": 3, "slots": [{"id": 78, "gejala_id": 5, "weight": 0.1, "vorder": 1, "vur": 0.3333333333333333, "vur_norm": 0.04054054054054054, "credit": 1.1, "credit_norm": 0.09090909090909093, "vur_baru": 0.027548209366391185, "vur_baru_norm": 0.040540540540540536}, {"id": 79, "gejala_id": 9, "weight": 0.2, "vorder": 2, "vur": 0.4444444444444444, "vur_norm": 0.05405405405405406, "credit": 1.2, "credit_norm": 0.09917355371900827, "vur_baru": 0.03673094582185491, "vur_baru_norm": 0.05405405405405405}, {"id": 80, "gejala_id": 11, "weight": 0.1, "vorder": 3, "vur": 0.6666666666666666, "vur_norm": 0.08108108108108109, "credit": 1.1, "credit_norm": 0.09090909090909093, "vur_baru": 0.05509641873278237, "vur_baru_norm": 0.08108108108108107}, {"id": 81, "gejala_id": 12, "weight": 0.7, "vorder": 4, "vur": 0.8888888888888888, "vur_norm": 0.10810810810810811, "credit": 1.7, "credit_norm": 0.14049586776859505, "vur_baru": 0.07346189164370982, "vur_baru_norm": 0.1081081081081081}, {"id": 82, "gejala_id": 13, "weight": 0.5, "vorder": 5, "vur": 1.1111111111111112, "vur_norm": 0.13513513513513514, "credit": 1.5, "credit_norm": 0.12396694214876033, "vur_baru": 0.09182736455463729, "vur_baru_norm": 0.13513513513513514}, {"id": 83, "gejala_id": 14, "weight": 0.5, "vorder": 6, "vur": 1.3333333333333333, "vur_norm": 0.16216216216216217, "credit": 1.5, "credit_norm": 0.12396694214876033, "vur_baru": 0.11019283746556474, "vur_baru_norm": 0.16216216216216214}, {"id": 84, "gejala_id": 15, "weight": 0.6, "vorder": 7, "vur": 1.5555555555555556, "vur_norm": 0.1891891891891892, "credit": 1.6, "credit_norm": 0.1322314049586777, "vur_baru": 0.1285583103764922, "vur_baru_norm": 0.1891891891891892}, {"id": 85, "gejala_id": 16, "weight": 0.1, "vorder": 8, "vur": 0.8888888888888888, "vur_norm": 0.10810810810810811, "credit": 1.1, "credit_norm": 0.09090909090909093, "vur_baru": 0.07346189164370982, "vur_baru_norm": 0.1081081081081081}, {"id": 86, "gejala_id": 23, "weight": 0.3, "vorder": 9, "vur": 1.0, "vur_norm": 0.12162162162162163, "credit": 1.3, "credit_norm": 0.10743801652892562, "vur_baru": 0.08264462809917356, "vur_baru_norm": 0.12162162162162161}], "nurj": 0.9135802469135802, "rur": 0.10150891632373113, "total_VUR": 8.222222222222221, "believe": 0.5609271523178808, "total_vur": 3.5, "total_vur_baru": 0.5303030303030303, "total_vur_baru_norm": 1.0, "total_credit": 6.6000000000000005, "total_credit_norm": 1.0}, {"penyakit": 4, "slots": [{"id": 87, "gejala_id": 1, "weight": 0.6, "vorder": 1, "vur": 0.2222222222222222, "vur_norm": 0.019607843137254898, "credit": 1.6, "credit_norm": 0.11764705882352942, "vur_baru": 0.016339869281045753, "vur_baru_norm": 0.0196078431372549}, {"id": 88, "gejala_id": 5, "weight": 0.1, "vorder": 2, "vur": 0.8888888888888888, "vur_norm": 0.07843137254901959, "credit": 1.1, "credit_norm": 0.08088235294117647, "vur_baru": 0.06535947712418301, "vur_baru_norm": 0.0784313725490196}, {"id": 89, "gejala_id": 11, "weight": 0.1, "vorder": 3, "vur": 1.0, "vur_norm": 0.08823529411764705, "credit": 1.1, "credit_norm": 0.08088235294117647, "vur_baru": 0.07352941176470588, "vur_baru_norm": 0.08823529411764706}, {"id": 90, "gejala_id": 12, "weight": 0.7, "vorder": 4, "vur": 1.3333333333333333, "vur_norm": 0.1176470588235294, "credit": 1.7, "credit_norm": 0.125, "vur_baru": 0.09803921568627451, "vur_baru_norm": 0.11764705882352941}, {"id": 91, "gejala_id": 13, "weight": 0.5, "vorder": 5, "vur": 1.6666666666666667, "vur_norm": 0.14705882352941177, "credit": 1.5, "credit_norm": 0.11029411764705882, "vur_baru": 0.12254901960784315, "vur_baru_norm": 0.14705882352941177}, {"id": 92, "gejala_id": 14, "weight": 0.5, "vorder": 6, "vur": 2.0, "vur_norm": 0.1764705882352941, "credit": 1.5, "credit_norm": 0.11029411764705882, "vur_baru": 0.14705882352941177, "vur_baru_norm": 0.17647058823529413}, {"id": 93, "gejala_id": 15, "weight": 0.6, "vorder": 7, "vur": 2.3333333333333335, "vur_norm": 0.20588235294117646, "credit": 1.6, "credit_norm": 0.11764705882352942, "vur_baru": 0.17156862745098042, "vur_baru_norm": 0.2058823529411765}, {"id": 94, "gejala_id": 17, "weight": 0.8, "vorder": 8, "vur": 0.8888888888888888, "vur_norm": 0.07843137254901959, "credit": 1.8, "credit_norm": 0.1323529411764706, "vur_baru": 0.06535947712418301, "vur_baru_norm": 0.0784313725490196}, {"id": 95, "gejala_id": 18, "weight": 0.7, "vorder": 9, "vur": 1.0, "vur_norm": 0.08823529411764705, "credit": 1.7, "credit_norm": 0.125, "vur_baru": 0.07352941176470588, "vur_baru_norm": 0.08823529411764706}], "nurj": 1.2592592592592593, "rur": 0.13991769547325103, "total_VUR": 11.333333333333334, "believe": 0.658041958041958, "total_vur": 3.5, "total_vur_baru": 0.5303030303030303, "total_vur_baru_norm": 1.0, "total_credit": 6.6000000000000005, "total_credit_norm": 1.0}, {"penyakit": 5, "slots": [{"id": 96, "gejala_id": 2, "weight": 0.4, "vorder": 1, "vur": 0.2857142857142857, "vur_norm": 0.0392156862745098, "credit": 1.4, "credit_norm": 0.1217391304347826, "vur_baru": 0.024844720496894408, "vur_baru_norm": 0.039215686274509796}, {"id": 97, "gejala_id": 4, "weight": 0.9, "vorder": 2, "vur": 0.5714285714285714, "vur_norm": 0.0784313725490196, "credit": 1.9, "credit_norm": 0.16521739130434782, "vur_baru": 0.049689440993788817, "vur_baru_norm": 0.07843137254901959}, {"id": 98, "gejala_id": 6, "weight": 0.5, "vorder": 3, "vur": 0.8571428571428571, "vur_norm": 0.11764705882352941, "credit": 1.5, "credit_norm": 0.13043478260869565, "vur_baru": 0.07453416149068323, "vur_baru_norm": 0.1176470588235294}, {"id": 99, "gejala_id": 12, "weight": 0.7, "vorder": 4, "vur": 2.2857142857142856, "vur_norm": 0.3137254901960784, "credit": 1.7, "credit_norm": 0.14782608695652175, "vur_baru": 0.19875776397515527, "vur_baru_norm": 0.31372549019607837}, {"id": 100, "gejala_id": 18, "weight": 0.7, "vorder": 5, "vur": 1.4285714285714286, "vur_norm": 0.19607843137254902, "credit": 1.7, "credit_norm": 0.14782608695652175, "vur_baru": 0.12422360248447205, "vur_baru_norm": 0.196078431372549}, {"id": 101, "gejala_id": 19, "weight": 0.4, "vorder": 6, "vur": 0.8571428571428571, "vur_norm": 0.11764705882352941, "credit": 1.4, "credit_norm": 0.1217391304347826, "vur_baru": 0.07453416149068323, "vur_baru_norm": 0.1176470588235294}, {"id": 102, "gejala_id": 20, "weight": 0.9, "vorder": 7, "vur": 1.0, "vur_norm": 0.13725490196078433, "credit": 1.9, "credit_norm": 0.16521739130434782, "vur_baru": 0.08695652173913043, "vur_baru_norm": 0.1372549019607843}], "nurj": 1.0408163265306123, "rur": 0.14868804664723032, "total_VUR": 7.285714285714286, "believe": 0.7561514195583595, "total_vur": 3.5, "total_vur_baru": 0.5303030303030303, "total_vur_baru_norm": 1.0, "total_credit": 6.6000000000000005, "total_credit_norm": 1.0}, {"penyakit": 6, "slots": [{"id": 103, "gejala_id": 2, "weight": 0.4, "vorder": 1, "vur": 0.75, "vur_norm": 0.21428571428571427, "credit": 1.4, "credit_norm": 0.2121212121212121, "vur_baru": 0.11363636363636363, "vur_baru_norm": 0.2142857142857143}, {"id": 104, "gejala_id": 7, "weight": 0.8, "vorder": 2, "vur": 1.0, "vur_norm": 0.2857142857142857, "credit": 1.8, "credit_norm": 0.2727272727272727, "vur_baru": 0.1515151515151515, "vur_baru_norm": 0.2857142857142857}, {"id": 105, "gejala_id": 21, "weight": 0.6, "vorder": 3, "vur": 0.75, "vur_norm": 0.21428571428571427, "credit": 1.6, "credit_norm": 0.24242424242424243, "vur_baru": 0.11363636363636363, "vur_baru_norm": 0.2142857142857143}, {"id": 106, "gejala_id": 22, "weight": 0.8, "vorder": 4, "vur": 1.0, "vur_norm": 0.2857142857142857, "credit": 1.8, "credit_norm": 0.2727272727272727, "vur_baru": 0.1515151515151515, "vur_baru_norm": 0.2857142857142857}], "nurj": 0.875, "rur": 0.21875, "total_VUR": 3.5, "believe": 0.7244444444444444, "total_vur": 3.5, "total_vur_baru": 0.5303030303030303, "total_vur_baru_norm": 1.0, "total_credit": 6.6000000000000005, "total_credit_norm": 1.0}]}');

DROP TABLE IF EXISTS "penyakit";
DROP SEQUENCE IF EXISTS penyakit_id_seq;
CREATE SEQUENCE penyakit_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."penyakit" (
    "id" integer DEFAULT nextval('penyakit_id_seq') NOT NULL,
    "nama" character varying(250) NOT NULL,
    "keterangan" text,
    "deleted" boolean NOT NULL,
    CONSTRAINT "penyakit_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "penyakit" ("id", "nama", "keterangan", "deleted") VALUES
(1,	'karies gigi',	'karies gigi adalah kondisi saat muncul lubang pada gigi yang disebabkan oleh bakteri. kondisi ini dapat menyebabkan sakit gigi parah, infeksi dan lepasnya gigi',	'0'),
(2,	'gingivitis',	'gingivitis adalah salah satu jenis penyakit gusi yang menyebabkan iritasi, kemerahan dan pembengkakan pada gusi',	'0'),
(3,	'periodontitis',	'periodontitis adalah infeksi gusi yang serius yang merusak jaringan lunak dan tulang yang menyokong gigi',	'0'),
(4,	'abses',	'abses adalah penyakit dimana nanah yang menumpuk digigi akibat infeksi',	'0'),
(5,	'pupitis',	'pulitis adalah peradangan yang terjadi pada pulpa. pulpa merupakan jaringan yang lunak yang terbentuk dari urat dan pembuluh darah yang diselimuti oleh struktur gigi',	'0'),
(6,	'erosi gigi',	'erosi gigi adalah terkikisnya elemen gigi yang disebabkan oleh asam. elemen adalah lapisan keras pelindung gigi',	'0');

DROP TABLE IF EXISTS "rule";
DROP SEQUENCE IF EXISTS rule_id_seq;
CREATE SEQUENCE rule_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."rule" (
    "id" integer DEFAULT nextval('rule_id_seq') NOT NULL,
    "penyakit_id" integer,
    CONSTRAINT "rule_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "rule_penyakit_id_fkey" FOREIGN KEY (penyakit_id) REFERENCES penyakit(id) NOT DEFERRABLE
) WITH (oids = false);

INSERT INTO "rule" ("id", "penyakit_id") VALUES
(9,	2),
(10,	1),
(11,	3),
(12,	4),
(13,	5),
(14,	6);

DROP TABLE IF EXISTS "user";
DROP SEQUENCE IF EXISTS user_id_seq;
CREATE SEQUENCE user_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."user" (
    "id" integer DEFAULT nextval('user_id_seq') NOT NULL,
    "username" character varying(250),
    "nama" character varying(250),
    "password" character varying(250),
    "role" character varying(250),
    CONSTRAINT "user_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "user" ("id", "username", "nama", "password", "role") VALUES
(1,	'admin',	NULL,	'pbkdf2:sha256:50000$X6YO8c0d$f0735fad9f50b7abedc2a826fff84bcb19e848ddc52d189a4a98e3fc6e47efd8',	'admin'),
(2,	'admin',	NULL,	'pbkdf2:sha256:50000$8lDCNMk8$70fdc37b8ba93052d5033019e38919357d3affa6fbdf7bfa31cdf6f01b9d072e',	'admin'),
(3,	'user',	NULL,	'pbkdf2:sha256:50000$1S80Kgy6$1d85ce556079137f459c84847cf53fa80c228408a3f3a3d62440206940d334ae',	'user'),
(7,	'Yesto',	'Yesto',	NULL,	'user');

-- 2019-03-26 05:11:37.920845+00
