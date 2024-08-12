-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 28 Mar 2024 pada 08.25
-- Versi server: 10.4.24-MariaDB
-- Versi PHP: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbpenjualan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_customer'),
(22, 'Can change user', 6, 'change_customer'),
(23, 'Can delete user', 6, 'delete_customer'),
(24, 'Can view user', 6, 'view_customer'),
(25, 'Can add kategori', 7, 'add_kategori'),
(26, 'Can change kategori', 7, 'change_kategori'),
(27, 'Can delete kategori', 7, 'delete_kategori'),
(28, 'Can view kategori', 7, 'view_kategori'),
(29, 'Can add produk', 8, 'add_produk'),
(30, 'Can change produk', 8, 'change_produk'),
(31, 'Can delete produk', 8, 'delete_produk'),
(32, 'Can view produk', 8, 'view_produk'),
(33, 'Can add transaksi penjualan', 9, 'add_transaksipenjualan'),
(34, 'Can change transaksi penjualan', 9, 'change_transaksipenjualan'),
(35, 'Can delete transaksi penjualan', 9, 'delete_transaksipenjualan'),
(36, 'Can view transaksi penjualan', 9, 'view_transaksipenjualan'),
(37, 'Can add detail transaksi penjualan', 10, 'add_detailtransaksipenjualan'),
(38, 'Can change detail transaksi penjualan', 10, 'change_detailtransaksipenjualan'),
(39, 'Can delete detail transaksi penjualan', 10, 'delete_detailtransaksipenjualan'),
(40, 'Can view detail transaksi penjualan', 10, 'view_detailtransaksipenjualan'),
(41, 'Can add detail transaksi pembelian', 11, 'add_detailtransaksipembelian'),
(42, 'Can change detail transaksi pembelian', 11, 'change_detailtransaksipembelian'),
(43, 'Can delete detail transaksi pembelian', 11, 'delete_detailtransaksipembelian'),
(44, 'Can view detail transaksi pembelian', 11, 'view_detailtransaksipembelian'),
(45, 'Can add transaksi pembelian', 12, 'add_transaksipembelian'),
(46, 'Can change transaksi pembelian', 12, 'change_transaksipembelian'),
(47, 'Can delete transaksi pembelian', 12, 'delete_transaksipembelian'),
(48, 'Can view transaksi pembelian', 12, 'view_transaksipembelian');

-- --------------------------------------------------------

--
-- Struktur dari tabel `core_customer`
--

CREATE TABLE `core_customer` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `last_name` varchar(150) NOT NULL,
  `password` varchar(128) NOT NULL,
  `username` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `core_customer`
--

INSERT INTO `core_customer` (`id`, `name`, `address`, `phone`, `date_joined`, `email`, `first_name`, `is_active`, `is_staff`, `is_superuser`, `last_login`, `last_name`, `password`, `username`) VALUES
(3, 'Ahmad Afandi', 'Dusun Opo opo Lor RT / RW 01/04 Desa Opopo', '082231376068', '2024-03-24 05:55:27.572178', 'samesj4@gmail.com', '', 1, 0, 0, '2024-03-24 05:55:28.197813', '', 'pbkdf2_sha256$260000$7Ix5cBPJzsYjtZiUOWCmqR$BrTAdWpMsOZcNWYGHgXJwWhuEk73VYlcqFI+KDB2Ii4=', 'afandi'),
(4, NULL, NULL, NULL, '2024-03-26 01:15:00.335604', 'admin@example.com', '', 1, 1, 1, '2024-03-28 14:19:03.429003', '', 'pbkdf2_sha256$260000$0aB3cYl4d8fRSlFUbccz8B$Lz2ee5ZCbAe/hwWCU5gW9dmqFWHgwFvY1J7VWzM+7Q4=', 'admin'),
(6, 'Dina', 'Dusun Opo opo Lor RT / RW 01/04 Desa Opopo', '082231376068', '2024-03-26 14:49:56.920123', 'samesj4@gmail.com', '', 1, 0, 0, '2024-03-28 00:03:17.264554', '', 'pbkdf2_sha256$260000$jXSedMs9j9whwPlorfuOR0$GXvHSXW4nKEojLWJ8W+gAdgsRd/IJ7Gg89x9TTZxwTI=', 'dina'),
(7, 'Ahmad Afandi', 'Dusun Opo opo Lor RT / RW 01/04 Desa Opopo', '082231376068', '2024-03-27 13:07:48.880207', 'samesj4@gmail.com', '', 1, 0, 0, '2024-03-27 13:08:34.891815', '', 'pbkdf2_sha256$260000$rNBWGZ4hIUwfpEV9OLZ71C$JaCUpzt3HXcVKQOKKJCtx3wOokyrwLbMrSkRiBac3UM=', 'admin123');

