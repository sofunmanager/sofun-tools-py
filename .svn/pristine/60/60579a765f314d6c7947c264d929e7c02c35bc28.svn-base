import configparser
import os


class INI_Tools:
    path="config/"
    
    def get(section,option:str=None,file:str='config.ini'):
        config = configparser.ConfigParser()
        try:
            config.read(INI_Tools.path+file)
            if(config.has_section(section)):
                if(option):
                    if(config.has_option(section,option)):
                        return config.get(section,option)
                    else:
                        return None
                else:
                    return config.items(section)
            else:
                return None
        except FileNotFoundError:
            # 文件不存在的处理逻辑
            print("INI文件不存在")
            return None

    def set(section,option,value,file:str='config.ini'):
        config = configparser.ConfigParser()
        os.makedirs(INI_Tools.path, exist_ok=True)
        fileName=INI_Tools.path+file
        config.read(fileName)


        if not config.has_section(section):
            config.add_section(section)

        config.set(section, option,value)

        with open(fileName, 'w') as configfile:
            config.write(configfile)



# print(INI_Tools.set("USER_CONFIG","token","123123123"))
print(INI_Tools.get("USER_CONFIG","token"))