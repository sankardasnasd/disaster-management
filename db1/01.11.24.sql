/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - crisis_guard1
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`crisis_guard1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `crisis_guard1`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add camp_table',7,'add_camp_table'),
(26,'Can change camp_table',7,'change_camp_table'),
(27,'Can delete camp_table',7,'delete_camp_table'),
(28,'Can view camp_table',7,'view_camp_table'),
(29,'Can add login_table',8,'add_login_table'),
(30,'Can change login_table',8,'change_login_table'),
(31,'Can delete login_table',8,'delete_login_table'),
(32,'Can view login_table',8,'view_login_table'),
(33,'Can add notification',9,'add_notification'),
(34,'Can change notification',9,'change_notification'),
(35,'Can delete notification',9,'delete_notification'),
(36,'Can view notification',9,'view_notification'),
(37,'Can add services_table',10,'add_services_table'),
(38,'Can change services_table',10,'change_services_table'),
(39,'Can delete services_table',10,'delete_services_table'),
(40,'Can view services_table',10,'view_services_table'),
(41,'Can add coordinator_table',11,'add_coordinator_table'),
(42,'Can change coordinator_table',11,'change_coordinator_table'),
(43,'Can delete coordinator_table',11,'delete_coordinator_table'),
(44,'Can view coordinator_table',11,'view_coordinator_table'),
(45,'Can add goods_table',12,'add_goods_table'),
(46,'Can change goods_table',12,'change_goods_table'),
(47,'Can delete goods_table',12,'delete_goods_table'),
(48,'Can view goods_table',12,'view_goods_table'),
(49,'Can add guideline_table',13,'add_guideline_table'),
(50,'Can change guideline_table',13,'change_guideline_table'),
(51,'Can delete guideline_table',13,'delete_guideline_table'),
(52,'Can view guideline_table',13,'view_guideline_table'),
(53,'Can add item_table',14,'add_item_table'),
(54,'Can change item_table',14,'change_item_table'),
(55,'Can delete item_table',14,'delete_item_table'),
(56,'Can view item_table',14,'view_item_table'),
(57,'Can add emergency_response_team_table',15,'add_emergency_response_team_table'),
(58,'Can change emergency_response_team_table',15,'change_emergency_response_team_table'),
(59,'Can delete emergency_response_team_table',15,'delete_emergency_response_team_table'),
(60,'Can view emergency_response_team_table',15,'view_emergency_response_team_table'),
(61,'Can add medical_support_table',16,'add_medical_support_table'),
(62,'Can change medical_support_table',16,'change_medical_support_table'),
(63,'Can delete medical_support_table',16,'delete_medical_support_table'),
(64,'Can view medical_support_table',16,'view_medical_support_table'),
(65,'Can add needs_table',17,'add_needs_table'),
(66,'Can change needs_table',17,'change_needs_table'),
(67,'Can delete needs_table',17,'delete_needs_table'),
(68,'Can view needs_table',17,'view_needs_table'),
(69,'Can add user_table',18,'add_user_table'),
(70,'Can change user_table',18,'change_user_table'),
(71,'Can delete user_table',18,'delete_user_table'),
(72,'Can view user_table',18,'view_user_table'),
(73,'Can add request_table',19,'add_request_table'),
(74,'Can change request_table',19,'change_request_table'),
(75,'Can delete request_table',19,'delete_request_table'),
(76,'Can view request_table',19,'view_request_table'),
(77,'Can add complaint_table',20,'add_complaint_table'),
(78,'Can change complaint_table',20,'change_complaint_table'),
(79,'Can delete complaint_table',20,'delete_complaint_table'),
(80,'Can view complaint_table',20,'view_complaint_table'),
(81,'Can add volunteer_table',21,'add_volunteer_table'),
(82,'Can change volunteer_table',21,'change_volunteer_table'),
(83,'Can delete volunteer_table',21,'delete_volunteer_table'),
(84,'Can view volunteer_table',21,'view_volunteer_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'myapp','camp_table'),
(20,'myapp','complaint_table'),
(11,'myapp','coordinator_table'),
(15,'myapp','emergency_response_team_table'),
(12,'myapp','goods_table'),
(13,'myapp','guideline_table'),
(14,'myapp','item_table'),
(8,'myapp','login_table'),
(16,'myapp','medical_support_table'),
(17,'myapp','needs_table'),
(9,'myapp','notification'),
(19,'myapp','request_table'),
(10,'myapp','services_table'),
(18,'myapp','user_table'),
(21,'myapp','volunteer_table'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-11-01 08:47:23.196824'),
(2,'auth','0001_initial','2024-11-01 08:47:23.660352'),
(3,'admin','0001_initial','2024-11-01 08:47:23.774712'),
(4,'admin','0002_logentry_remove_auto_add','2024-11-01 08:47:23.783715'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-11-01 08:47:23.794284'),
(6,'contenttypes','0002_remove_content_type_name','2024-11-01 08:47:23.905663'),
(7,'auth','0002_alter_permission_name_max_length','2024-11-01 08:47:23.967559'),
(8,'auth','0003_alter_user_email_max_length','2024-11-01 08:47:23.992493'),
(9,'auth','0004_alter_user_username_opts','2024-11-01 08:47:23.999506'),
(10,'auth','0005_alter_user_last_login_null','2024-11-01 08:47:24.059951'),
(11,'auth','0006_require_contenttypes_0002','2024-11-01 08:47:24.063371'),
(12,'auth','0007_alter_validators_add_error_messages','2024-11-01 08:47:24.071381'),
(13,'auth','0008_alter_user_username_max_length','2024-11-01 08:47:24.132530'),
(14,'auth','0009_alter_user_last_name_max_length','2024-11-01 08:47:24.190390'),
(15,'auth','0010_alter_group_name_max_length','2024-11-01 08:47:24.209377'),
(16,'auth','0011_update_proxy_permissions','2024-11-01 08:47:24.216436'),
(17,'auth','0012_alter_user_first_name_max_length','2024-11-01 08:47:24.273737'),
(18,'myapp','0001_initial','2024-11-01 08:47:25.185760'),
(19,'sessions','0001_initial','2024-11-01 08:47:25.221276');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('6eb5a0z2ciem0zjjke72y9fkle6uedhu','eyJsaWQiOjIsImdvb2RzIjoiMiJ9:1t6o4M:iO_rUGVwibyMhf6knZLt0XTqHHDTQx9NwS87oFd2zI8','2024-11-15 09:35:50.083183');

/*Table structure for table `myapp_camp_table` */

DROP TABLE IF EXISTS `myapp_camp_table`;

CREATE TABLE `myapp_camp_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `landmark` varchar(100) NOT NULL,
  `capacity` bigint NOT NULL,
  `details` varchar(100) NOT NULL,
  `lattitude` varchar(100) NOT NULL,
  `longitude` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_camp_table` */

insert  into `myapp_camp_table`(`id`,`name`,`place`,`post`,`landmark`,`capacity`,`details`,`lattitude`,`longitude`,`image`) values 
(1,'camp','clt','673638','near hospital',20,'ggg','3145','12314','929202_s9ZBk8x.jpg');

/*Table structure for table `myapp_complaint_table` */

DROP TABLE IF EXISTS `myapp_complaint_table`;

CREATE TABLE `myapp_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaints` varchar(200) NOT NULL,
  `reply` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `CAMP_id` bigint NOT NULL,
  `COORDINATOR_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaint_table_CAMP_id_0fac2226_fk_myapp_camp_table_id` (`CAMP_id`),
  KEY `myapp_complaint_tabl_COORDINATOR_id_139152f8_fk_myapp_coo` (`COORDINATOR_id`),
  KEY `myapp_complaint_table_USER_id_fc088c0e_fk_myapp_user_table_id` (`USER_id`),
  CONSTRAINT `myapp_complaint_tabl_COORDINATOR_id_139152f8_fk_myapp_coo` FOREIGN KEY (`COORDINATOR_id`) REFERENCES `myapp_coordinator_table` (`id`),
  CONSTRAINT `myapp_complaint_table_CAMP_id_0fac2226_fk_myapp_camp_table_id` FOREIGN KEY (`CAMP_id`) REFERENCES `myapp_camp_table` (`id`),
  CONSTRAINT `myapp_complaint_table_USER_id_fc088c0e_fk_myapp_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_complaint_table` */

/*Table structure for table `myapp_coordinator_table` */

DROP TABLE IF EXISTS `myapp_coordinator_table`;

CREATE TABLE `myapp_coordinator_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `gender` varchar(30) NOT NULL,
  `phone_number` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `CAMP_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_coordinator_table_CAMP_id_4f35dcb2_fk_myapp_camp_table_id` (`CAMP_id`),
  KEY `myapp_coordinator_ta_LOGIN_id_b244b972_fk_myapp_log` (`LOGIN_id`),
  CONSTRAINT `myapp_coordinator_ta_LOGIN_id_b244b972_fk_myapp_log` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login_table` (`id`),
  CONSTRAINT `myapp_coordinator_table_CAMP_id_4f35dcb2_fk_myapp_camp_table_id` FOREIGN KEY (`CAMP_id`) REFERENCES `myapp_camp_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_coordinator_table` */

insert  into `myapp_coordinator_table`(`id`,`name`,`address`,`dob`,`gender`,`phone_number`,`email`,`image`,`CAMP_id`,`LOGIN_id`) values 
(1,'febin','skajfafjkj','2023-03-01','male',9876543210,'feb@gmail.com','1320161_yv6bkpN.jpeg',1,2);

/*Table structure for table `myapp_emergency_response_team_table` */

DROP TABLE IF EXISTS `myapp_emergency_response_team_table`;

CREATE TABLE `myapp_emergency_response_team_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `experience` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_emergency_resp_LOGIN_id_0d72695f_fk_myapp_log` (`LOGIN_id`),
  CONSTRAINT `myapp_emergency_resp_LOGIN_id_0d72695f_fk_myapp_log` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_emergency_response_team_table` */

