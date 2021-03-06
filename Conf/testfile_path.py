
import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

#测试数据的路径
test_data_path = os.path.join(base_dir, 'Testdata', 'case_data.xlsx')

#测试结果的路径
test_result_path = os.path.join(base_dir, 'Testdata', 'result_test.xls')

#日志路径
log_path = os.path.join(base_dir, 'Log')

#测试报告路径
report_path = os.path.join(base_dir, 'HtmlTestReport')

#用例配置文件的路径
case_conf_path = os.path.join(base_dir, 'Conf', 'case.conf')

#邮箱的配置文件的路径
email_conf_path = os.path.join(base_dir, 'Conf', 'email.cof')

#数据库的ip地址
mysql_conf_path = os.path.join(base_dir, 'Conf', 'mysql.conf')


