-- -----------------------------------------------------------------------------
-- Disable commits and foreign key checks
-- -----------------------------------------------------------------------------
SET FOREIGN_KEY_CHECKS = 0;
SET AUTOCOMMIT = 0;


-- -----------------------------------------------------------------------------
-- Create tables
-- -----------------------------------------------------------------------------

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
    `id_shelter` int NOT NULL,
    PRIMARY KEY (`id_animal`),
    FOREIGN KEY (`id_availability`) REFERENCES `Availabilities` (`id_availability`),
    FOREIGN KEY (`id_species`) REFERENCES `Species` (`id_species`),
    FOREIGN KEY (`id_breed`) REFERENCES `Breeds` (`id_breed`),
    FOREIGN KEY (`id_gender`) REFERENCES `Genders` (`id_gender`),
    FOREIGN KEY (`id_shelter`) REFERENCES `Shelters` (`id_shelter`)
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

-- Create Images table
CREATE TABLE `Images` (
    `id_image` int AUTO_INCREMENT UNIQUE NOT NULL,
    `id_animal` int NOT NULL,
    PRIMARY KEY (`id_image`),
    FOREIGN KEY (`id_animal`) REFERENCES `Animals` (`id_animal`)
        ON DELETE CASCADE
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

-- Create Liked Animals table
CREATE TABLE `Liked_Animals` (
    `id_liked_animal` int AUTO_INCREMENT UNIQUE NOT NULL,
    `id_account` int NOT NULL,
    `id_animal` int NOT NULL,
    PRIMARY KEY (`id_liked_animal`),
    FOREIGN KEY (`id_account`) REFERENCES `Accounts` (`id_account`),
    FOREIGN KEY (`id_animal`) REFERENCES `Animals` (`id_animal`)
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
(3, 'Birman'),
(2, 'Shiba Inu');

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
-- Insert sample data into tables
-- -----------------------------------------------------------------------------
-- Insert new Shelters
INSERT INTO `Shelters` (`name`, `address`, `phone_number`,
`opening_hour`, `closing_hour`)
VALUES
('Pet Refuge', '2273 Bel Meadow Drive, Bellevue Oregon',
'909-410-5017', 9, 17),
('Jefferson County Animal Shelter', '153 Lakefront Drive, Avondale Washington', '782-889-0021', 9, 17),
('Happy Pet Rescue', '621 Hazel Street, Bisbee California', '145-617-0830', 10, 16);

-- Insert new Animals
INSERT INTO `Animals` (`id_availability`, `id_species`, `id_breed`, `name`, `birth_date`, `id_gender`, `size`, `summary`, `date_created`, `id_shelter`)
VALUES
(1, 3, 36, 'Cleocatra',
'2019-04-20', 2, 12,
'Cleocatra is a sweet independent persian cat. She keeps herself very busy but is very sweet and open to some pampering!',
'2023-09-04', 1),
(1, 3, 35, 'Safari',
'2021-04-02', 4, 8,
'Looking for a social cat? Look no further than the social Safari! She gets along well with children and other pets.',
'2022-10-10', 2),
(2, 3, 46, 'Tango',
'2023-01-04', 3, 6,
'Anywhere is a stage for the singing Tango who is otherwise silently sleeping. Seeks out people but doesn''t quite get along with other animals.',
'2023-10-26', 2),
(1, 2, 18, 'Curls',
'2018-12-03', 2, 33,
'Curls came from another home that could no longer care for her. She gets along well with kids and is looking for a great carer who can groom her well.',
'2023-10-26', 3),
(3, 2, 7, 'Luna',
'2023-06-29', 1, 21,
'Puppy Luna has been getting lots of training. He is very playful with kids and other animals.',
'2023-04-05', 1),
(4, 2, 15, 'Snowy',
'2023-02-10', 3, 32,
'Snowy had to part ways from his liter recently. Expect lots of sassy vocals from him! Can be a bit too excited on walks.',
'2023-03-27', 3),
(1, 1, 1, 'Coco',
'2021-06-20', 2, 5,
'Persevering Coco went through a house fire where her caretakers had to let her go. She is very social and can speak several phrases.',
'2023-10-26', 3),
(3, 2, 3, 'Fuji',
'2019-08-13', 1, 70,
'Fuji is a super dog & people-friendly retriever. And also a food-driven guy. He loves chasing balls and whatever is moving.',
'2023-11-29', 1),
(4, 2, 50, 'Sushi',
'2017-10-29', 2, 20,
'Sushi is a bit shy with people but definitely friendly to kids. Sushi enjoys playing with all kinds of puzzle toys.',
'2023-11-29', 2);

-- Insert new Animal_Dispositions
INSERT INTO `Animal_Dispositions` (`id_animal`, `id_disposition`)
VALUES
(1, 5),
(1, 6),
(2, 1),
(2, 2),
(2, 5),
(3, 7),
(3, 8),
(4, 2),
(4, 6),
(5, 1),
(5, 2),
(6, 3),
(6, 8),
(7, 4),
(7, 8),
(8, 1),
(9, 2);

-- Insert new Accounts
INSERT INTO `Accounts` (`id_credential`, `email`, `password`, `name`)
VALUES
(2, 'director@petrefuge.org', 'L4ve@nimal$', 'Pet Refuge'),
(1, 'eSharp@gmail.com', 'dogSearch4', 'Enrique Sharp'),
(1, 'tashHop@icloud.com', 'sw33Tc@ts', 'Tasha Hopkins');

-- Insert new News
INSERT INTO `News` (`date`, `title`, `body`)
VALUES
('2023-10-26', 'No Fees November',
'This upcoming month of November, all fees will be waived. The adoptions fees for cats, dogs, and other animals at Pet Refuge will come down to $0! This is brought to the Bellevue community by the generous fundraising efforts of the Forest Rangers of the North. Home a nice furry companion before the holidays! Take the steps to learn about a lifestyle compatibility for interested animals. Stop on by at Pet Refuge today!'),
('2023-10-27', 'Found Kittens?',
'Before contacting the Pet Refuge shelter, learn about some steps to take when finding kittens in your community. 1. Is the mother cat still around? Figure out if the mother cat is seen around the kittens for a period of around half a day. If the mother cat is no longer around, make an assessment on the condition of the kittens... Follow the link to learn more... https://rroll.to/hjme3D'),
('2023-10-28', 'Winter 5k Run Fundraiser',
'This December 10 at Bellevue Community Center, there is a local 5k Winter Run. Join Pet Refuge in the 5k Winter Run as a volunteer or donor. Volunteers can join the 5k Run as representative runners. Another opportunity is to be present in the tent providing information and other goodies to the community about Pet Refuge. Or support our fundraising efforts by donating on behalf of our runners! To learn more visit our 5k Winter Run''s event page.');

-- Insert new Images
INSERT INTO `Images` (`id_animal`)
VALUES
(1),
(2),
(3),
(4),
(5),
(6),
(7);

-- -----------------------------------------------------------------------------
-- Re-enable commits and foreign key checks
-- -----------------------------------------------------------------------------
SET FOREIGN_KEY_CHECKS = 1;
COMMIT;
