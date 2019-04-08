import pytest


class TestBase:

    @pytest.mark.possitive
    def test_login(self, pm, user):
        pm.login_page.open() \
            .enter_email(user.email()) \
            .enter_pass(user.password()) \
            .click_login_btn()
        pm.home_page.click_my_account_btn()
        first_name = pm.account_page.get_first_name()
        last_name = pm.account_page.get_last_name()
        email = pm.account_page.get_email()
        assert email == user.email()
        assert first_name == "alex"
        assert last_name == "zh"
