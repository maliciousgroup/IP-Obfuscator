import ipaddress
import random

from colorama import Style, Fore

red = Fore.RED
cyan = Fore.CYAN
yellow = Fore.YELLOW

bold = Style.BRIGHT
reset = Style.RESET_ALL


class Obfuscation:

    def __init__(self, ip: ipaddress.IPv4Address):
        self.ip = ip
        self.intro()

    @staticmethod
    def intro():
        _credits = f'''

██╗██████╗      ██████╗ ██████╗ ███████╗██╗   ██╗███████╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗ 
██║██╔══██╗    ██╔═══██╗██╔══██╗██╔════╝██║   ██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║██████╔╝    ██║   ██║██████╔╝█████╗  ██║   ██║███████╗██║     ███████║   ██║   ██║   ██║██████╔╝
██║██╔═══╝     ██║   ██║██╔══██╗██╔══╝  ██║   ██║╚════██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
██║██║         ╚██████╔╝██████╔╝██║     ╚██████╔╝███████║╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝╚═╝          ╚═════╝ ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                   
{bold}{cyan}[*] Author: d3d (@MaliciousGroup){reset}
        '''
        print(_credits)

    def obfuscate(self):
        octets = self.ip.__str__().split('.')
        print(f"{bold}{yellow}[+] Obfuscation Layer 1) Decimal, Hexadecimal and Octal Representation{reset}")
        print(f"{'Decimal:':<30}{int(self.ip)}")
        print(f"{'Hexadecimal:':<30}{hex(int(self.ip))}")
        print(f"{'Octal:':<30}{oct(int(self.ip)).replace('o', '0')}")
        hex_parts = []
        hex_rand = ""
        oct_parts = []
        oct_rand = ""
        for octet in octets:
            hex_parts.append(hex(int(octet)))
            oct_parts.append(oct(int(octet)).replace('o', '0'))
        print(f"\n{bold}{yellow}[+] Obfuscation Layer 2) Hexadecimal and Octal with Random Padding{reset}")
        for i in hex_parts:
            hex_rand += i.replace('0x', '0x' + '0' * random.randint(1, 30)) + '.'
        print(f"{'Random Hex Padding:':<30}{hex_rand}".rstrip('.'))
        for i in oct_parts:
            oct_rand += '0' * random.randint(1, 30) + i + '.'
        print(f"{'Random Oct Padding:':<30}{oct_rand}".rstrip('.'))
        count = 0
        print(f"\n{bold}{yellow}[+] Obfuscation Layer 3) Random Radix with Random Padding{reset}")
        while count < 5:
            rand_baseval = ""
            for i in range(0, 4):
                val = random.randint(0, 2)
                if val == 0:
                    rand_baseval += octets[i] + '.'
                elif val == 1:
                    rand_baseval += hex_parts[i].replace('0x', '0x' + '0' * random.randint(1, 30)) + '.'
                else:
                    rand_baseval += '0' * random.randint(1, 30) + oct_parts[i] + '.'
            print(f"{'Random Base Padding:':<30}{rand_baseval}".rstrip('.'))
            count += 1


def usage():
    print(f"\n{bold}[*] Usage:{reset}")
    print(f"python3 {yellow}{argv[0]}{reset} <ip address>\n")


if __name__ == '__main__':
    from sys import argv

    if len(argv) != 2:
        usage()
        exit(code=1)
    try:
        _ip = ipaddress.IPv4Address(argv[1])
        obfs = Obfuscation(_ip)
        obfs.obfuscate()
    except ValueError:
        print(f"{bold}{red}{argv[1]} is not a valid IPv4 Address.{reset}")
        usage()
        exit(code=2)
