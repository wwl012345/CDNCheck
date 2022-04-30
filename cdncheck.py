import sys
import getopt
import re
import random
import requests

banner = '''
                                                                                               
                               ,--.                          ,--,                         ,--. 
  ,----..     ,---,          ,--.'|          ,----..       ,--.'|   ,---,. ,----..    ,--/  /| 
 /   /   \  .'  .' `\    ,--,:  : |         /   /   \   ,--,  | : ,'  .' |/   /   \,---,': / ' 
|   :     ,---.'     \,`--.'`|  ' :        |   :     ,---.'|  : ,---.'   |   :     :   : '/ /  
.   |  ;. |   |  .`\  |   :  :  | |        .   |  ;. |   | : _' |   |   ..   |  ;. |   '   ,   
.   ; /--`:   : |  '  :   |   \ | :        .   ; /--`:   : |.'  :   :  |-.   ; /--`'   |  /    
;   | ;   |   ' '  ;  |   : '  '; |        ;   | ;   |   ' '  ; :   |  ;/;   | ;   |   ;  ;    
|   : |   '   | ;  .  '   ' ;.    ;        |   : |   '   |  .'. |   :   .|   : |   :   '   \   
.   | '___|   | :  |  |   | | \   |        .   | '___|   | :  | |   |  |-.   | '___|   |    '  
'   ; : .''   : | /  ;'   : |  ; .'        '   ; : .''   : |  : '   :  ;/'   ; : .''   : |.  \ 
'   | '/  |   | '` ,/ |   | '`--'          '   | '/  |   | '  ,/|   |    '   | '/  |   | '_\.' 
|   :    /;   :  .'   '   : |              |   :    /;   : ;--' |   :   .|   :    /'   : |     
 \   \ .' |   ,.'     ;   |.'               \   \ .' |   ,/     |   | ,'  \   \ .' ;   |,'     
  `---`   '---'       '---'                  `---`   '---'      `----'     `---`   '---'       
                                                                             --by 想走安全的小白
'''

