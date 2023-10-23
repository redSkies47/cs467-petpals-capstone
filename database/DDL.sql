-- -----------------------------------------------------------------------------
-- Disable commits and foreign key checks
-- -----------------------------------------------------------------------------
SET FOREIGN_KEY_CHECKS = 0;
SET AUTOCOMMIT = 0;


-- -----------------------------------------------------------------------------
-- Create tables
-- -----------------------------------------------------------------------------

-- Create Availabilities table
CREATE TABLE `Availabilities` (
    `id_availability` int AUTO_INCREMENT UNIQUE NOT NULL,
    `description` varchar(50) NOT NULL,
    PRIMARY KEY (`id_availability`)
);

-- Create Species table
CREATE TABLE `Species` (
    `id_species` int AUTO_INCREMENT UNIQUE NOT NULL,
    `description` varchar(50) NOT NULL,
    PRIMARY KEY (`id_species`)
);

-- Create Breeds table
CREATE TABLE `Breeds` (
    `id_breed` int AUTO_INCREMENT UNIQUE NOT NULL,
    `id_species` int NOT NULL,
    `description` varchar(50) NOT NULL,
    PRIMARY KEY (`id_breed`),
    FOREIGN KEY (`id_species`) REFERENCES `Species` (`id_species`)
);

-- Create Genders table
CREATE TABLE `Genders` (
    `id_gender` int AUTO_INCREMENT UNIQUE NOT NULL,
    `description` varchar(50) NOT NULL,
    PRIMARY KEY (`id_gender`)
);

-- Create Dispositions table
CREATE TABLE `Dispostions` (
    `id_disposition` int AUTO_INCREMENT UNIQUE NOT NULL,
    `description` varchar(50) NOT NULL,
    PRIMARY KEY (`id_disposition`)
);

-- Create Animals table
CREATE TABLE `Animals` (
    `id_animal` int AUTO_INCREMENT UNIQUE NOT NULL,
    `id_availability` int DEFAULT 0, /* Available */
    `id_species` int DEFAULT 0, /* Other */
    `id_breed` int DEFAULT 0, /* Other */
    `name` varchar(45) NOT NULL,
    `birth_date` date NOT NULL,
    `id_gender` int NOT NULL,
    `size` int NOT NULL,
    `summary` text(500),
    `date_created` date NOT NULL,
        /* DEFAULT GETDATE() not working, handle on client-side */
    PRIMARY KEY (`id_animal`),
    FOREIGN KEY (`id_availability`) REFERENCES `Availabilities` (`id_availability`),
    FOREIGN KEY (`id_species`) REFERENCES `Species` (`id_species`),
    FOREIGN KEY (`id_breed`) REFERENCES `Breeds` (`id_breed`),
    FOREIGN KEY (`id_gender`) REFERENCES `Genders` (`id_gender`)
);

-- Create Animal_Dispositions table
CREATE TABLE `Animal_Dispositions` (
    `id_animal_disposition` int AUTO_INCREMENT UNIQUE NOT NULL,
    `id_animal` int NOT NULL,
    `id_disposition` int NOT NULL,
    PRIMARY KEY (`id_animal_disposition`),
    FOREIGN KEY (`id_animal`) REFERENCES `Animals` (`id_animal`)
        ON DELETE CASCADE,
    FOREIGN KEY (`id_disposition`) REFERENCES `Dispositions` (`id_disposition`)
);

-- Create Credentials table
CREATE TABLE `Credentials` (
    `id_credential` int AUTO_INCREMENT UNIQUE NOT NULL,
    `description` varchar(50) NOT NULL,
    PRIMARY KEY (`id_credential`)
);

-- Create Accounts table
CREATE TABLE `Accounts` (
    `id_account` int AUTO_INCREMENT UNIQUE NOT NULL,
    `id_credential` int NOT NULL,
    `email` varchar(100) NOT NULL,
    `password` varchar(30) NOT NULL,
    `name` varchar(100),
    PRIMARY KEY (`id_account`),
    FOREIGN KEY (`id_credential`) REFERENCES `Credentials` (`id_credential`)
);

-- Create News table
CREATE TABLE `News` (
    `id_news` int AUTO_INCREMENT UNIQUE NOT NULL,
    `date` date NOT NULL,
        /* DEFAULT GETDATE() not working, handle on client-side */
    `title` varchar(255) NOT NULL,
    `body` text(500) NOT NULL,
    PRIMARY KEY (`id_news`)
);

-- Create Shelters table
CREATE TABLE `Shelters` (
    `id_shelter` int AUTO_INCREMENT UNIQUE NOT NULL,
    `name` varchar(100) NOT NULL,
    `address` varchar(255) NOT NULL,
    `phone_number` varchar(12) NOT NULL, /* ###-###-#### */
    `opening_hour` int NOT NULL
        CHECK (`opening_hour` >= 0 AND `opening_hour` < 25),
    `closing_hour` int NOT NULL
        CHECK (`closing_hour` >= 0 AND `closing_hour` < 25),
    PRIMARY KEY (`id_shelter`)
);


-- -----------------------------------------------------------------------------
-- Re-enable commits and foreign key checks
-- -----------------------------------------------------------------------------
SET FOREIGN_KEY_CHECKS = 1;
COMMIT;
