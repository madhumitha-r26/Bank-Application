# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 18:14:00 2025

@author: Madhumitha
"""

class Bank:
    def __init__(self):
        self.current_amount=0
        
    def getvalues(self):
        print("------- ENTER YOUR DETAILS ----------")
        self.name=input("Enter Name:")
        self.acc_num=int(input("Enter Account Number:"))
        self.acc_type=input("Enter Account Type:")


    def deposit(self):
        self.deposit_amount=int(input("Enter Deposit Amount:"))
        self.current_amount+=self.deposit_amount
        

    def withdraw(self):
        self.withdraw_amount=int(input("Enter Withdraw Amount:"))
        if(self.withdraw_amount<self.current_amount):
            self.current_amount-=self.withdraw_amount
        else:
            print("Your balance is low!")
        
    def show_balance(self):
        self.current_amount=self.current_amount
        print("Current Balance:",self.current_amount) 
        
        
    def display(self):
        print("------------DETAILS--------------")
        print("Name:",self.name)   
        print("Account-Number:",self.acc_num)   
        print("Account-Type:",self.acc_type)   
        print("Current Balance:",self.current_amount)  
        
        
b=Bank()

while(True):
    print("-------BANK APPLICATION----------")
    print("1. Getting Details")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Displaying Details")
    print("5. Show Current Balance")
    print("6. Quit")

    ch=int(input("Enter your choice:"))
    if(ch==1):
        b.getvalues()
    elif(ch==2):
        b.deposit()
    elif(ch==3):
        b.withdraw()
    elif(ch==4):
        b.display()   
    elif(ch==5):
        b.show_balance()   
    elif(ch==6):
        print("Thank you and have a nice day!")
        break
    else:
        print("Invalid Option")
      