def ping(domain):
    # 开始进行多地ping检测
    print("[+] {}域名正在进行CDN检测".format(domain))
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; "
    }

    #查询时需要callback参数，将其中的一些值做成了列表
    callback_list = [
        "jQuery11130026963948833894413_1645520722094",
        "jQuery11130026963948833894413_1645520722095",
        "jQuery11130026963948833894413_1645520722096",
        "jQuery11130026963948833894413_1645520722097",
        "jQuery11130026963948833894413_1645520722098",
        "jQuery11130026963948833894413_1645520722099",
        "jQuery11130026963948833894413_1645520722100",
    ]

    #站长之家节点列表
    #国内节点列表
    node_list1 = {
        "浙江杭州[电信]": "278d10bf-cbc5-494a-bbab-e76c05b4f3cd",
        "福建泉州[电信]": "bfc066b6-e917-4a60-88c6-d646154b1cf5",
        "辽宁沈阳[多线]": "07f2f1cc-8414-4557-a8c1-27750a732f16",
        "江西南昌[电信]": "e4f581f3-0d6c-4ce3-b9d4-1e4fdfc99c1f",
        "安徽合肥[移动]": "fc778772-3967-4b70-be93-9045f310e16c",
        "广东佛山[电信]": "0ae10bfa-b5da-4e31-80e7-da9be7490840",
        "天津[联通]": "9365c01e-163f-4f07-b569-a9302b685c30",
        "河南新乡[多线]": "ea551b59-2609-4ab4-89bc-14b2080f501a",
        "黑龙江哈尔滨[联通]": "2805fa9f-05ea-46bc-8ac0-1769b782bf52",
        "安徽合肥[联通]": "66426ad9-99d9-471f-b55f-c270cc3fc878",
        "浙江扬州[多线]": "4a40427f-502e-4a85-8752-980f2d8bbae1",
        "广东东莞[电信]": "cd4e7631-8427-41b6-8e44-869a70a04b20",
        "山东济南[联通]": "4d7637d7-4950-4b79-9741-c397789bcf05",
        "辽宁大连[电信]": "e1d5b78f-6ba5-485d-a4dd-54dc546b991a",
        "上海[多线]": "a936bb02-6b19-4da5-9c82-e8bb68fcfbea",
        "北京[多线]": "463cd3ff-65cb-4b5a-8c77-555ef43b6612",
        "内蒙古呼和浩特[多线]": "8c0b720b-e1a1-4422-a948-e8d7ec7e4906",
        "山东枣庄[联通]_1": "9e980285-f696-4478-a645-fc1e5a76ed47",
        "江苏徐州[电信]": "92dad4c3-9bc3-4f71-a0b0-db9376613bb2",
        "湖北十堰[电信]": "0003d32b-8585-4480-b0ea-dd0a10768dd2",
        "新疆哈密[电信]": "9bc90d67-d208-434d-b680-294ae4288571",
        "云南昆明[电信]": "14ef4fcf-3712-4971-9c24-0d1657751022",
        "中国香港_1": "cdcf3a45-8366-4ab4-ae80-75eb6c1c9fca",
        "中国香港_2": "a0be885d-24ad-487d-bbb0-c94cd02a137d",
        "中国台湾": "483bad95-d9a8-4026-87f4-7a56501bf5fd",
    }

    #国外节点列表
    node_list2 = {
        "韩国CN2": "1f4c5976-8cf3-47e7-be10-aa9270461477",
        "韩国CN联通_1": "dc440a55-1148-480f-90a7-9d1e0269b682",
        "韩国CN联通_2": "6cd2450a-d73d-40c7-96ce-afc20540eeea",
        "美国_1": "737831b4-95e1-445f-a981-c1333faf88bd",
        "美国高防": "9d45ea23-5a13-4b89-8b56-85cc183c3e67",
        "德国": "d9041619-7d90-42ea-9811-2b2fe11cb2b0",
        "荷兰": "08117724-8437-4ebb-88ae-93e50f660867",
        "英国": "2cf34de5-74b1-406d-a735-0b4d96c52480",
        "新加坡": "6bdfa30f-f80a-4816-9aa1-a8b32d9fbdda",
        "俄罗斯": "0e215450-a287-486e-b758-49b00e432bd4",
    }

    ip_value = ""
    for n in node_list1.keys():
        try:
            url = "https://ping.chinaz.com/iframe.ashx?t=ping&callback={}".format(random.choice(callback_list))
            data = "guid={}&host={}&ishost=0&isipv6=0&encode=g4LFw6M5ZZa9pkSC|tGN8JBHp|lHVl2x&checktype=0".format(node_list1[n], domain)
            res = requests.post(url=url, headers=headers, data=data, verify=True)
            res_node = res.text
            node_value = re.findall("\({(.*?)}\)", res_node, re.S)
            if len(node_value[0]) == 14:
                print("[-] {}节点检测超时".format(n))
            else:
                print("[+] {}节点正在检测中...".format(n))
                ip_value += node_value[0]
        except Exception as e:
            print('[-] {} 节点请求失败'.format(n))
            continue
    set_ip1 = set(re.findall("ip:'(.*?)',", ip_value, re.S))

    for n in node_list2.keys():
        try:
            url = "https://ping.chinaz.com/iframe.ashx?t=ping&callback={}".format(random.choice(callback_list))
            data = "guid={}&host={}&ishost=0&isipv6=0&encode=g4LFw6M5ZZa9pkSC|tGN8JBHp|lHVl2x&checktype=0".format(node_list2[n], domain)
            res = requests.post(url=url, headers=headers, data=data, verify=True)
            res_node = res.text
            node_value = re.findall("\({(.*?)}\)", res_node, re.S)
            if len(node_value[0]) == 14:
                print("[-] {}节点检测超时".format(n))
            else:
                print("[+] {}节点正在检测中...".format(n))
                ip_value += node_value[0]
        except Exception as e:
            print('[-] {} 节点请求失败'.format(n))
            continue
    set_ip2 = set(re.findall("ip:'(.*?)',", ip_value, re.S))

    if len(set_ip1) > 1 or len(set_ip2) > 1:
        print("[-] 经检测{}可能使用CDN加速，请进一步判断真实IP")
        str1 = "[-] 经检测{}可能使用CDN加速，请进一步判断真实IP"
        with open('result.txt', 'a+') as file:  # 设置文件对象
            file.write(str1)  # 将字符串写入文件中
    elif len(set_ip1) == 1 or len(set_ip2) == 1:
        if len(set_ip1) == 1:
            print("[+] 经检测{}国内未使用CDN加速，可能的真实IP为：{}\n".format(domain, ",".join(set_ip1)))
            str2 = "[+] 经检测{}国内未使用CDN加速，可能的真实IP为：{}\n".format(domain, ",".join(set_ip1))
        else:
            print("[+] 经检测{}国外未使用CDN加速，真实IP可能为：{}\n".format(domain, ",".join(set_ip2)))
            str2 = "[+] 经检测{}国外未使用CDN加速，真实IP可能为：{}\n".format(domain, ",".join(set_ip2))
        with open('result.txt', 'a+') as file:  # 设置文件对象
            file.write(str2)  # 将字符串写入文件中
    else:
        print('站长之家网站请求失败，请检查网络配置')

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], '-h-u-f', ['help', 'url=', 'filename='])
        for opt_name, opt_value in opts:
            if opt_name in ('-h', '--help'):
                print(banner)
                print("对单个域名进行cdn检测")
                print("python3 cndcheck.py -u domain")
                print("python3 cndcheck.py --url domain\n")
                print("对多个域名进行cdn检测")
                print("python3 cndcheck.py -f url.txt")
                print("python3 cndcheck.py --filename url.txt\n")
                exit()
            if opt_name in ('-u', '--url'):
                print(banner)
                domain = sys.argv[2]
                ping(domain)
                exit()
            if opt_name in ('-f', '--filename'):
                print(banner)
                for line in open(sys.argv[2]):
                    domain = line.strip()
                    ping(domain)
                exit()
    except Exception as e:
        print(banner)
        print("参数错误，请使用-h或--help参数查看帮助")
        exit()