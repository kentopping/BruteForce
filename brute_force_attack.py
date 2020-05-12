#!/usr/bin/env python
import argparse
import brute_force



def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Enter the target URL")
    parser.add_argument("-e", "--email", dest="email", help="Enter your email")
    parser.add_argument("-p", "--password", dest="password", help="Enter your password")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify the URL, use --help for more info")
    if not options.email:
        parser.error("[-] Please specify the attackers email, use --help for more info")
    if not options.password:
        parser.error("[-] Please specify the email password, use --help for more info")
    return options


options = parse()
target = options.target
email = options.email
password = options.password

brute_force_attack = brute_force.Brute(target, email, password)
brute_force_attack.attack()