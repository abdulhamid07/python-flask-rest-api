/*
SQLyog Ultimate v13.1.1 (64 bit)
MySQL - 5.7.24 : Database - flaskpython
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
USE `flaskpython`;

/*Table structure for table `alembic_version` */

DROP TABLE IF EXISTS `alembic_version`;

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `alembic_version` */

insert  into `alembic_version`(`version_num`) values 
('fa2ef4a949cb');

/*Table structure for table `dosen` */

DROP TABLE IF EXISTS `dosen`;

CREATE TABLE `dosen` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nidn` varchar(30) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `alamat` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `dosen` */

insert  into `dosen`(`id`,`nidn`,`nama`,`phone`,`alamat`) values 
(1,'155410026','Abdul Hamid','089867551243','Bantul'),
(2,'163119987','Putri Ayu','082378156612','Sleman'),
(3,'17561761109','Panji Sobari','089876127701','Bantul'),
(4,'185410021','Surya P','083387119812','Sleman');

/*Table structure for table `mahasiswa` */

DROP TABLE IF EXISTS `mahasiswa`;

CREATE TABLE `mahasiswa` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nim` varchar(30) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `alamat` varchar(100) NOT NULL,
  `dosen_satu` bigint(20) DEFAULT NULL,
  `dosen_dua` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dosen_satu` (`dosen_satu`),
  KEY `dosen_dua` (`dosen_dua`),
  CONSTRAINT `mahasiswa_ibfk_1` FOREIGN KEY (`dosen_satu`) REFERENCES `dosen` (`id`) ON DELETE SET NULL,
  CONSTRAINT `mahasiswa_ibfk_2` FOREIGN KEY (`dosen_dua`) REFERENCES `dosen` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `mahasiswa` */

insert  into `mahasiswa`(`id`,`nim`,`nama`,`phone`,`alamat`,`dosen_satu`,`dosen_dua`) values 
(1,'165119077','Endra S','089834127711','Wonosari',1,2),
(2,'155410012','Marcelino T','082376115623','Wonosobo',2,1),
(3,'163110023','Sarwan H','081526771890','Manding',3,4);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(250) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `level` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`name`,`email`,`password`,`created_at`,`updated_at`,`level`) values 
(1,'admin','admin@gmail.com','pbkdf2:sha256:260000$KofS16jbEIUmlnGw$6ee188f1ea45a849e3320036e5de68931153aa7b1efad5e395e81d7b233bb55b','2021-09-25 14:37:47','2021-09-25 14:37:47',1),
(2,'hamid','hamid@gmail.com','pbkdf2:sha256:260000$FumZRSdoxJoNsYrQ$6e25f0b5b221d71eaff31c3888aa8c75f3da5a08c2c5fe46c2656cb6c37a7d19','2021-09-25 18:34:38','2021-09-25 18:34:38',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
