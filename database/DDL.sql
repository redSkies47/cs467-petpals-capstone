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
CREATE TABLE `Dispositions` (
    `id_disposition` int AUTO_INCREMENT UNIQUE NOT NULL,
    `description` varchar(50) NOT NULL,
    PRIMARY KEY (`id_disposition`)
);

-- Create Animals table
CREATE TABLE `Animals` (
    `id_animal` int AUTO_INCREMENT UNIQUE NOT NULL,
    `id_availability` int DEFAULT 1, /* Available */
    `id_species` int DEFAULT 1, /* Other */
    `id_breed` int DEFAULT 1, /* Other */
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
    `id_credential` int DEFAULT 1, /* Public */
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
-- Insert categorical data into tables
-- -----------------------------------------------------------------------------

-- Insert Availabilities categories
INSERT INTO `Availabilities` (`description`)
VALUES
('Available'), /* id_availability = 1, to use as default value in Animals */
('Not Available'),
('Pending'),
('Adopted');

-- Insert Species categories
INSERT INTO `Species` (`description`)
VALUES
('Other'), /* id_species = 1, to use as default value in Animals */
('Dog'),
('Cat');

-- -- Insert Breeds categories
INSERT INTO `Breeds` (`id_species`, `description`)
VALUES
(1, 'Other'), /* id_breed = 1, to use as default value in Animals */
(2, 'Pit Bull'),
(2, 'Labrador Retriever'),
(2, 'Chihuahua'),
(2, 'Boxer'),
(2, 'German Shepherd Dog'),
(2, 'Beagle'),
(2, 'Dachshund'),
(2, 'Border Collie'),
(2, 'Australian Cattle Dog'),
(2, 'Jack Russell Terrier'),
(2, 'Australian Shepherd'),
(2, 'Shih Tzu'),
(2, 'Rottweiler'),
(2, 'Siberian Husky'),
(2, 'French Bulldog'),
(2, 'Golden Retriever'),
(2, 'Poodle'),
(2, 'Bulldog'),
(2, 'German Shorthaired Pointer'),
(2, 'Pembroke Welsh Corgi'),
(2, 'Yorkshire Terrier'),
(2, 'Cavalier King Charles Spaniel'),
(2, 'Doberman Pinscher'),
(2, 'Miniature Schnauzer'),
(2, 'Cane Corso'),
(2, 'Great Dane'),
(3, 'Domestic Shorthair'),
(3, 'Domestic Longhair'),
(3, 'Maine Coon'),
(3, 'Ragdoll'),
(3, 'American Shorthair'),
(3, 'Siamese'),
(3, 'Russian Blue'),
(3, 'Bengal'),
(3, 'Persian'),
(3, 'Bombay'),
(3, 'Devon Rex'),
(3, 'Exotic Shorthair'),
(3, 'British Shorthair'),
(3, 'Abyssinian'),
(3, 'Scottish Fold'),
(3, 'Sphynx'),
(3, 'Siberian'),
(3, 'Norwegian Forest Cat'),
(3, 'Oriental Shorthair'),
(3, 'Cornish Rex'),
(3, 'Selkirk Rex'),
(3, 'Birman');

-- Insert Genders categories
INSERT INTO `Genders` (`description`)
VALUES
('Male - Intact'),
('Female - Intact'),
('Male - Neutered'),
('Female - Spayed');

-- Insert Dispositions categories
INSERT INTO `Dispositions` (`description`)
VALUES
('Good with other animals'),
('Good with children'),
('Animal must be leashed at all times'),
('High energy needs'),
('Low energy needs'),
('High grooming needs'),
('Low grooming needs'),
('Vocal');

-- Insert Credentials categories
INSERT INTO `Credentials` (`description`)
VALUES
('public'), /* id_credential = 1, to use as default value in Accounts */
('administrative');

-- -----------------------------------------------------------------------------
-- Re-enable commits and foreign key checks
-- -----------------------------------------------------------------------------
SET FOREIGN_KEY_CHECKS = 1;
COMMIT;