/*Table structure for table `myapp_goods_table` */

DROP TABLE IF EXISTS `myapp_goods_table`;

CREATE TABLE `myapp_goods_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `details` varchar(100) NOT NULL,
  `stock` varchar(100) NOT NULL,
  `quantity` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `COORDINATOR_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_goods_table_COORDINATOR_id_e099fd81_fk_myapp_coo` (`COORDINATOR_id`),
  CONSTRAINT `myapp_goods_table_COORDINATOR_id_e099fd81_fk_myapp_coo` FOREIGN KEY (`COORDINATOR_id`) REFERENCES `myapp_coordinator_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_goods_table` */

insert  into `myapp_goods_table`(`id`,`type`,`name`,`date`,`details`,`stock`,`quantity`,`place`,`COORDINATOR_id`) values 
(2,'mediii','febin','2024-11-01','rlg4','tjkgb4','33','save',1);

/*Table structure for table `myapp_guideline_table` */

DROP TABLE IF EXISTS `myapp_guideline_table`;

CREATE TABLE `myapp_guideline_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `guidelines` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `COORDINATOR_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_guideline_tabl_COORDINATOR_id_8851d7f6_fk_myapp_coo` (`COORDINATOR_id`),
  CONSTRAINT `myapp_guideline_tabl_COORDINATOR_id_8851d7f6_fk_myapp_coo` FOREIGN KEY (`COORDINATOR_id`) REFERENCES `myapp_coordinator_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_guideline_table` */

