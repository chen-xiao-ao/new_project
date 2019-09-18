import allure


class TestJenkins(object):

    @allure.step('测试步骤')
    def test_01(self):
        allure.attach('附件名称', '附件中内容')
        assert True
