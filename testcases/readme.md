备注
数据量大的时候，且数据排序没有固定规律，很难获取到对应的值时可以使用jsonpath

pip install r requirements.txt  安装requirements.txt文件内所有第三方库

pytest.ini配置文件的参数说明
-vs -v打印详细信息 -s 打印调试信息
-n  -n表示多线程运行
--reruns  失败用例重跑
--html=路径  生产html的报告
-m 执行带标记的用例
addopts = -vs --reruns 2 --html=./reports/report.html
addopts = -vs -m "users or smoke"
testpaths = ./testcases
python_files = mashang_*.py
python_classes =Test*
python_functions = test*
markers =
    smoke:冒烟测试
    users:用户管理模块
控制执行顺序
@pytest.mark.run(order=1)
一万个用例中只有三个用例需要前置条件 需要连接数据库 改如何操作 fixture实现部门用例的前后置

@pytest.fixture(scope="function")
def execute_database_sql():
    print("连接数据库")
    yield
    print("断开数据库")

class TestMaShang:
    def test_baili(self, execute_database_sql):
        print("baili")
        assert 1 == 1

    def test_weiwei(self):
        print("weiwei")
        assert 1 == 1

    def test_xingyao(self):
        print("xingyao")
        assert 1 == 1