-- --------------------------------------------------------

--
-- Struktur dari tabel `core_customer_groups`
--

CREATE TABLE `core_customer_groups` (
  `id` int(11) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `core_customer_user_permissions`
--

CREATE TABLE `core_customer_user_permissions` (
  `id` int(11) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `core_detailtransaksipembelian`
--

CREATE TABLE `core_detailtransaksipembelian` (
  `id` bigint(20) NOT NULL,
  `jumlah` int(11) DEFAULT NULL,
  `produk_id` bigint(20) DEFAULT NULL,
  `transaksi_pembelian_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `core_detailtransaksipembelian`
--

INSERT INTO `core_detailtransaksipembelian` (`id`, `jumlah`, `produk_id`, `transaksi_pembelian_id`) VALUES
(1, 1, 1, 1),
(2, 3, 2, 1),
(3, 1, 1, 2),
(4, 1, 1, 3),
(5, 2, 2, 3),
(6, 3, 3, 3),
(7, 1, 1, 4),
(8, 2, 2, 4),
(9, 3, 3, 4),
(10, 2, 2, 5),
(11, 1, 1, 6),
(12, 2, 2, 6),
(13, 3, 3, 6),
(14, 1, 1, 7),
(15, 2, 2, 7),
(16, 3, 3, 7),
(17, 1, 1, 8),
(18, 2, 2, 8),
(19, 3, 3, 8),
(20, 0, 1, 9),
(21, 0, 2, 9),
(22, 0, 3, 9),
(23, 1, 1, 10),
(24, 2, 2, 10),
(25, 3, 3, 10),
(26, 1, 1, 11),
(27, 3, 3, 11),
(28, 0, 1, 12),
(29, 0, 2, 12),
(30, 3, 1, 13),
(31, 3, 2, 13),
(32, 3, 1, 14),
(33, 6, 2, 14),
(34, 2, 3, 14),
(35, 100, 3, 15),
(36, 1, 2, 15);

-- --------------------------------------------------------

--
-- Struktur dari tabel `core_detailtransaksipenjualan`
--

CREATE TABLE `core_detailtransaksipenjualan` (
  `id` bigint(20) NOT NULL,
  `jumlah` int(11) DEFAULT NULL,
  `produk_id` bigint(20) DEFAULT NULL,
  `transaksi_penjualan_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `core_detailtransaksipenjualan`
--

INSERT INTO `core_detailtransaksipenjualan` (`id`, `jumlah`, `produk_id`, `transaksi_penjualan_id`) VALUES
(3, 100, 1, 3),
(4, 450, 2, 3),
(7, 201, 3, 5),
(8, 300, 1, 5),
(9, 170, 3, 6),
(10, 110, 1, 6),
(11, 200, 1, 7),
(12, 276, 1, 8),
(13, 332, 2, 8),
(14, 400, 3, 8),
(15, 143, 1, 9),
(16, 432, 3, 9),
(17, 212, 2, 10);

-- --------------------------------------------------------

--
-- Struktur dari tabel `core_kategori`
--

CREATE TABLE `core_kategori` (
  `id` bigint(20) NOT NULL,
  `nama` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `core_kategori`
--

INSERT INTO `core_kategori` (`id`, `nama`) VALUES
(1, 'Makanan'),
(2, 'Minuman'),
(7, 'Snack'),
(8, 'Sembako');

-- --------------------------------------------------------

--
-- Struktur dari tabel `core_produk`
--

CREATE TABLE `core_produk` (
  `id` bigint(20) NOT NULL,
  `nama_produk` varchar(200) DEFAULT NULL,
  `gambar_produk` varchar(100) DEFAULT NULL,
  `harga_beli` int(11) DEFAULT NULL,
  `harga_jual` int(11) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `kategori_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `core_produk`
--

INSERT INTO `core_produk` (`id`, `nama_produk`, `gambar_produk`, `harga_beli`, `harga_jual`, `stock`, `kategori_id`) VALUES
(1, 'ayam goreng', 'gambar/banner/654a25a73f416.jpg', 10000, 12000, 94, 1),
(2, 'Es Teh', 'gambar/banner/es_teh.jpg', 2000, 3000, 16, 2),
(3, 'Keripik Pisang', 'gambar/banner/Ekspor-Keripik-Singkong-Dari-Indonesia-1024x576.jpg', 2000, 5000, 195, 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `core_transaksipembelian`
--

CREATE TABLE `core_transaksipembelian` (
  `id` bigint(20) NOT NULL,
  `no_transaksi` varchar(200) DEFAULT NULL,
  `nama_suplayer` varchar(200) DEFAULT NULL,
  `total_transaksi` bigint(20) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `date_created` datetime(6) DEFAULT NULL,
  `tanggal_kulakan` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `core_transaksipembelian`
--

INSERT INTO `core_transaksipembelian` (`id`, `no_transaksi`, `nama_suplayer`, `total_transaksi`, `status`, `date_created`, `tanggal_kulakan`) VALUES
(1, 'Pb-0001', 'afandi', NULL, 'Baru', '2024-03-26 12:13:53.666660', '2024-03-26 00:00:00.000000'),
(2, 'Pb-0002', 'same', NULL, 'Baru', '2024-03-26 12:18:03.978228', '2024-03-27 00:00:00.000000'),
(3, 'Pb-0002', 'same', NULL, 'Baru', '2024-03-26 12:18:35.128527', '2024-03-27 00:00:00.000000'),
(4, 'Pb-0004', 'same', NULL, 'Baru', '2024-03-26 12:19:37.332526', '2024-03-27 00:00:00.000000'),
(5, 'Pb-0005', 'same', NULL, 'Baru', '2024-03-26 12:23:36.983150', '2024-03-26 00:00:00.000000'),
(6, 'Pb-0006', 'same', NULL, 'Baru', '2024-03-26 12:24:15.259825', '2024-03-26 00:00:00.000000'),
(7, 'Pb-0007', 'same', NULL, 'Baru', '2024-03-26 12:25:05.442287', '2024-03-26 00:00:00.000000'),
(8, 'Pb-0008', 'adsfsdf', NULL, 'Baru', '2024-03-26 13:38:52.256734', '2024-03-27 00:00:00.000000'),
(9, 'Pb-0009', 'afandi', NULL, 'Baru', '2024-03-26 13:43:32.075738', '2024-03-26 00:00:00.000000'),
(10, 'Pb-0010', 'adsfsdf', NULL, 'Baru', '2024-03-26 13:47:16.710636', '2024-03-26 00:00:00.000000'),
(11, 'Pb-0011', 'afandi', NULL, 'Baru', '2024-03-26 13:48:00.995653', '2024-03-27 00:00:00.000000'),
(12, 'Pb-0012', 'afandi', NULL, 'Baru', '2024-03-26 13:48:51.758825', '2024-03-27 00:00:00.000000'),
(13, 'Pb-0013', 'afandi', NULL, 'Baru', '2024-03-26 13:54:13.523639', '2024-03-27 00:00:00.000000'),
(14, 'Pb-0014', 'afandi', NULL, 'Baru', '2024-03-26 13:54:53.325142', '2024-03-27 00:00:00.000000'),
(15, 'Pb-0015', 'afandi', NULL, 'Baru', '2024-03-26 14:55:55.375901', '2024-03-26 00:00:00.000000');

-- --------------------------------------------------------

--
-- Struktur dari tabel `core_transaksipenjualan`
--

CREATE TABLE `core_transaksipenjualan` (
  `id` bigint(20) NOT NULL,
  `no_transaksi` varchar(200) DEFAULT NULL,
  `total_transaksi` bigint(20) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `date_created` datetime(6) DEFAULT NULL,
  `tanggal_penjualan` datetime(6) DEFAULT NULL,
  `customer_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `core_transaksipenjualan`
--

INSERT INTO `core_transaksipenjualan` (`id`, `no_transaksi`, `total_transaksi`, `status`, `date_created`, `tanggal_penjualan`, `customer_id`) VALUES
(3, 'PJ-3', 150000, 'Baru', '2024-03-06 17:35:48.129134', '2024-01-06 17:35:48.129134', 3),
(5, 'PJ-3', 46000, 'Baru', '2024-03-26 14:50:35.244563', '2024-01-26 14:50:35.189709', 6),
(6, 'PJ-3', 217000, 'Baru', '2024-03-27 13:08:17.705549', '2024-01-27 13:08:17.700052', 7),
(7, 'PJ-4', 24000, 'Baru', '2024-03-27 22:21:25.456548', '2024-01-27 22:21:25.455550', 6),
(8, 'PJ-5', 65000, 'Baru', '2024-03-27 23:57:17.989310', '2024-02-27 23:57:17.987289', 6),
(9, 'PJ-6', 17000, 'Baru', '2024-03-27 23:58:04.810812', '2024-03-27 23:58:04.809814', 6),
(10, 'PJ-7', 3000, 'Baru', '2024-03-28 00:03:36.867756', '2024-03-28 00:03:36.866793', 6);

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(6, 'core', 'customer'),
(11, 'core', 'detailtransaksipembelian'),
(10, 'core', 'detailtransaksipenjualan'),
(7, 'core', 'kategori'),
(8, 'core', 'produk'),
(12, 'core', 'transaksipembelian'),
(9, 'core', 'transaksipenjualan'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'core', '0001_initial', '2024-03-23 15:48:29.954597'),
(2, 'contenttypes', '0001_initial', '2024-03-23 15:48:30.484179'),
(3, 'admin', '0001_initial', '2024-03-23 15:48:32.977249'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-03-23 15:48:33.048408'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-03-23 15:48:33.080322'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-03-23 15:48:34.074750'),
(7, 'auth', '0001_initial', '2024-03-23 15:48:37.185426'),
(8, 'auth', '0002_alter_permission_name_max_length', '2024-03-23 15:48:37.982294'),
(9, 'auth', '0003_alter_user_email_max_length', '2024-03-23 15:48:38.136879'),
(10, 'auth', '0004_alter_user_username_opts', '2024-03-23 15:48:38.184752'),
(11, 'auth', '0005_alter_user_last_login_null', '2024-03-23 15:48:38.242597'),
(12, 'auth', '0006_require_contenttypes_0002', '2024-03-23 15:48:38.289473'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2024-03-23 15:48:38.341334'),
(14, 'auth', '0008_alter_user_username_max_length', '2024-03-23 15:48:38.385224'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2024-03-23 15:48:38.441066'),
(16, 'auth', '0010_alter_group_name_max_length', '2024-03-23 15:48:38.581689'),
(17, 'auth', '0011_update_proxy_permissions', '2024-03-23 15:48:38.642527'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2024-03-23 15:48:38.683417'),
(19, 'core', '0002_customer_address_customer_phone', '2024-03-23 15:48:38.911807'),
(20, 'core', '0003_alter_customer_options_alter_customer_managers_and_more', '2024-03-23 15:48:44.696146'),
(21, 'sessions', '0001_initial', '2024-03-23 15:48:45.605711'),
(22, 'core', '0004_detailtransaksipembelian_transaksipembelian', '2024-03-25 20:09:48.516189');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0fjmbewau1j8rzgtcdpykwe16cr7c9oh', '.eJxVjz0OwyAMRu_CHKFAgIaO3XuGyGBo_hqkAFOUuxekDOliyf6en-yDDJDTOOTo9mFC8iScNPeZAbu4rQY4w_YJ1IYt7ZOhFaFXGuk7oFtfF_snGCGOZdtiz50w2kuBoKW0oBCt90JyqXqlQJsHdMoz2zOntOfegzAd56i5skwU6eJ22OoR5HkQVsucvysUO29IzCaFBGtpRNu2Z1MeuRHsTnQVOM8f5KtRkA:1rnxYw:tVxfzTMISLdryIS_Lj4tukI7BHjhCI2rjhsqSL10RUY', '2024-04-06 16:21:14.831541'),
('40k4u4ahbhzpwk2ic45rgdfkrd43656k', '.eJxVjDsOwjAQRO_iGllxvPGHkj5niNbeDQkQW8qnQtwdW0oB5cy8eW8x4LFPw7HxOswkrgLE5bcLGJ-c6kAPTPcsY077OgdZEXmum-wz8et2sn-CCbepvBXGbvTakANt0AYHTJogjE2JjjhytCM4H8FR65T1yndtY0ygBlSrQ5FWXcKFiw1pmZP4fAFQQD4J:1rpk2R:3vKTdrYOgKQEA25lJcLJI-KUJ6J3zWgMgVkRNnfKrbQ', '2024-04-11 14:19:03.463928'),
('fywx9tuxiqrqd9g7m9k5vxm082gte45b', '.eJxVjDEOwjAMRe-SGUWqm5iEkZ0zVI4dkwJKpaadKu4OlTrA-t97fzMDrUsZ1pbnYRRzMWBOv1sifua6A3lQvU-Wp7rMY7K7Yg_a7G2S_Loe7t9BoVa-NUuA7FJU74Si90wowqrOg8eASDGdqUftOHQZo4IqudQDSATkzpn3BwfXOHg:1rnx7F:Idm8rcDkCd5Wq63B--s5nw2s42-ZICv3RsFKsgFRGBM', '2024-04-06 15:52:37.824802'),
('lnqwuwfilbp4zrt05qdm2ws4j84b990e', '.eJxVjDsOwjAQRO_iGllxvPGHkj5niNbeDQkQW8qnQtwdW0oB5cy8eW8x4LFPw7HxOswkrgLE5bcLGJ-c6kAPTPcsY077OgdZEXmum-wz8et2sn-CCbepvBXGbvTakANt0AYHTJogjE2JjjhytCM4H8FR65T1yndtY0ygBlSrQ5FWXcKFiw1pmZP4fAFQQD4J:1rpMT4:Oi_3lU3OTXAc7nocFrcnRF-B3iS21tPKCyGGupkf3Sw', '2024-04-10 13:08:58.692639');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indeks untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indeks untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indeks untuk tabel `core_customer`
--
ALTER TABLE `core_customer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indeks untuk tabel `core_customer_groups`
--
ALTER TABLE `core_customer_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `core_customer_groups_customer_id_group_id_dafb5506_uniq` (`customer_id`,`group_id`),
  ADD KEY `core_customer_groups_group_id_da90e5e6_fk_auth_group_id` (`group_id`);

--
-- Indeks untuk tabel `core_customer_user_permissions`
--
ALTER TABLE `core_customer_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `core_customer_user_permi_customer_id_permission_i_7eccb269_uniq` (`customer_id`,`permission_id`),
  ADD KEY `core_customer_user_p_permission_id_45563430_fk_auth_perm` (`permission_id`);

--
-- Indeks untuk tabel `core_detailtransaksipembelian`
--
ALTER TABLE `core_detailtransaksipembelian`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_detailtransaksi_produk_id_3d4415df_fk_core_prod` (`produk_id`),
  ADD KEY `core_detailtransaksi_transaksi_pembelian__f81a8a93_fk_core_tran` (`transaksi_pembelian_id`);

--
-- Indeks untuk tabel `core_detailtransaksipenjualan`
--
ALTER TABLE `core_detailtransaksipenjualan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_detailtransaksi_produk_id_308234ad_fk_core_prod` (`produk_id`),
  ADD KEY `core_detailtransaksi_transaksi_penjualan__6c007219_fk_core_tran` (`transaksi_penjualan_id`);

--
-- Indeks untuk tabel `core_kategori`
--
ALTER TABLE `core_kategori`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `core_produk`
--
ALTER TABLE `core_produk`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_produk_kategori_id_ce0e4a17_fk_core_kategori_id` (`kategori_id`);

--
-- Indeks untuk tabel `core_transaksipembelian`
--
ALTER TABLE `core_transaksipembelian`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `core_transaksipenjualan`
--
ALTER TABLE `core_transaksipenjualan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_transaksipenjualan_customer_id_cc9c7ae9_fk_core_customer_id` (`customer_id`);

--
-- Indeks untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_core_customer_id` (`user_id`);

--
-- Indeks untuk tabel `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indeks untuk tabel `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT untuk tabel `core_customer`
--
ALTER TABLE `core_customer`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `core_customer_groups`
--
ALTER TABLE `core_customer_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `core_customer_user_permissions`
--
ALTER TABLE `core_customer_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `core_detailtransaksipembelian`
--
ALTER TABLE `core_detailtransaksipembelian`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT untuk tabel `core_detailtransaksipenjualan`
--
ALTER TABLE `core_detailtransaksipenjualan`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT untuk tabel `core_kategori`
--
ALTER TABLE `core_kategori`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `core_produk`
--
ALTER TABLE `core_produk`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `core_transaksipembelian`
--
ALTER TABLE `core_transaksipembelian`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT untuk tabel `core_transaksipenjualan`
--
ALTER TABLE `core_transaksipenjualan`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT untuk tabel `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ketidakleluasaan untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ketidakleluasaan untuk tabel `core_customer_groups`
--
ALTER TABLE `core_customer_groups`
  ADD CONSTRAINT `core_customer_groups_customer_id_bc34f3ce_fk_core_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `core_customer` (`id`),
  ADD CONSTRAINT `core_customer_groups_group_id_da90e5e6_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ketidakleluasaan untuk tabel `core_customer_user_permissions`
--
ALTER TABLE `core_customer_user_permissions`
  ADD CONSTRAINT `core_customer_user_p_customer_id_81424fc8_fk_core_cust` FOREIGN KEY (`customer_id`) REFERENCES `core_customer` (`id`),
  ADD CONSTRAINT `core_customer_user_p_permission_id_45563430_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Ketidakleluasaan untuk tabel `core_detailtransaksipembelian`
--
ALTER TABLE `core_detailtransaksipembelian`
  ADD CONSTRAINT `core_detailtransaksi_produk_id_3d4415df_fk_core_prod` FOREIGN KEY (`produk_id`) REFERENCES `core_produk` (`id`),
  ADD CONSTRAINT `core_detailtransaksi_transaksi_pembelian__f81a8a93_fk_core_tran` FOREIGN KEY (`transaksi_pembelian_id`) REFERENCES `core_transaksipembelian` (`id`);

--
-- Ketidakleluasaan untuk tabel `core_detailtransaksipenjualan`
--
ALTER TABLE `core_detailtransaksipenjualan`
  ADD CONSTRAINT `core_detailtransaksi_produk_id_308234ad_fk_core_prod` FOREIGN KEY (`produk_id`) REFERENCES `core_produk` (`id`),
  ADD CONSTRAINT `core_detailtransaksi_transaksi_penjualan__6c007219_fk_core_tran` FOREIGN KEY (`transaksi_penjualan_id`) REFERENCES `core_transaksipenjualan` (`id`);

--
-- Ketidakleluasaan untuk tabel `core_produk`
--
ALTER TABLE `core_produk`
  ADD CONSTRAINT `core_produk_kategori_id_ce0e4a17_fk_core_kategori_id` FOREIGN KEY (`kategori_id`) REFERENCES `core_kategori` (`id`);

--
-- Ketidakleluasaan untuk tabel `core_transaksipenjualan`
--
ALTER TABLE `core_transaksipenjualan`
  ADD CONSTRAINT `core_transaksipenjualan_customer_id_cc9c7ae9_fk_core_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `core_customer` (`id`);

--
-- Ketidakleluasaan untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_core_customer_id` FOREIGN KEY (`user_id`) REFERENCES `core_customer` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
