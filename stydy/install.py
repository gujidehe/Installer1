# 引入模块
import glob
import time
import os

# 定义全局变量
devices_list_finally = []
file_list_finally = []
chose_file_num = []
package_name_list = ['com.yqxue.yqxue', 'com.yiqizuoye.jzt']
old_file_list = []
d = {}
new_d = {}
new_file_list = []
packages_list_finally = []


# 卸载应用
# def uninstall_apk():
#     for uninstall_package_to_devices_index in range(len(devices_list_finally)):
#         for package_name in package_name_list:
#             print('adb -s' + ' '+ devices_list_finally[uninstall_package_to_devices_index] + ' ' + 'uninstall' + ' ' + package_name)
#             os.system('adb -s' + ' '+ devices_list_finally[uninstall_package_to_devices_index] + ' ' + 'uninstall' + ' ' + package_name)

# 安装应用
# 卸载APP
def uninstall_apk():
    print('请选择要卸载的APP:''\n'
          '1.' + package_name_list[0] + '\n' +
          '2.' + package_name_list[1] + '\n' +
          '3.卸载所有APP''\n'
          '4.都不卸载''\n'
          '========================================================================================')
    a = int(input('请输入你的选择：'))
    for uninstall_package_to_devices_index in range(len(devices_list_finally)):
        if a == 1:
            print('adb -s' + ' ' + devices_list_finally[uninstall_package_to_devices_index] + ' ' + 'uninstall' + ' ' +
                  package_name_list[a - 1])
            os.system(
                'adb -s' + ' ' + devices_list_finally[uninstall_package_to_devices_index] + ' ' + 'uninstall' + ' ' +
                package_name_list[a - 1])
        elif a == 2:
            print('adb -s' + ' ' + devices_list_finally[uninstall_package_to_devices_index] + ' ' + 'uninstall' + ' ' +
                  package_name_list[a - 1])
            os.system(
                'adb -s' + ' ' + devices_list_finally[uninstall_package_to_devices_index] + ' ' + 'uninstall' + ' ' +
                package_name_list[a - 1])
        elif a == 3:
            for package_name in package_name_list:
                print('adb -s' + ' ' + devices_list_finally[
                    uninstall_package_to_devices_index] + ' ' + 'uninstall' + ' ' + package_name)
                os.system('adb -s' + ' ' + devices_list_finally[
                    uninstall_package_to_devices_index] + ' ' + 'uninstall' + ' ' + package_name)
        elif a == 4:
            break
        else:
            print('输入错误')


# 安装APP
def install_apk(chose_file_num):
    for install_apk_to_devices_index in range(len(devices_list_finally)):
        print('adb -s' + ' ' + devices_list_finally[install_apk_to_devices_index] + ' ' + 'install' + ' ' +
              file_list_finally[chose_file_num])
        os.system('adb -s' + ' ' + devices_list_finally[install_apk_to_devices_index] + ' ' + 'install' + ' ' +
                  file_list_finally[chose_file_num])
    clear_packageDate()


# 检查本地文件是否存在
def check_local_file():
    file_list = glob.glob('C:\\Users\\thinkpad\\Downloads\\*.apk')
    for file_name in file_list:
        timestamp = os.path.getctime(file_name)
        d[timestamp] = file_name
        old_file_list.append(timestamp)
    for i in sorted(old_file_list):
        new_d[i] = d[i]
        new_file_list.append(new_d[i])
    # print (file_list)
    file_index = len(new_file_list)
    if file_index != 0:
        # print('%s, %d' %(file_list, file_index))
        if file_index == 1:
            print('one local file''\n'
                  '========================================================================================')
            install_apk()
        elif file_index > 1:
            print('========================================================================================''\n'
                  'PLEASE chose one apk that you want to install')
            for file_num in range(file_index):
                # print('file_num=',file_num)
                file_list_finally.append(new_file_list[file_num])
                print('%d: %s ' % (file_num + 1, new_file_list[file_num]))  # 打印apk列表
                # print(file_list_finally)
            chose_file = input('Enter num to chose apk:>>')
            # print(type(chose_file))
            try:
                chose_file_num = int(chose_file)
                if type(chose_file_num) is int:
                    chose_file_num = chose_file_num - 1
                    print('正在安装：')
                    install_apk(chose_file_num)
                else:
                    print('your enter is err,please check it...')
                    # check_local_file()
            except ValueError:
                print('you enter vslue is err,please check it.. ')
                time.sleep(3)
                clear_packageDate()
    else:
        print('Can not find local file. plase check local file...')


# 检查是否有设备连接PC
def check_devices_link():
    devices_list_start = []
    devices_cmd = os.popen('adb devices').readlines()
    devices_list_start_count = len(devices_cmd)
    devices_list_start_count = devices_list_start_count - 2
    # print('devices_cmd=',devices_cmd)
    # print(devices_list_start_count)
    if devices_list_start_count >= 1:
        print('查找到的本机已连接设备')
        for devices_num in range(devices_list_start_count):
            # print('devices_num=',devices_num)
            devices_list_start.append(devices_cmd[devices_num + 1])
            # print(devices_list_start)
            device_list_pers = devices_list_start[devices_num].index('\t')
            # print(device_list_pers)
            devices_list_finally.append(devices_list_start[devices_num][:device_list_pers])
            print('devices list :' + '%d  ' % (devices_num + 1) + '%s' % devices_list_finally[devices_num])
            # print(type(devices_list_finally))
        print('========================================================================================')
        uninstall_apk()
        check_local_file()
    else:
        print('没有找到设备，请链接设备！''\n'
              '========================================================================================')


# 清空应用数据
def clear_packageDate():
    print('开始清理数据''\n'
          '========================================================================================')
    for clear_packageDate_to_devices_index in range(len(devices_list_finally)):
        packages_list_all = os.popen('adb -s' + ' ' + devices_list_finally[
            clear_packageDate_to_devices_index] + ' ' + 'shell pm list packages').readlines()  # 获取应用列表
        # print('adb -s'+' '+devices_list_finally[clear_packageDate_to_devices_index]+' '+'shell pm list packages')
        # print('packages_list_all:',packages_list_all)
        for package_num in range(len(packages_list_all)):
            # print('package_num:::',package_num)
            # 筛出包名
            packages_list_pers1 = packages_list_all[package_num].index(':')  # 定位冒号位置
            packages_list_pers2 = packages_list_all[package_num].index('\n')  # 定位换行位置
            packages_list_finally.append(packages_list_all[package_num][packages_list_pers1 + 1:packages_list_pers2])
        for package_name in package_name_list:
            if package_name in packages_list_finally:
                print('adb -s' + ' ' + devices_list_finally[
                    clear_packageDate_to_devices_index] + ' ' + 'shell pm clear' + ' ' + package_name)
                os.system('adb -s' + ' ' + devices_list_finally[
                    clear_packageDate_to_devices_index] + ' ' + 'shell pm clear' + ' ' + package_name)
            else:
                break


check_devices_link()
os.system('pause')
