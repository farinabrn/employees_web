CREATE DATABASE IF NOT EXISTS employees_web;

/*
USE employees_web;
IF NOT EXISTS `employees`
	CREATE TABLE `employees` (
		`id` int(11) NOT NULL AUTO_INCREMENT,
		`name` varchar(200) NOT NULL,
		`hiring_date` datetime(6) NOT NULL,
		`email` varchar(254) NOT NULL,
		`salary` int(11) NOT NULL,
		`cell_phone` int(11) NOT NULL,
		`manager_id` int(11) DEFAULT NULL,
		PRIMARY KEY (`id`),
		KEY `employees_manager_id_0674f795_fk_employees_id` (`manager_id`),
		CONSTRAINT `employees_manager_id_0674f795_fk_employees_id` FOREIGN KEY (`manager_id`) REFERENCES `employees` (`id`)
	) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

	INSERT INTO `employees` VALUES
		(1,'A','2019-09-01 17:57:07.000000','A@c.com',1000,999999,NULL),
		(2,'B','2019-09-01 18:09:49.000000','B@c.com',500,999292000,1),
		(3,'C','2019-09-02 00:29:04.000000','C@c.com',500,90999,1),
		(4,'D','2019-09-02 00:30:09.000000','D@c.com',200,999909092,2),
		(5,'E','2019-09-02 00:30:44.000000','E@c.com',300,99865544,2);
		*/