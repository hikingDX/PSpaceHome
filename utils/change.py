class ChangeUtils:
    @classmethod
    def get_phontname_by_num(cls, num):
        if num == 0:
            return 'Android手机'
        elif num == 1:
            return 'iOS手机'
        elif num == 2:
            return 'Android平板'
        elif num == 3:
            return 'iOS平板'

    @classmethod
    def get_testresult_by_num(cls, num):
        if num == 0:
            return '等待脚本测试'
        elif num == 1:
            return '测试成功'
        elif num == 2:
            return '测试失败'
