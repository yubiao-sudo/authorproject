import os
import yaml


class read_yaml:
    def __init__(self, dir_filename, yaml_filename):
        self.dir_name = dir_filename
        self.yml_filename = yaml_filename

    # 读取yaml文件
    def read_yml(self):
        Common_dir = os.path.dirname(os.path.abspath(__file__))
        print(Common_dir)
        sec_dir = os.path.join(Common_dir, 'flie_yaml')
        # Ro_Pc_dir = os.path.dirname(Common_dir)
        # print(sec_dir)
        Ele_dir = os.path.join(sec_dir, self.dir_name)
        # print(Ele_dir)
        Ele_dir_yaml = os.path.join(Ele_dir, self.yml_filename)
        # print(Ele_dir_yaml)
        try:
            with open(Ele_dir_yaml, 'r', encoding='utf-8') as f_yaml:
                return yaml.load(f_yaml, Loader=yaml.FullLoader)
        except Exception as e:
            raise e


if __name__ == '__main__':
    # 测试
    r = read_yaml('ele_yaml', 'page_index.yaml')
    data = r.read_yml()
    print(data)