insert  into `myapp_guideline_table`(`id`,`guidelines`,`details`,`date`,`COORDINATOR_id`) values 
(1,'111111_X1ISzSL.pdf','gg','2024-11-01',1);

/*Table structure for table `myapp_item_table` */

DROP TABLE IF EXISTS `myapp_item_table`;

CREATE TABLE `myapp_item_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `picture` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_item_table_LOGIN_id_f09458b9_fk_myapp_login_table_id` (`LOGIN_id`),
  CONSTRAINT `myapp_item_table_LOGIN_id_f09458b9_fk_myapp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_item_table` */

/*Table structure for table `myapp_login_table` */

DROP TABLE IF EXISTS `myapp_login_table`;

CREATE TABLE `myapp_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_login_table` */

insert  into `myapp_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'febin','febin','coordinator');

/*Table structure for table `myapp_medical_support_table` */

DROP TABLE IF EXISTS `myapp_medical_support_table`;

CREATE TABLE `myapp_medical_support_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `details` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `COORDINATOR_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_medical_suppor_COORDINATOR_id_1668dc51_fk_myapp_coo` (`COORDINATOR_id`),
  CONSTRAINT `myapp_medical_suppor_COORDINATOR_id_1668dc51_fk_myapp_coo` FOREIGN KEY (`COORDINATOR_id`) REFERENCES `myapp_coordinator_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_medical_support_table` */

