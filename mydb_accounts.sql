CREATE TABLE `Account` (
  sid INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  ID VARCHAR(45) NOT NULL UNIQUE,
  password VARCHAR(45) NOT NULL,
  gender VARCHAR(45) NOT NULL,
  birth DATE NOT NULL,
  email VARCHAR(45) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

LOCK TABLES `Account` WRITE;
INSERT INTO `Account` (name, ID, password, gender, birth, email)
VALUES 
('강민호','minho_kang58','minho_0818','여','1985-8-18','sam_ho8508@gmail.com'),
('고영표','youngpyo_ko19','youngpyo_0916','남','1991-9-16','kt_pyo3109@naver.com'),
('고우석','wooseok_ko88','wooseok_0806','남','1998-8-6','lg_seok9808@naver.com'),
('구본혁','bonhyuk_koo71','bonhyuk_0111','남','1997-1-11','lg_hyuk9701@naver.com'),
('구자욱','jawook_koo32','jawook_0212','남','1993-2-12','sam_wook9302@gmail.com'),
('구창모','changmo_koo72','changmo_0217','남','1997-2-17','lg_koo9702@naver.com'),
('권희동','huidong_kwon012','huidong_1230','여','1990-12-30','nc_dong9012@gmail.com'),
('김강률','gangryul_kim88','gangryul_0828','여','1988-8-28','doo_ryul8808@gmail.com'),
('김대우','daewoo_kim47','daewoo_0726','남','1984-7-26','lot_woo8407@naver.com'),
('김동엽','dongyub_kim07','dongyub_0724','남','1990-7-24','sam_yub9007@hanmail.net'),
('김민성','minseong_kim812','minseong_1217','남','1988-12-17','lg_seong@naver.com'),
('김상수','sangsu_kim03','sangsu_0323','여','1990-3-23','sam_su9003@naver.com'),
('김성현','sunghyun_kim73','sunghyun_0309','남','1987-3-9','ssg_hyun8703@gmail.com'),
('김원중','wonjung_kim36','wonjung_0614','남','1993-6-14','lot_jung9306@naver.com'),
('김진욱','jinuk_kim27','jinuk_0705','여','2002-7-5','lot_uk0207@gmail.com'),
('김현수','hyunsoo_kim81','hyunsoo_0112','여','1988-1-12','lg_soo8801@hanmail.net'),
('나성범','sungbum_na910','sungbum_1003','남','1989-10-3','nc_bum8910@gmail.com'),
('나승엽','seungyup_na22','seungyup_0215','남','2002-2-15','lot_yeop0202@hanmail.net'),
('노수광','sookwang_ro08','sookwang_0806','남','1990-8-6','han_kwang9008@hanmail.net'),
('노시환','sihwan_roh012','sihwan_1203','남','2000-12-3','han_hwan0012@gmail.com'),
('노진혁','jinhyuk_no97','jinhyuk_0715','남','1989-7-15','nc_hyuk8907@naver.com'),
('박건우','kunwoo_park09','kunwoo_0908','여','1990-9-8','doo_woo9009@hanmail.net'),
('박민우','minwoo_park32','minwoo_0206','여','1993-2-6','nc_woo9302@gmail.com'),
('박석민','sokmin_park56','sokmin_0626','여','1985-6-22','nc_min8506@hanmail.net'),
('박세혁','seihyok_park01','seihyok_0109','남','1990-1-9','doo_hyok9010@hanmail.net'),
('박치국','chihuk_park83','chihuk_0310','남','1998-3-10','doo_guk9803@gmail.com'),
('박해민','haemin_park02','haemin_0224','남','1990-2-24','sam_min9002@hanmail.net'),
('서건창','geonchang_seo98','geonchang_0822','남','1989-8-22','lg_chang@gmail.com'),
('서준원','junwon_seo011','junwon_1105','남','2000-11-5','lot_won0011@naver.com'),
('송명기','myunggi_song08','myunggi_0809','여','2000-8-9','nc_gi0008@gmail.com'),
('신정락','jungrak_shin75','jungrak_0513','남','1987-5-13','han_rak8705@gmail.com'),
('안치홍','chihong_an07','chihong_0702','남','1990-7-2','lot_hong9007@gmail.com'),
('양의지','euiji_yang76','euij_0605','암','1987-6-5','nc_ji8706@gmail.com'),
('오재일','jaeil_oh610','jaeil_1029','여','1986-10-29','sam_il8610@naver.com'),
('오지환','jihwan_oh03','jihwan','남','1990-3-12','lg_hwan@naver.com'),
('원종현','jonghyun_won77','jonghyun_0731','남','1987-7-31','nc_hyun8707@hanmail.net'),
('원태인','taein_won04','taein_0406','남','2000-4-6','sam_in0004@gmail.com'),
('유강남','kangnam_yoo27','kangnam_0715','남','1992-7-15','lg_nam9207@gmail.com'),
('유희관','heekwan_yoo66','heekwan_0601','남','1986-6-1','doo_kwan8606@naver.com'),
('이대호','daeho_lee26','daeho_0621','남','1982-6-21','lot_ho8206naver.com'),
('이승호','seungho_lee92','seungho_0208','남','1999-2-8','ki_ho9902@hanmail.net'),
('이영하','youngha_lee711','youngha_1101','남','1997-11-1','doo_ha9711@naver.com'),
('이용찬','yongchan_lee91','wongchan_0102','여','1989-1-2','nc_chan8901@naver.com'),
('이준영','junyoung_lee28','junyoung_0810','여','1992-8-10','kia_young9208@naver.com'),
('이천웅','chunwoong_lee810','chunwoong_1020','암','1988-10-20','lg_woong8810@gmail.com'),
('이형종','hyungjong_lee96','hyungjong_0607','남','1989-6-7','lg_jong8906@naver.com'),
('임준섭','junseob_lim97','junseob_0716','남','1989-7-16','han_seob8907@gmail.com'),
('임찬규','chankyu_im211','chankyu_1120','여','1992-11-20','lg_kyu9211@gmail.com'),
('장민재','minje_jang03','minje_0319','남','1990-3-19','han_je9003@gmail.com'),
('장시환','sihwan_jang711','sihwan_1101','남','1987-11-1','han_hwan8711@gmail.com'),
('장원준','wonjun_jang57','wonjun_0731','여','1985-7-31','doo_jun8507@hanmail.net'),
('정보근','bokeun_jeong98','bokeun_0831','남','1999-8-31','lot_keun9908@gmail.com'),
('정수빈','soobin_jeong010','soobin_1007','남','1990-10-7','doo_bin9010@naver.com'),
('정우람','wooram_jeong56','wooram_0601','남','1985-6-1','han_ram8506@naver.com'),
('정우영','wooyoung_jung98','wooyoung_0819','남','1999-8-19','lg_young9908@gmail.com'),
('정은원','eunwon_jung01','eunwon_0117','여','2000-1-17','han_won0001@naver.com'),
('정훈','hoon_jeong77','hoon_0718','여','1987-7-18','lot_hoon8707@gmail.com'),
('조상우','sangwoo_cho49','sangwoo_0904','여','1994-9-4','ki_woo9409@naver.com'),
('진해수','haesoo_jin66','haesoo_0626','남','1986-6-26','lg_soo8606@naver.com'),
('차우찬','woochan_cha75','woochan_0531','남','1987-5-31','lg_chan8705@gmail.com'),
('채은성','eunseong_chae01','eunseong_0106','여','1990-1-6','lg_seong9001@hanmail.net'),
('최원준','wonjun_choi412','wonjun_1221','여','1994-12-21','doo_joon9412@hanmail.net'),
('최재훈','jaehun_choi98','jaehun_0827','여','1989-8-27','han_hun8908@gmail.com'),
('최정','jeong_choi72','jeong_0208','남','1987-2-28','ssg_jeong8702@hanmail.net'),
('하주석','jooseok_ha42','jooseok_0225','여','1994-2-25','han_suk9402@naver.com'),
('한유섬','yooseom_han98','yooseom_0809','남','1989-8-9','ssg_seom8908@gmail.com'),
('함덕주','deokju_ham51','deokju_0113','여','1995-1-13','lg_ju9501@hanmail.com'),
('허경민','kyongmin_hur08','kyongmin_0826','여','1990-8-26','doo_min9008@gmail.com'),
('홍건희','keonhee_hong29','keonhee_0929','여','1992-9-29','doo_hee9209@gmail.com'),
('홍창기','changki_hong311','changki_1121','여','1993-11-21','lg_ki9311@hanmail.net');
UNLOCK TABLES;



DROP TABLE IF EXISTS `preference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `preference` (
  `id` varchar(45) NOT NULL,
  `preference1` varchar(45) DEFAULT NULL,
  `preference2` varchar(45) DEFAULT NULL,
  `preference3` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cat1_idx` (`preference1`),
  KEY `cat2_idx` (`preference2`),
  KEY `cat3_idx` (`preference3`),
  CONSTRAINT `cat1` FOREIGN KEY (`preference1`) REFERENCES `category` (`idcategory`),
  CONSTRAINT `cat2` FOREIGN KEY (`preference2`) REFERENCES `category` (`idcategory`),
  CONSTRAINT `cat3` FOREIGN KEY (`preference3`) REFERENCES `category` (`idcategory`),
  CONSTRAINT `user_id` FOREIGN KEY (`id`) REFERENCES `accounts` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;
--
-- Dumping data for table `preference`
--

LOCK TABLES `preference` WRITE;
/*!40000 ALTER TABLE `preference` DISABLE KEYS */;
INSERT INTO `preference` VALUES ('bokeun_jeong98','드라마','상품리뷰','국내여행'),('bonhyuk_koo71','애완/반려동물','스포츠','IT/컴퓨터'),('changki_hong311','스타/연예인','상품리뷰','국내여행'),('changmo_koo72','공연/전시','세계여행','비즈니스/경제'),('chankyu_im211','방송','요리/레시피','세계여행'),('chihong_an07','좋은글/이미지','비즈니스/경제','어학/외국어'),('chihuk_park83','일상/생각','사회/정치','건강/의학'),('chunwoong_lee810','공연/전시','만화/애니','교육/학문'),('daeho_lee26','원예/재배','세계여행','비즈니스/경제'),('daewoo_kim47','영화','일상/생각','국내여행'),('deokju_ham51','스포츠','IT/컴퓨터','어학/외국어'),('dongyub_kim07','드라마','스타/연예인','게임'),('euiji_yang76','좋은글/이미지','상품리뷰','취미'),('eunseong_chae01','인테리어/DIY','원예/재배','국내여행'),('eunwon_jung01','문학/책','패션/미용','사회/정치'),('gangryul_kim88','미술/디자인','육아/결혼','비즈니스/경제'),('geonchang_seo98','미술/디자인','원예/재배','스포츠'),('haemin_park02','드라마','방송','맛집'),('haesoo_jin66','인테리어/DIY','세계여행','교육/학문'),('heekwan_yoo66','문학/책','요리/레시피','게임'),('hoon_jeong77','애완/반려동물','원예/재배','스포츠'),('huidong_kwon012','미술/디자인','일상/생각','비즈니스/경제'),('hyungjong_lee96','음악','요리/레시피','건강/의학'),('hyunsoo_kim81','게임','맛집','건강/의학'),('jaehun_choi98','미술/디자인','애완/반려동물','교육/학문'),('jaeil_oh610','요리/레시피','스포츠','세계여행'),('jawook_koo32','영화','좋은글/이미지','원예/재배'),('jeong_choi72','문학/책','사진','국내여행'),('jihwan_oh03','미술/디자인','원예/재배','맛집'),('jinhyuk_no97','문학/책','국내여행','건강/의학'),('jinuk_kim27','자동차','세계여행','맛집'),('jonghyun_won77','미술/디자인','스타/연예인','어학/외국어'),('jooseok_ha42','문학/책','상품리뷰','원예/재배'),('jungrak_shin75','미술/디자인','스타/연예인','사진'),('junseob_lim97','미술/디자인','방송','맛집'),('junwon_seo011','영화','일상/생각','건강/의학'),('junyoung_lee28','좋은글/이미지','게임','어학/외국어'),('kangnam_yoo27','드라마','스타/연예인','사진'),('keonhee_hong29','애완/반려동물','좋은글/이미지','원예/재배'),('kunwoo_park09','인테리어/DIY','요리/레시피','세계여행'),('kyongmin_hur08','패션/미용','건강/의학','비즈니스/경제'),('minho_kang58','만화/애니','취미','사회/정치'),('minje_jang03','만화/애니','방송','건강/의학'),('minseong_kim812','공연/전시','애완/반려동물','상품리뷰'),('minwoo_park32','일상/생각','취미','교육/학문'),('myunggi_song08','음악','자동차','건강/의학'),('sangsu_kim03','인테리어/DIY','스포츠','맛집'),('sangwoo_cho49','미술/디자인','공연/전시','비즈니스/경제'),('seihyok_park01','게임','맛집','교육/학문'),('seungho_lee92','영화','공연/전시','IT/컴퓨터'),('seungyup_na22','문학/책','일상/생각','원예/재배'),('sihwan_jang711','드라마','만화/애니','인테리어/DIY'),('sihwan_roh012','미술/디자인','상품리뷰','건강/의학'),('sokmin_park56','음악','애완/반려동물','IT/컴퓨터'),('soobin_jeong010','방송','원예/재배','어학/외국어'),('sookwang_ro08','드라마','자동차','교육/학문'),('sungbum_na910','세계여행','사회/정치','비즈니스/경제'),('sunghyun_kim73','육아/결혼','좋은글/이미지','원예/재배'),('taein_won04','만화/애니','원예/재배','취미'),('wonjung_kim36','일상/생각','애완/반려동물','세계여행'),('wonjun_choi412','사진','비즈니스/경제','어학/외국어'),('wonjun_jang57','육아/결혼','요리/레시피','건강/의학'),('woochan_cha75','공연/전시','요리/레시피','교육/학문'),('wooram_jeong56','드라마','좋은글/이미지','사회/정치'),('wooseok_ko88','미술/디자인','취미','건강/의학'),('wooyoung_jung98','원예/재배','자동차','국내여행'),('yongchan_lee91','영화','자동차','사회/정치'),('yooseom_han98','애완/반려동물','요리/레시피','스포츠'),('youngha_lee711','영화','상품리뷰','스포츠'),('youngpyo_ko19','스타/연예인','요리/레시피','세계여행');
/*!40000 ALTER TABLE `preference` ENABLE KEYS */;
UNLOCK TABLES;