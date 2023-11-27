/*
Kristy Kha
Samantha Lin
Yuk Shu Shukie Li
Jonathan Chan
PetPals - "Dating" App for Animal Adoption
CS 467 - Online Capstone
*/

-- -----------------------------------------------------------------------------
-- Disable commits and foreign key checks
-- -----------------------------------------------------------------------------
SET FOREIGN_KEY_CHECKS = 0;
SET AUTOCOMMIT = 0;


-- -----------------------------------------------------------------------------
-- Remove tables
-- -----------------------------------------------------------------------------
-- Delete Accounts table
DROP TABLE `Accounts`;

-- Delete Animals table
DROP TABLE `Animals`;

-- Delete Animal Dispositions table
DROP TABLE `Animal_Dispositions`;

-- Delete Availabilities table
DROP TABLE `Availabilities`;

-- Delete Breeds table
DROP TABLE `Breeds`;

-- Delete Credentials table
DROP TABLE `Credentials`;

-- Delete Dispositions table
DROP TABLE `Dispositions`;

-- Delete Genders table
DROP TABLE `Genders`;

-- Delete Images table
DROP Table `Images`;

-- Delete News table
DROP TABLE `News`;

-- Delete Shelters table
DROP TABLE `Shelters`;

-- Delete Species table
DROP TABLE `Species`;

-- -----------------------------------------------------------------------------
-- Re-enable commits and foreign key checks
-- -----------------------------------------------------------------------------
SET FOREIGN_KEY_CHECKS = 1;
COMMIT;