/*Table structure for table `myapp_needs_table` */

DROP TABLE IF EXISTS `myapp_needs_table`;

CREATE TABLE `myapp_needs_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `quantity` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `COORDINATOR_id` bigint NOT NULL,
  `GOODS_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_needs_table_COORDINATOR_id_bcc677b9_fk_myapp_coo` (`COORDINATOR_id`),
  KEY `myapp_needs_table_GOODS_id_d0a6867f_fk_myapp_goods_table_id` (`GOODS_id`),
  CONSTRAINT `myapp_needs_table_COORDINATOR_id_bcc677b9_fk_myapp_coo` FOREIGN KEY (`COORDINATOR_id`) REFERENCES `myapp_coordinator_table` (`id`),
  CONSTRAINT `myapp_needs_table_GOODS_id_d0a6867f_fk_myapp_goods_table_id` FOREIGN KEY (`GOODS_id`) REFERENCES `myapp_goods_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_needs_table` */

/*Table structure for table `myapp_notification` */

DROP TABLE IF EXISTS `myapp_notification`;

CREATE TABLE `myapp_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `notification` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `details` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_notification` */

insert  into `myapp_notification`(`id`,`notification`,`date`,`details`) values 
(1,'come','2024-11-01','fnlqf');

/*Table structure for table `myapp_request_table` */

DROP TABLE IF EXISTS `myapp_request_table`;

CREATE TABLE `myapp_request_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `request` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_request_table_USER_id_8ef558ea_fk_myapp_user_table_id` (`USER_id`),
  CONSTRAINT `myapp_request_table_USER_id_8ef558ea_fk_myapp_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_request_table` */

/*Table structure for table `myapp_services_table` */

DROP TABLE IF EXISTS `myapp_services_table`;

CREATE TABLE `myapp_services_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_services_table` */

/*Table structure for table `myapp_user_table` */

DROP TABLE IF EXISTS `myapp_user_table`;

CREATE TABLE `myapp_user_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` int NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone_number` bigint NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_table_LOGIN_id_76a60eb1_fk_myapp_login_table_id` (`LOGIN_id`),
  CONSTRAINT `myapp_user_table_LOGIN_id_76a60eb1_fk_myapp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_user_table` */

/*Table structure for table `myapp_volunteer_table` */

DROP TABLE IF EXISTS `myapp_volunteer_table`;

CREATE TABLE `myapp_volunteer_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_volunteer_table_LOGIN_id_101ae350_fk_myapp_login_table_id` (`LOGIN_id`),
  CONSTRAINT `myapp_volunteer_table_LOGIN_id_101ae350_fk_myapp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_volunteer_table` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
