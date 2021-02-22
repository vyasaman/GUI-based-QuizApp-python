-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.22 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for Exam
CREATE DATABASE IF NOT EXISTS `Exam` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Exam`;

-- Dumping structure for table Exam.question
CREATE TABLE IF NOT EXISTS `question` (
  `qid` int NOT NULL AUTO_INCREMENT,
  `question` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `op1` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `op2` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `op3` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `op4` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `correct` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `techID` int DEFAULT NULL,
  PRIMARY KEY (`qid`),
  UNIQUE KEY `question` (`question`),
  KEY `techID` (`techID`),
  CONSTRAINT `question_ibfk_1` FOREIGN KEY (`techID`) REFERENCES `technology` (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table Exam.question: ~12 rows (approximately)
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` (`qid`, `question`, `op1`, `op2`, `op3`, `op4`, `correct`, `techID`) VALUES
	(1, ' A process that involves recognizing and focusing on the important characteristics of a situation or object is known as:', 'Encapsulation ', 'Polymorphism', 'Abstraction ', 'Inheritance', 'c', 1),
	(2, ' Which statement is true regarding an object?', 'An object is what classes instantiated are from', 'An object is an instance of a class', 'An object is a variable', 'An object is a reference to an attribute', 'b', 1),
	(3, ' In object-oriented programming, new classes can be defined by extending existing classes. This is an example of:', 'Encapsulation ', 'Interface', 'Composition ', 'Inheritance ', 'd', 1),
	(4, 'The wrapping up of data and functions into a single unit is called', 'Encapsulation', 'Polymorphism', 'Abstraction', 'Inheritance', 'a', 1),
	(5, ' Which of the following is not OOPS concept in Java?', 'Inheritance', 'Encapsulation', 'Polymorphism', 'Compilation', 'd', 1),
	(6, 'Which of the following is invalid?', '_a = 1', '__a = 1', '__str__ = 1', ' none of the mentioned', 'd', 2),
	(7, 'Which of the following cannot be a variable?', '__int__', 'in', 'it', 'on', 'b', 2),
	(8, 'Which of the following is an invalid statement?', 'abc = 1,000,000', 'a b c = 1000 2000 3000', ' a,b,c = 1000, 2000, 3000', 'a_b_c = 1,000,000', 'b', 2),
	(9, 'Which is the correct operator for X to the power y?', 'X^y', 'X^^y', 'X**y', 'None of the mentioned', 'c', 2),
	(10, 'Which one of these is floor division?', '//', '/', '%', 'None of the mentioned', 'a', 2),
	(11, 'Java Script is a _____ language.', 'Scripting', 'Markup', 'Low Level', 'Assembly', 'a', 3),
	(13, 'Which of the following is a JavaScript Framework?', 'Django', 'Angular', 'Spring', 'Flask', 'b', 3);
/*!40000 ALTER TABLE `question` ENABLE KEYS */;

-- Dumping structure for table Exam.results
CREATE TABLE IF NOT EXISTS `results` (
  `rid` int NOT NULL AUTO_INCREMENT,
  `uid` int NOT NULL,
  `techID` int NOT NULL,
  `marks` int DEFAULT NULL,
  `resDate` datetime DEFAULT NULL,
  `status` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'not Declared',
  PRIMARY KEY (`rid`),
  KEY `FK__userdata` (`uid`),
  KEY `FK_results_technology` (`techID`),
  CONSTRAINT `FK__userdata` FOREIGN KEY (`uid`) REFERENCES `userdata` (`uid`),
  CONSTRAINT `FK_results_technology` FOREIGN KEY (`techID`) REFERENCES `technology` (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table Exam.results: ~0 rows (approximately)
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
INSERT INTO `results` (`rid`, `uid`, `techID`, `marks`, `resDate`, `status`) VALUES
	(4, 10002, 2, 100, '2021-01-31 20:36:22', 'Pass'),
	(5, 10005, 4, 95, '2021-02-19 12:47:56', 'Pass');
/*!40000 ALTER TABLE `results` ENABLE KEYS */;

-- Dumping structure for table Exam.technology
CREATE TABLE IF NOT EXISTS `technology` (
  `tid` int NOT NULL AUTO_INCREMENT,
  `t_name` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tid`),
  UNIQUE KEY `t_name` (`t_name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table Exam.technology: ~2 rows (approximately)
/*!40000 ALTER TABLE `technology` DISABLE KEYS */;
INSERT INTO `technology` (`tid`, `t_name`) VALUES
	(4, 'C++'),
	(1, 'Java'),
	(3, 'Java Script'),
	(2, 'Python');
/*!40000 ALTER TABLE `technology` ENABLE KEYS */;

-- Dumping structure for table Exam.userdata
CREATE TABLE IF NOT EXISTS `userdata` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `uname` varchar(50) NOT NULL DEFAULT '',
  `pass` varchar(50) NOT NULL DEFAULT '',
  `role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=10006 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table Exam.userdata: ~5 rows (approximately)
/*!40000 ALTER TABLE `userdata` DISABLE KEYS */;
INSERT INTO `userdata` (`uid`, `uname`, `pass`, `role`) VALUES
	(10001, 'Aman Vyas', '123456', 'Admin'),
	(10002, 'Ankit', 'ankit123', 'student'),
	(10003, 'Raj', 'raj123', 'admin'),
	(10004, 'Akshay Kumar', 'ak123', 'student'),
	(10005, 'Ajay Devgun', 'ajd123', 'student');
/*!40000 ALTER TABLE `userdata` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
