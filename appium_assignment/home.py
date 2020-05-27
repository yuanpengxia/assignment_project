
import pytest
class TestHome:
    def setup(self):
        pass
    def teardown(self):
        pass
    def test_search(self):
        print("热门币种搜索：")
    def test_notice(self):
        print("公告：")
    def test_personal_centor(self):
        print("个人中心：")
    def test_rise_list(self):
        print("热搜榜：")
        pytest.assume(1 == 2)
        pytest.assume(1 == 1)
        pytest.assume(1 == 3)


if __name__ == '__main__':
    pytest.main("-v -x TestHome::test_rise_list")