USE pokedex;

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
	`id` int auto_increment PRIMARY KEY,
    `pseudo` varchar(50) NOT NULL UNIQUE,
    `password` varchar(100) NOT NULL,
    `role` varchar(10) default 'user'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Table structure for table `bag`
--

CREATE TABLE `bag` (
	`user_id` int NOT NULL,
    `pokemon_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;