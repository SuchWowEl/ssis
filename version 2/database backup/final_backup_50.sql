-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: test_db
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `course code` varchar(8) NOT NULL,
  `course` varchar(100) NOT NULL,
  PRIMARY KEY (`course code`),
  UNIQUE KEY `course code_UNIQUE` (`course code`),
  UNIQUE KEY `course_UNIQUE` (`course`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES ('BSCE','Bachelor of Science in Ceramic Engineering'),('BSChE','Bachelor of Science in Chemical Engineering'),('BS Chem','Bachelor of Science in Chemistry'),('BSCA','Bachelor of Science in Computer Applications'),('BSCS','Bachelor of Science in Computer Science'),('BSEE','Bachelor of Science in Electronics Engineering'),('BSIT','Bachelor of Science in Information Technology'),('BSMetE','Bachelor of Science in Metallurgical Engineering'),('BSEM','Bachelor of Science in Mining Engineering'),('BSPSYCH','Bachelor of Science in Psychology');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `student id` char(9) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `name` varchar(255) NOT NULL,
  `gender` varchar(30) NOT NULL,
  `year level` varchar(8) NOT NULL,
  `course code` varchar(45) NOT NULL,
  PRIMARY KEY (`student id`),
  UNIQUE KEY `student id_UNIQUE` (`student id`),
  KEY `course code_idx` (`course code`),
  CONSTRAINT `course code` FOREIGN KEY (`course code`) REFERENCES `courses` (`course code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES ('2021-0000','zero','Non-binary','1st Year','BSIT'),('2021-0001','one','Male','2nd Year','BSCS'),('2021-0002','dos','Female','3rd Year','BSPSYCH'),('2021-0003','tres','Male','1st Year','BSCA'),('2021-0004','quatro','Male','2nd Year','BSCS'),('2021-0005','cinco','Female','3rd Year','BSEM'),('2021-0006','saiz','Non-binary','2nd Year','BSIT'),('2021-0007','siete','Female','2nd Year','BSPSYCH'),('2021-0008','otso','Female','1st Year','BSEE'),('2021-0009','nueve','Non-binary','4th Year','BSMetE'),('2021-0010','dyis','Female','2nd Year','BSEE'),('2021-0023','mj','Male','2nd Year','BSChE'),('2021-0024','kobe','Male','3rd Year','BSCS'),('2021-0078','Who likes all our pretty songs','Female','1st Year','BSChE'),('2021-1456','omyghot','Non-binary','1st Year','BSCE'),('2021-2423','But he knows not','Male','2nd Year','BSIT'),('2021-5242','And he likes','Female','1st Year','BSEE'),('2021-5243','All our pretty songs','Male','1st Year','BSEE'),('2021-5244','And he likes to','Female','2nd Year','BSMetE'),('2021-5245','Shoot his gun','Male','3rd Year','BS Chem'),('2021-5246','But he knows not','Non-binary','2nd Year','BSIT'),('2021-5247','What it means','Non-binary','2nd Year','BSIT'),('2021-5248','Knows not what it means','Male','3rd Year','BSCA'),('2021-5249','And I say yeah','Male','3rd Year','BSCA'),('2021-5250','Somebody once told me','Female','1st Year','BSCS'),('2021-5251','The world is gonna roll me','Male','2nd Year','BSCS'),('2021-5252','I ain\'t the sharpest tool in the shed','Female','3rd Year','BSMetE'),('2021-5253','She was looking','Male','2nd Year','BSCE'),('2021-5254','kinda dumb','Female','3rd Year','BSIT'),('2021-5255','In shape of an \"L\"','Male','1st Year','BSMetE'),('2021-5256','on her forehead','Non-binary','1st Year','BSCE'),('2021-5257','Well the years','Male','1st Year','BS Chem'),('2021-5258','Start coming','Female','2nd Year','BSEM'),('2021-5259','And they don\'t','Male','3rd Year','BSCE'),('2021-5260','Stop coming','Non-binary','3rd Year','BSCE'),('2021-5261','Fed to the rules','Male','2nd Year','BS Chem'),('2021-5262','And I hit the ground','Female','2nd Year','BSMetE'),('2021-5263','RUNNING','Male','3rd Year','BSCE'),('2021-5264','Didn\'t make sense','Female','4th Year','BSChE'),('2021-5265','Not to live for fun','Male','1st Year','BSPSYCH'),('2021-5266','Your brain gets smart','Female','1st Year','BSCE'),('2021-5267','So much to d','Female','2nd Year','BSChE'),('2021-6435','Knows not what it means','Non-binary','2nd Year','BSEM'),('2021-6512','Who likes','Non-binary','4th Year','BSCE'),('2021-7844','no waeaeae','Male','3rd Year','BSEM'),('2021-7845','sad','Male','1st Year','BS Chem'),('2021-8452','And he likes to sing along','Non-binary','4th Year','BS Chem'),('2021-8542','HES THE ONE','Male','2nd Year','BSMetE'),('2021-8564','And I say he\'s the one','Male','3rd Year','BSCA'),('2021-9835','And he likes to shoot his gun','Female','2nd Year','BSPSYCH');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-22 12:07:46
