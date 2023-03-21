-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 08-Mar-2023 às 21:31
-- Versão do servidor: 5.7.36
-- versão do PHP: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `projeto`
--

DELIMITER $$
--
-- Procedimentos
--
DROP PROCEDURE IF EXISTS `Producao`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `Producao` ()  NO SQL
    DETERMINISTIC
SELECT tb1.id_prod,tb1.initial_date,tb1.final_date,SUM(tb2.quantidade) FROM producao tb1 INNER JOIN materiais_producao tb2 on tb1.id_prod = tb2.id_prod GROUP BY tb1.id_prod$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `cargos`
--

DROP TABLE IF EXISTS `cargos`;
CREATE TABLE IF NOT EXISTS `cargos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(25) NOT NULL,
  `desc` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=660 DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `cargos`
--

INSERT INTO `cargos` (`id`, `nome`, `desc`) VALUES
(465, 'Presidente', '\'\''),
(659, 'Gerente', '\'\'');

-- --------------------------------------------------------

--
-- Estrutura da tabela `grupos`
--

DROP TABLE IF EXISTS `grupos`;
CREATE TABLE IF NOT EXISTS `grupos` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `grupos`
--

INSERT INTO `grupos` (`id`, `nome`) VALUES
(45, 'Administrador'),
(68, 'Manutençao');

-- --------------------------------------------------------

--
-- Estrutura da tabela `materiais`
--

DROP TABLE IF EXISTS `materiais`;
CREATE TABLE IF NOT EXISTS `materiais` (
  `id_mat` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `tipo_id` int(11) NOT NULL,
  PRIMARY KEY (`id_mat`),
  KEY `tipo_id` (`tipo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `materiais`
--

INSERT INTO `materiais` (`id_mat`, `nome`, `tipo_id`) VALUES
(1235, 'Material Danificado', 4),
(3256, 'Base Metal', 3),
(3265, 'Tampa verde', 2),
(4568, 'Tampa Metal', 2),
(5698, 'Base Azul', 3),
(6328, 'Base Verde', 3),
(6548, 'Caixa Verde', 1),
(9746, 'Tampa Azul', 2),
(9864, 'Caixa Metal', 1),
(9875, 'Caixa Azul', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `materiais_producao`
--

DROP TABLE IF EXISTS `materiais_producao`;
CREATE TABLE IF NOT EXISTS `materiais_producao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_prod` int(11) NOT NULL,
  `id_mat` int(11) NOT NULL,
  `quantidade` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_mat` (`id_mat`),
  KEY `id _prod` (`id_prod`)
) ENGINE=InnoDB AUTO_INCREMENT=552 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `materiais_producao`
--

INSERT INTO `materiais_producao` (`id`, `id_prod`, `id_mat`, `quantidade`) VALUES
(549, 1678310898, 3256, 0),
(550, 1678310898, 5698, 0),
(551, 1678310898, 6328, 0);

-- --------------------------------------------------------

--
-- Estrutura da tabela `mat_tipo`
--

DROP TABLE IF EXISTS `mat_tipo`;
CREATE TABLE IF NOT EXISTS `mat_tipo` (
  `tipo_id` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`tipo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `mat_tipo`
--

INSERT INTO `mat_tipo` (`tipo_id`, `nome`) VALUES
(1, 'Caixa'),
(2, 'Tampa'),
(3, 'Base'),
(4, 'Rejeito');

-- --------------------------------------------------------

--
-- Estrutura da tabela `producao`
--

DROP TABLE IF EXISTS `producao`;
CREATE TABLE IF NOT EXISTS `producao` (
  `id_prod` int(11) NOT NULL,
  `initial_date` datetime NOT NULL,
  `final_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_prod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `producao`
--

INSERT INTO `producao` (`id_prod`, `initial_date`, `final_date`) VALUES
(1678310898, '2023-03-08 18:28:18', NULL);

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `senha` text NOT NULL,
  `cargo` int(11) NOT NULL,
  `grupo` int(11) NOT NULL,
  `img_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cargo` (`cargo`),
  KEY `grupo` (`grupo`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `nome`, `senha`, `cargo`, `grupo`, `img_name`) VALUES
(45, 'hugo', '$2b$12$x2h.XnYrZJFnSj2ByUf0iemvdWRgBjFtNxytqrxHXu7m859zNHUZO', 659, 45, 'aaa'),
(46, 'Hugo Rodrigo', '$2b$12$KQ3MUpz4DD7GHB28ceYluO/Aya2dujqdFkh9NLuKffKeJGL9gsZFy', 465, 45, 'padrao.jpeg'),
(47, 'a', '$2b$12$mBvL4Bl5wKoJdYPxR9U3nue9MdOjOvFX6AbjJry4OKOhgfHbqCP0y', 465, 68, 'padrao.jpeg'),
(48, 's', '$2b$12$mBvL4Bl5wKoJdYPxR9U3nud2YtMo7SCP.S8Vsr4RD8FtiABQSjJhW', 465, 68, 'padrao.jpeg'),
(49, 'd', '$2b$12$.dqqDWqFZ2UYOMlodbEZdOWny62E5q.M1ebK.V7v1pMVTlpN/3.Nq', 465, 45, 'padrao.jpeg'),
(50, 'a', '$2b$12$JbE/99uc/QIp8k1q943X1.3L3d7LmZcLghASzHMz/pMH0C/b4nSsK', 465, 45, 'padrao.jpeg'),
(51, 'b', '$2b$12$JbE/99uc/QIp8k1q943X1.eMDy2IyfoGrpQxQg/0OKhqgFdpjJ8Sy', 465, 45, 'padrao.jpeg'),
(52, 'daila', '$2b$12$oGmd7nkZSGAJSJYc/26ufu4kpNYc71xvvwwP2V5plSPCy0H64Mayy', 465, 45, 'padrao.jpeg');

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `materiais`
--
ALTER TABLE `materiais`
  ADD CONSTRAINT `tipo_id` FOREIGN KEY (`tipo_id`) REFERENCES `mat_tipo` (`tipo_id`);

--
-- Limitadores para a tabela `materiais_producao`
--
ALTER TABLE `materiais_producao`
  ADD CONSTRAINT `materiais_producao_ibfk_1` FOREIGN KEY (`id_mat`) REFERENCES `materiais` (`id_mat`),
  ADD CONSTRAINT `materiais_producao_ibfk_2` FOREIGN KEY (`id_prod`) REFERENCES `producao` (`id_prod`);

--
-- Limitadores para a tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`cargo`) REFERENCES `cargos` (`id`),
  ADD CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`grupo`) REFERENCES `grupos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
