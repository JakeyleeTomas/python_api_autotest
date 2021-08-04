
class TestMaShang:

    # def setup_class(self):
    #     "在每个类之前执行一次，创建日志对象，创建日志对象"
    #
    # def teardown_class(self):
    #     "在每个方法之前执行一次，创建日志对象，创建日志对象"
    #
    # def setup(self):
    #     "在每个方法之前执行一次，创建日志对象，创建日志对象"
    #
    # def teardown(self):
    #     "在每个类之前执行一次，创建日志对象，创建日志对象"
    #
    # # @pytest.mark.usefixtures("")
    # @pytest.mark.users
    def test_baili(self):
        print("baili")
        assert 1 == 1

    # @pytest.mark.smoke
    def test_weiwei(self):
        print("weiwei")
        assert 1 == 1

    def test_xingyao(self):
        print("xingyao")
        assert 1 == 1

#
# @pytest.mark.usefixtures("execute_database_sql")
# class TestAaa():
#     def test_aaa(self):
#         print("aaa")
#
#
# class TestBbb():
#     def test_aaa(self):
#         print("bbb")
