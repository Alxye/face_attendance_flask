/*
 Navicat Premium Data Transfer

 Source Server         : 阿里云ECS
 Source Server Type    : MySQL
 Source Server Version : 80032 (8.0.32-0ubuntu0.20.04.2)
 Source Host           : 101.132.152.202:3306
 Source Schema         : wechat

 Target Server Type    : MySQL
 Target Server Version : 80032 (8.0.32-0ubuntu0.20.04.2)
 File Encoding         : 65001

 Date: 27/03/2023 20:57:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for attendance
-- ----------------------------
DROP TABLE IF EXISTS `attendance`;
CREATE TABLE `attendance`  (
  `staff_id` int NOT NULL,
  `date` date NOT NULL,
  `salary` int NULL DEFAULT 0,
  `am_type` int NULL DEFAULT NULL COMMENT '0-未打卡 1-打卡 2-异常',
  `pm_type` int NULL DEFAULT NULL COMMENT '0-未打卡 1-打卡 2-异常',
  `clock_in_time` datetime NULL DEFAULT NULL,
  `clock_out_time` datetime NULL DEFAULT NULL,
  `am_address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `pm_address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`staff_id`, `date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of attendance
-- ----------------------------
INSERT INTO `attendance` VALUES (1, '2023-03-27', 0, 2, 0, '2023-03-27 10:48:35', NULL, '东南大学苏州研究院', '');
INSERT INTO `attendance` VALUES (2, '2023-03-23', 0, 2, 1, '2023-03-23 13:28:54', '2023-03-23 17:34:30', '', '东南大学苏州研究院');
INSERT INTO `attendance` VALUES (3, '2023-03-24', 0, 0, 0, NULL, NULL, '', '');
INSERT INTO `attendance` VALUES (8, '2023-03-24', 0, 0, 1, NULL, '2023-03-24 18:20:15', '', '东南大学苏州研究院');
INSERT INTO `attendance` VALUES (8, '2023-03-27', 0, 0, 1, NULL, '2023-03-27 20:10:32', '', '东南大学苏州研究院');
INSERT INTO `attendance` VALUES (1116, '2022-12-01', NULL, 2, 2, '2023-03-22 10:00:00', '2023-03-22 16:06:00', NULL, NULL);
INSERT INTO `attendance` VALUES (1116, '2023-03-02', NULL, 1, 1, '2023-03-02 09:02:00', '2023-03-02 13:03:00', NULL, NULL);
INSERT INTO `attendance` VALUES (1116, '2023-03-18', NULL, 1, 2, '2023-03-21 09:00:00', '2023-03-21 16:06:00', NULL, NULL);
INSERT INTO `attendance` VALUES (1116, '2023-03-19', NULL, 0, 1, '2023-03-21 10:00:00', '2023-03-21 16:06:00', NULL, NULL);
INSERT INTO `attendance` VALUES (1116, '2023-03-20', NULL, 1, 1, '2023-03-21 10:00:00', '2023-03-21 16:06:00', NULL, NULL);
INSERT INTO `attendance` VALUES (1116, '2023-03-21', NULL, 1, 1, '2023-03-21 10:00:00', '2023-03-21 16:06:00', NULL, NULL);
INSERT INTO `attendance` VALUES (1699, '2023-03-24', 0, 0, 1, NULL, '2023-03-24 17:42:37', '', '东南大学苏州研究院');
INSERT INTO `attendance` VALUES (1699, '2023-03-27', 0, 0, 0, NULL, NULL, '', '');
INSERT INTO `attendance` VALUES (1992, '2023-03-23', 0, 0, 0, NULL, NULL, '', '');
INSERT INTO `attendance` VALUES (1992, '2023-03-24', 0, 0, 0, NULL, NULL, '', '');
INSERT INTO `attendance` VALUES (7411, '2023-03-24', 0, 0, 2, NULL, '2023-03-24 14:49:08', '', '东南大学苏州研究院');
INSERT INTO `attendance` VALUES (9446, '2023-03-24', 0, 0, 2, NULL, '2023-03-24 14:06:28', '', '东南大学苏州研究院');
INSERT INTO `attendance` VALUES (12138, '2023-03-23', 0, 1, 1, '2023-03-23 05:53:54', '2023-03-23 14:18:44', '', '东南大学苏州研究院');
INSERT INTO `attendance` VALUES (12138, '2023-03-24', 0, 0, 1, NULL, '2023-03-24 15:00:02', '', '东南大学苏州研究院');
INSERT INTO `attendance` VALUES (12138, '2023-03-27', 0, 1, 0, '2023-03-27 09:48:07', NULL, '东南大学苏州研究院', '');

-- ----------------------------
-- Table structure for attendance_appeal
-- ----------------------------
DROP TABLE IF EXISTS `attendance_appeal`;
CREATE TABLE `attendance_appeal`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `staff_id` int NULL DEFAULT NULL,
  `date` date NULL DEFAULT NULL,
  `appeal_reason` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `state` int NULL DEFAULT NULL,
  `reject_reason` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `time_state` int NULL DEFAULT NULL COMMENT '0-上午 1-下午',
  `category` int NULL DEFAULT NULL COMMENT '0-打卡失败 1-打卡异常',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 41 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of attendance_appeal
-- ----------------------------
INSERT INTO `attendance_appeal` VALUES (1, 12138, '2023-03-23', '23号上班补卡', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (2, 12138, '2023-03-23', '23号上班补卡', 1, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (3, 12138, '2023-03-23', '上班补卡', 0, NULL, 0, 0);
INSERT INTO `attendance_appeal` VALUES (4, 12138, '2023-03-23', '上班补卡', 0, NULL, 1, 0);
INSERT INTO `attendance_appeal` VALUES (5, 12138, '2023-03-22', '22_23', 1, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (6, 12138, '2023-03-23', '22_23', 1, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (7, 12138, '2023-03-23', '22_23', 2, 'f-ing', 1, 1);
INSERT INTO `attendance_appeal` VALUES (8, 12138, '2023-03-23', '111', 2, 'f-ing', 0, 1);
INSERT INTO `attendance_appeal` VALUES (9, 12138, '2023-03-23', '111', 2, 'f-ing', 1, 1);
INSERT INTO `attendance_appeal` VALUES (10, 6, '2023-03-13', '', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (11, 6, '2023-03-13', '', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (12, 6, '2023-03-14', '', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (13, 6, '2023-03-14', '', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (14, 6, '2023-03-15', '', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (15, 6, '2023-03-15', '', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (16, 6, '2023-03-16', '', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (17, 6, '2023-03-16', '', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (18, 6, '2023-03-17', '', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (19, 6, '2023-03-17', '', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (20, 6, '2023-03-18', '', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (21, 6, '2023-03-18', '', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (22, 6, '2023-03-19', '', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (23, 6, '2023-03-19', '', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (24, 12138, '2023-03-23', '11111', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (25, 12138, '2023-03-19', '11111', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (26, 12138, '2023-03-20', '11111', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (27, 12138, '2023-03-24', '打卡', 0, NULL, 0, 0);
INSERT INTO `attendance_appeal` VALUES (28, 1992, '2023-03-24', 'kkk', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (29, 1992, '2023-03-24', 'kkk', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (30, 9446, '2023-03-24', '识别失败', 0, NULL, 1, 0);
INSERT INTO `attendance_appeal` VALUES (31, 7411, '2023-03-24', '', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (32, 7411, '2023-03-24', '', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (33, 7411, '2023-03-24', '', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (34, 7411, '2023-03-24', '', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (35, 7411, '2023-03-24', '', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (36, 7411, '2023-03-24', '', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (37, 8, '2023-03-24', '1537738484849', 0, NULL, 1, 0);
INSERT INTO `attendance_appeal` VALUES (38, 1699, '2023-03-24', '上午忘记打卡', 0, NULL, 0, 1);
INSERT INTO `attendance_appeal` VALUES (39, 1699, '2023-03-24', '上午忘记打卡', 0, NULL, 1, 1);
INSERT INTO `attendance_appeal` VALUES (40, 1699, '2023-03-27', '人类识别不成功', 0, NULL, 0, 0);

-- ----------------------------
-- Table structure for corporation
-- ----------------------------
DROP TABLE IF EXISTS `corporation`;
CREATE TABLE `corporation`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `notice` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `address` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of corporation
-- ----------------------------
INSERT INTO `corporation` VALUES (1, '重在参与', '派大星和海绵宝宝一起...捉水母！！！', '北京市朝阳县');

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department`  (
  `department_id` int NOT NULL AUTO_INCREMENT,
  `department_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `notice` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `clock_in_start` time NULL DEFAULT NULL,
  `clock_in_end` time NULL DEFAULT NULL,
  `clock_out_start` time NULL DEFAULT NULL,
  `clock_out_end` time NULL DEFAULT NULL,
  `longitude` float NULL DEFAULT NULL,
  `latitude` float NULL DEFAULT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`department_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO `department` VALUES (1, '开发部', '📢公告：请在打卡时间内进行打卡，上班（下班）打卡时间段之后（之前）1小时属于迟到（早退），其余时间禁止打卡！', '09:00:00', '11:59:59', '17:00:00', '18:59:59', 120.751, 31.2701, '江苏省苏州市苏州工业园区枕典巷');
INSERT INTO `department` VALUES (2, '服务中心', '📢notice：缺人ing！！！', '00:00:00', '23:59:59', '00:00:00', '23:59:59', 120.747, 31.2692, '江苏省苏州市苏州工业园区林泉街');
INSERT INTO `department` VALUES (3, '人事处', '📢公告：请在打卡时间内进行打卡，上班（下班）打卡时间段之后（之前）1小时属于迟到（早退），其余时间禁止打卡！', '09:00:00', '09:59:59', '15:00:00', '18:59:59', 120.746, 31.2704, '江苏省苏州市苏州工业园区林泉街与文景路交叉口正南方向152米');
INSERT INTO `department` VALUES (4, '未来发展中心', '📢公告：请在打卡时间内进行打卡，上班（下班）打卡时间段之后（之前）1小时属于迟到（早退），其余时间禁止打卡！', '08:00:00', '09:59:59', '15:14:50', '18:59:59', 120.751, 31.2694, '江苏省苏州市苏州工业园区枕典巷');
INSERT INTO `department` VALUES (5, '管理中心', '📢公告：请在打卡时间内进行打卡，上班（下班）打卡时间段之后（之前）1小时属于迟到（早退），其余时间禁止打卡！', '09:00:00', '09:59:59', '21:00:00', '21:59:59', 120.745, 31.2701, '江苏省苏州市苏州工业园区林泉街399号');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `staff_id` int NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `age` int NULL DEFAULT NULL,
  `type` int NULL DEFAULT NULL,
  `reg_time` datetime NULL DEFAULT NULL,
  `login_time` bigint NULL DEFAULT NULL,
  `department_id` int NULL DEFAULT NULL,
  `face_info` blob NULL,
  `openid` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`, `staff_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 53 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 1112, 'pbkdf2:sha256:260000$Yep1WFwoxQBGFYLw$01893e14883831141e9a938d61bd429d8b81cc604215d92477fd8d06e98e097b', 'new', 12, 2, NULL, 1679919705, 1, NULL, NULL);
INSERT INTO `user` VALUES (2, 1299, 'pbkdf2:sha256:260000$hvVu1ZpZTtY7tJwO$1d67c7add13fc9f9f6a61d2391859ea60870815f71c046cbd80c31b5f4fbd27e', 'new', 0, 2, '2023-03-23 11:54:36', 1679885265, 2, NULL, NULL);
INSERT INTO `user` VALUES (3, 1114, 'pbkdf2:sha256:260000$0mUWax2ABcufs53v$56e2ff2723f3e4af9c7cac13718e686aea2090c778df0a12910f6f90b42021e2', 'new', 0, 1, '2023-03-23 11:56:31', NULL, 2, NULL, NULL);
INSERT INTO `user` VALUES (4, 1115, 'pbkdf2:sha256:260000$raDgHmYRUsuqBwAo$b1b446dc2dde1126d90b691d70838178de410f61a847b3cad3144800ae54646f', 'new', 12, 1, '2023-03-23 13:04:35', NULL, 1, NULL, NULL);
INSERT INTO `user` VALUES (5, 1116, 'pbkdf2:sha256:260000$recQBwER7QHwzFNT$c64b7ae520a2d5ab538f456f03ad75b6949e87e683280bfd11a834f5f60f89f3', 'zx', 12, 1, '2023-03-23 13:06:51', NULL, 1, NULL, NULL);
INSERT INTO `user` VALUES (6, 1117, 'pbkdf2:sha256:260000$zkeJAxyPDjHmAHOP$5df780605d495465f2222509e4b57faba5dd79b26abac55c107a5dc4d07212e3', 'zx', 12, 1, '2023-03-23 13:14:08', NULL, 1, NULL, NULL);
INSERT INTO `user` VALUES (7, 1119, 'pbkdf2:sha256:260000$ZWghNTupmYpe2mow$acf0bc4043185b89b3417349142dd0bd4fcf608be52121dfef37a19fcae987e3', 'new', 0, 3, '2023-03-23 13:14:41', NULL, 1, NULL, NULL);
INSERT INTO `user` VALUES (11, 7410, '123456', NULL, NULL, 2, NULL, NULL, 2, NULL, NULL);
INSERT INTO `user` VALUES (18, 1120, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (19, 1121, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (20, 1122, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (21, 1123, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (22, 1124, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (23, 1125, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (24, 1126, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (25, 1127, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (26, 1128, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (27, 1129, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (28, 1130, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (29, 1140, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (30, 1139, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (31, 1138, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (32, 1137, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (33, 1136, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (34, 1135, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (35, 1134, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (36, 1133, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');
INSERT INTO `user` VALUES (37, 1132, 'pbkdf2:sha256:260000$vqoWebnQL95XjeGT$6a564c9e57b9cb08317b33cfd446bbf3a8b0d6a947903ca9f845788c03aadbbe', 'z', 12, 1, '2023-03-24 09:05:29', NULL, 1, NULL, '');

SET FOREIGN_KEY_CHECKS = 1;
