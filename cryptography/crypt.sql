-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 21, 2021 at 05:39 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crypt`
--

-- --------------------------------------------------------

--
-- Table structure for table `friend_list`
--

CREATE TABLE `friend_list` (
  `s_no` int(11) NOT NULL,
  `user_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `friend` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `friend_list`
--

INSERT INTO `friend_list` (`s_no`, `user_id`, `friend`) VALUES
(4, 'prince', 'roshan'),
(5, 'roshan', 'prince'),
(6, 'prince', 'cat'),
(7, 'cat', 'prince'),
(8, 'cat', 'roshan'),
(9, 'roshan', 'cat');

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `s_no` int(11) NOT NULL,
  `sender` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `receiver` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `mssg` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `message`
--

INSERT INTO `message` (`s_no`, `sender`, `receiver`, `mssg`) VALUES
(17, 'roshan', 'prince', '62464865233104f1772e11df9450e6273963b0ac3624071d7896a7b4479fcc415d030a2642e00ab013f1858f7277df4489cf868831397f8bdf22e02b8bdec668'),
(18, 'roshan', 'prince', '162373444806619912120d968915f3317038e3f944244e5734d787da2efca9615d09116a4cb21bf803edd0e60157af36e0a1e5ed114a16e5b743c045e2bda348'),
(19, 'prince', 'cat', '8ea7a4801d42a92dc571741aa3ea0d9a459996caeec87800e46fa312385070a5464bd6e2d6060030c46bd7f0ae704803d353780296c89c6f477d9b4248f59667'),
(20, 'cat', 'prince', '8ea3a1ec7262cb44a91d011aa3ea0d9a459996caeec87800e46fa312385070a5464fd38eb9266259a807a2f0ae704803d353780296c89c6f477d9b4248f59667'),
(21, 'prince', 'roshan', '62485645424361d10e4164df9450e6273963b0ac3624071d7896a7b4479fcc415d0d140623926f906a9ef08f7277df4489cf868831397f8bdf22e02b8bdec668'),
(22, 'prince', 'cat', '8ea3a1ec7262cb44a91d011aa3ea0d9a459996caeec87800e46fa312385070a5464fd38eb9266259a807a2f0ae704803d353780296c89c6f477d9b4248f59667');

-- --------------------------------------------------------

--
-- Table structure for table `request`
--

CREATE TABLE `request` (
  `s_no` int(11) NOT NULL,
  `user_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `request_to` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `request`
--

INSERT INTO `request` (`s_no`, `user_id`, `request_to`) VALUES
(6, 'roshan', 'mall'),
(7, 'cat', 'mall'),
(8, 'cat', 'rambhu');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `s_no` int(11) NOT NULL,
  `user_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `email_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `path` varchar(256) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `public_key` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`s_no`, `user_id`, `email_id`, `path`, `user_name`, `public_key`) VALUES
(20, 'sanjay', 'sanjay@123', 'C:/Users/PRINCE SINHA/cryptography/static/hidden_image/sanjay.png', 'sanjay', '3132409349'),
(21, 'prince', 'prince@gmail.com', 'C:/Users/PRINCE SINHA/cryptography/static/hidden_image/prince.png', 'prince', '2513340380'),
(22, 'roshan', 'roshan@gmail.com', 'C:/Users/PRINCE SINHA/cryptography/static/hidden_image/roshan.png', 'Roshan', '1556859708'),
(23, 'cat', 'cat@gmail.com', 'C:/Users/PRINCE SINHA/cryptography/static/hidden_image/cat.png', 'billu', '1424290014'),
(24, 'rambhu', 'rambhu@gmail.com', 'C:/Users/PRINCE SINHA/cryptography/static/hidden_image/rambhu.png', 'Rambhu Devi Sinha', '1152051601'),
(25, 'mall', 'mall@pheonix', 'C:/Users/PRINCE SINHA/cryptography/static/hidden_image/mall.png', 'phenoix', '2396649231');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `friend_list`
--
ALTER TABLE `friend_list`
  ADD PRIMARY KEY (`s_no`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`s_no`);

--
-- Indexes for table `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`s_no`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`s_no`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD UNIQUE KEY `email_id` (`email_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `friend_list`
--
ALTER TABLE `friend_list`
  MODIFY `s_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `message`
--
ALTER TABLE `message`
  MODIFY `s_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `request`
--
ALTER TABLE `request`
  MODIFY `s_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `s_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
