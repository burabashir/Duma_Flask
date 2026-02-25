-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 25, 2026 at 09:35 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dumasokogarden`
--

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_description` text DEFAULT NULL,
  `product_cost` int(11) DEFAULT NULL,
  `product_photo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`product_id`, `product_name`, `product_description`, `product_cost`, `product_photo`) VALUES
(1, 'Delemare', 'Chocolate', 150, '<FileStorage: \'Copilot_20260131_131249.png\' (\'image/png\')>'),
(2, 'Delemare', 'Chocolate', 150, 'Copilot_20260131_131249.png'),
(4, 'Delemare', 'Vanilla', 180, 'download.webp'),
(5, 'Natural', 'Vanilla', 120, 'shopping.webp'),
(6, 'Dairy Fresh', 'Hybrid', 160, 'shopping (1).webp'),
(7, 'Daima', 'Thick Chocolate', 160, 'shopping (2).webp'),
(8, 'Daima', 'Vanilla Chocolate', 160, 'shopping (2).webp'),
(9, 'Kwashaire', 'Vanilla Chocolate', 190, 'shopping (1).webp');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `email`, `phone`) VALUES
(1, 'Bashir Bura', '12345678', 'bashirbura@gmail.com', '0712345678'),
(2, 'Lewis Lena', '87654321', 'lewislena@gmail.com', '0787654321'),
(3, 'Claire Fire', '76543210', 'clairefire@gmail.com', '0776543210'),
(4, 'Akili Brain', '01234567', 'akilibrain@gmail.com', '0701234567'),
(5, 'Mschana Hard', '12345690', 'mschanahard@gmail.com', '0712345690'),
(6, 'Bahati Wambua', '09123456', 'bahatiwambua@gmail.com', '0709123456'),
(7, 'Jack Chan', '43218765', 'jackchan@gmail.com', '0743218765'),
(8, 'Bruce Lee', '12348765', 'brucelee@gmail.com', '0712348765'),
(9, 'Raven Heart', '87651234', 'ravenheart@gmail.com', '0787651234'),
(10, 'John Look', '09876543', 'johnlook@gmail.com', '0709876543'),
(11, 'Mary', '1234', 'mary@gmail.com', '0712340678'),
(12, 'Bore Soleh', '234174', 'boresoleh@gmail.com', '07144540678'),
(13, 'Nyambane Job', '76456274', 'jobnyambanegmail.com', '0714454078'),
(14, 'Nyamboso Job', '284174', 'nyambosojob@gmail.com', '0712354078'),
(15, 'Catherine Job', '284174', 'jobcatherine@gmail.com', '0714450078'),
(16, 'Clake Satanyau', '28476674', 'satanyauclake@gmail.com', '0714090078'),
(17, 'Ouma Othiambo', '284768764', 'othiamboouma@gmail.com', '0714097678'),
(18, 'Kijana Wamua', '2847454', 'wamuakijana@gmail.com', '0718767678'),
(19, 'Job Kondoo', '2840984', 'jobkondoo@gmail.com', '0718712678'),
(20, 'East Nyamira', '284345', 'nyamiraeast@gmail.com', '0718712606'),
(21, 'Wathiambo Njoro', '284345', 'wathiambonjoro@gmail.com', '0718719606');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product_details`
--
ALTER TABLE `product_details`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
