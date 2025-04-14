import csv
import math
from colorama import Fore, Back, Style
from datetime import datetime,timedelta
import colorama
from termcolor import colored


colorama.init()


class restaurant_name:
    def __init__(self, name, rating,X,Y):
        self.name = name
        self.rating = rating
        self.X = X
        self.Y = Y
        

class restaurant:
    def __init__(self):
        self.items = [
            restaurant_name("Spice Garden",  1.9,  -13.34,  14.56),
    restaurant_name("Curry Palace",  3.0,  14.43,  10.86),
    restaurant_name("Tandoori Treats",  1.7,  -0.02,  -0.52),
    restaurant_name("Masala Magic",  1.3,  -8.65,  -2.77),
    restaurant_name("Bollywood Bites",  4.0,  -7.03,  -2.18),
    restaurant_name("Saffron Spice",  3.3,  -6.93,  -9.92),
    restaurant_name("Mughal Mahal",  4.7,  5.38,  -2.16),
    restaurant_name("Royal Rasoi",  3.4,  -4.96,  -1.8),
    restaurant_name("Chaat Corner",  2.2,  3.21,  3.89),
    restaurant_name("Desi Dhaba",  2.2,  2.36,  6.19),
    restaurant_name("Flavors of India",  1.4,  1.75,  -2.85),
    restaurant_name("Namaste Kitchen",  0.9,  -2.83,  -11.26),
    restaurant_name("Zaika",  2.8,  2.89,  -3.87),
    restaurant_name("Rangoli",  4.5,  1.28,  -4.93),
    restaurant_name("Biryani House",  3.8,  -3.64,  -2.44),
    restaurant_name("Kebab Factory",  4.8,  4.47,  -14.54),
    restaurant_name("Indian Essence",  5.8,  -4.89,  -4.38),
    restaurant_name("Curry Leaf",  4.2,  -6.46,  -8.92),
    restaurant_name("Maharaja",  2.3,  -7.97,  -1.41),
    restaurant_name("Annapurna",  1.6,  -8.38,  -4.86),
    restaurant_name("Taste of India",  2.4,  -9.12, 11.12)]
        



class delievery_boy:
    def __init__(self, name,number, X,Y):
        self.name = name
        self.number = number
        self.X = X
        self.Y = Y
        
class boy_LIST:
    def __init__(self):
        self.items = [
            delievery_boy("Reyansh Thakur", "+917865500000", -1.45, -1.00),
            delievery_boy("Shaurya Mehta","+916760000000", 14.56, -1.10),
    delievery_boy("Harsh Singh", "+917656500000", -13.25,-7.02),
    delievery_boy("Nikhil Bansal", "+916283100000", 4.43,  2.50),
    delievery_boy("Rajesh Bansal", "+916855300000", -12.03,  4.18),
    delievery_boy("Kartik Mehta", "+916029000000",  10.88,  0.27),
    delievery_boy("Dhruv Gupta", "+917220200000", 0.53,  14.76),
    delievery_boy("Aditya Thakur", "+917065900000", -2.07,  13.21),
    delievery_boy("Krishna Patel", "+919719400000", 7.36,  12.19),
    delievery_boy("Aarav Tripathi", "+918899100000",  -4.86,  11.48),
    delievery_boy("Shaurya Desai", "+916478700000",  -7.39,  10.89),
    delievery_boy("Aarav Thakur", "+919789300000",  -8.24,  9.77),
    delievery_boy("Nikhil Joshi", "+916584400000",  -9.32,  8.11),
    delievery_boy("Vivaan Thakur", "+916198400000",  -11.95,  7.18),
    delievery_boy("Om Joshi", "+919393100000",  -12.87,  6.40),
    delievery_boy("Dhruv Thakur", "+918720800000",  -14.97,  5.41),
    delievery_boy("Aditya Kumar", "+916059000000",  1.46,  4.63),
    delievery_boy("Krishna Gupta", "+916205500000",  2.56,  3.79),
    delievery_boy("Reyansh Reddy", "+916760000000",  3.56,  2.10),
    delievery_boy("Om Mishra", "+917656500000",  4.25,  1.02),
    delievery_boy("Aryan Gupta", "+917007600000",  5.50,  0.11),
    delievery_boy("Reyansh Malhotra", "+917134500000",  6.18,  -14.75),
    delievery_boy("Aarav Mishra", "+916892900000",  7.27,  -13.87),
    delievery_boy("Aditya Malhotra", "+918568600000",  8.76,  -12.53),
    delievery_boy("Krishna Malhotra", "+917186300000",  9.21,  -11.89),
    delievery_boy("Shaurya Tripathi", "+916921600000",  10.19,  -10.96),
    delievery_boy("Aarav Nair", "+917084300000",  11.16,  -9.83),
    delievery_boy("Rohan Mehta", "+917979900000",  12.66,  -8.38),
    delievery_boy("Atharv Bhatia", "+916097100000",  13.93,  -7.59),
    delievery_boy("Arjun Chopra", "+918624100000",  14.61,  -6.47),
    delievery_boy("Vivaan Jain", "+917642700000",  -4.89,  -5.38),
    delievery_boy("Om Nair", "+917778800000",  -1.80,  -4.97),
    delievery_boy("Rohan Patel", "+918309300000",  4.32,  -3.46),
    delievery_boy("Sai Gupta", "+916205500000",  2.56,  -2.79),
    delievery_boy("Reyansh Thakur", "+917865500000",  -1.45,  -1.00)
        ]

class dishes:
    def __init__(self, name):
        self.name = name

class Menu:
    def __init__(self):
        self.items = [
    dishes("Chilly Paneer"),
    dishes("Tandoori Chicken"),
    dishes("Kadhai Paneer"),
    dishes("Idli"),
    dishes("Dosa"),
    dishes("Vada Paav"),
    dishes("Butten Paneer"),
    dishes("Butter Chicken"),
    dishes("Palak Paneer"),
    dishes("Biryani"),
    dishes("Gulab Jamun"),
    dishes("Rasgulla"),
    dishes("Jalebi"),
    dishes("Gajar Ka Halwa"),
    dishes("Kheer"),
    dishes("Kulfi"),
    dishes("Modak"),
    dishes("Samosa"),
    dishes("Kaju Katli"),
    dishes("Lassi")
]
        

order = []

            

def welcome_page():
    print(colored("\nWelcome to Foody World!", "yellow"))
    print(colored("1. Order Food", "green"))
    print(colored("2. View Our Restaurants", "red"))
    print(colored("3. Our Delivery Partners", "blue"))
    print(colored("Enter 0 at any point to return to this page.", "cyan"))

while True:
    welcome_page()
    boy_list = boy_LIST()
    RESTAURANT = restaurant()
    try:
        resp = int(input(colored("Enter Your Response, Sir: ","grey")))
    except:
        print(colored("Something Went Wrong","red"))
        continue
    print("\n")
    
    if resp<=-1 or resp>=4:
        print(colored("You Enter Wrong Number","red"))
        continue
    
    if resp==0:
        continue
    if resp==2:
        for i in range(len(RESTAURANT.items)):
            print(i+1, RESTAURANT.items[i].name)
            print("Rating: ",RESTAURANT.items[i].rating)
            
        print("Enter 0 for exit")
        
    if resp==3:
        for i in range(len(boy_list.items)):
            print(i+1, boy_list.items[i].name)
            print("Phone Number: ",boy_list.items[i].number)
    
    
    if resp==1:
        print(colored("Order Food","yellow"))
        username = input(colored("Enter Your Name: ","green"))
        print("Enter Your Location")
        print("Our service are limited to cordinates (15,0),(15,15), (-15,15), (-15,-15).\n Kindly Enter the cordinates within the range")
        try:
            user_x = int(input(colored("X Cordinate: ","grey")))
            user_y = int(input(colored("Y Cordinate: ","grey")))
        except:
            print(colored("You Enter Wrong Number","red"))
            continue
        print("\n")
        
        
        
        if not (-15 <= user_x <= 15) or not (-15 <= user_y <= 15):
            print("Sorry our service currently not available to you location")
        else: 
            print("Available Restaurants near You")
            k = 0
            choice = []
            for i in range(len(RESTAURANT.items)):
                dist = math.sqrt((user_x-RESTAURANT.items[i].X)*(user_x-RESTAURANT.items[i].X)+(user_y-RESTAURANT.items[i].Y)*(user_y-RESTAURANT.items[i].Y))
                if dist<=8:
                    k=k+1
                    choice.append(i)
                    print(k,RESTAURANT.items[i].name)
                    print("Rating",RESTAURANT.items[i].rating)
                
            try:
                reso_choice_= int(input(colored("Enter the restaurant number: ","grey")))
            except:
                print(colored("Something Went Wrong","red"))
                continue
            
            if reso_choice_>=k or reso_choice_<0:
                print(colored("You Enter Wrong Number","red"))
                continue
                
            reso_choice = int(choice[k-1])
            print("\n")
            
            print(RESTAURANT.items[reso_choice].name)
            print("Menu")
            
            menu = Menu()
            z = 1
            for i in menu.items:
                print(z, i.name)
                z = z+1
                
            try:
                food = int(input(colored("Enter Item Number: ","grey")))
            except:
                print(colored("Something Went Wrong","red"))
                continue
            
            if food>len(menu.items) or food<0:
                print(colored("You Enter Wrong Number","red"))
                continue
                
            print("\n")
            food_num = food-1 #index of ordered choice
            
            print("Order Type")
            print("0 Go back to home page")
            print("1. Priority Order")
            print("2. Non Priority Order")
            
            
            try:
                food_choice = int(input(colored("Enter Priority Number: ","grey")))
            except:
                print(colored("Something Went Wrong","red"))
                continue
            
            if food_choice>3 or food_choice<0:
                print(colored("You Enter Wrong Number","red"))
                continue
            
            print("\n")
            
            if food_choice==0:
                continue
            if food_choice==1:
                price = 100+10*len(menu.items[food_num].name)
            if food_choice==2:
                price = 10*len(menu.items[food_num].name)
            
                
            delievry_charge = dist*2+25
            final_price = price+delievry_charge
            
            try:
                phone_number = int(input(colored("Enter Your Phone Number: ","grey")))
            except:
                print(colored("Something Went Wrong","red"))
                continue
            
            if phone_number<0:
                print(colored("You Enter Wrong Number","red"))
                continue
            
            print("\n")
            
            print(colored("\nBill","yellow"))
            print(colored("STATUS: ","blue"),colored("ACCEPTED","green"))
            print(colored(f"Name: {username}","green"))
            print(colored(f"Phone Number: {phone_number}","green"))
            print(colored(f"Order: {menu.items[food_num].name}","green"))
            print(colored(f"Address Coordinates: X: {user_x} Y: {user_y}","green"))
            print(colored(f"Amount: {price}","green"))
            print(colored(f"Delievery Charge: {delievry_charge:.2f}","green"))
            print(colored(f"Total Payable Amount: {final_price:.2f}","green"))
            
            
            print(colored("Mode of Payment","yellow"))
            print("0. Go  back to home Page")
            print("1. COD (Cash of Delievery)")
            print("2. UPI")
            
            print("\n")
            try:
                payment_choice = int(input(colored("Enter Payment Choice Number: ","grey")))
            except:
                print(colored("Something Went Wrong","red"))
                continue
            
            if payment_choice<0 or payment_choice>2:
                print(colored("You Enter Wrong Number","red"))
                continue
            
            if payment_choice==0:
                continue
            if payment_choice==1:
                print("Cash of Delievery Confirmed")
            if payment_choice==2:
                print("Pay on UPI ID: someone@axl")
                
            
            print("\n")
            print("Thanks for Ordering food from Us")
            
            delievery_boy_dist = 100
            
            for i in range(len(boy_list.items)):
                boy_dist = math.sqrt((user_x-boy_list.items[i].X)*(user_x-boy_list.items[i].X)+(user_y-boy_list.items[i].Y)*(user_y-boy_list.items[i].Y))
                
                if boy_dist<=delievery_boy_dist:
                    delievry_partner = boy_list.items[i].name
                    delievery_boy_dist = boy_dist
                    
            
            
      
            food_made_time = datetime.now()
            ready_time = food_made_time + timedelta(minutes=5)
            out_for_delievry = ready_time + timedelta(minutes=5)
            delivered = out_for_delievry + timedelta(minutes=10)
            
      
            p = 0
            
            sorted_orders = sorted(order, key=lambda x: int(x['priority']), reverse=True)

          
            available_drivers = [driver for driver in boy_list.items if not any(
                o['Delievery_boy'] == driver.name and 
                int(o['delivered_min']) > datetime.now().minute 
                for o in sorted_orders
            )]

       
            if available_drivers:
                nearest_driver = min(
                    available_drivers,
                    key=lambda d: math.sqrt((user_x - d.X)**2 + (user_y - d.Y)**2)  # 🟢 dot notation for attributes
                )
                delivery_partner = nearest_driver.name
                delivery_boy_dist = math.sqrt((user_x - nearest_driver.X)**2 + (user_y - nearest_driver.Y)**2)

            
                if int(food_choice) == 1:
                    print("Status: BUSY")
                    print(colored(f"Priority delivery! {delivery_partner} is coming directly!", "red"))
                else:
                    print("Status: FREE")

                
              
                print(colored(f"Mr. {delivery_partner} is delivering your order. He is currently {delivery_boy_dist:.2f} meters away", "red"))
                
            else:
                print("All drivers busy. Your order will be assigned soon.")

                
            order.append({
                'UserName':f'{username}',
                'Phone Number': f'{phone_number}',
                'Order': f'{menu.items[food_num].name}',
                'X':f'{user_x}',
                'Y':f'{user_y}',
                'Delievery Charge': f'{delievry_charge}',
                'Total Payable Amount': f'{final_price}',
                'Delievery_boy': f'{delievry_partner}',
                'priority':f'{food_choice}',
                'delievred_hour':f'{delivered}'
                
           })
                 
            print(colored("0. For Home Page","red"))
            print(colored("1. VIEW STATUS OF YOU ORDER","yellow")) 
            
            try:
                status_choice = int(input("Enter Your Response: "))
            except:
                print(colored("Something Went Wrong","red"))
                continue
            
            if status_choice==0:
                continue
            if status_choice==1:
                print(colored("STATUS OF YOU ORDER","yellow"))
                print(colored("Ordered At: ","blue"),colored(f"{food_made_time}","green"))
                print(colored("Estimated Cooking Completion Time: ","blue"),colored(f"{ready_time}","green"))
                print(colored("Expected Dispatch Time: ","blue"),colored(f"{out_for_delievry}","green"))
                print(colored("Estimated Delivery Time: ","blue"),colored(f"{delivered}","green"))
                
            if status_choice>1 or status_choice<0:
                print(colored("You Enter Wrong Number","red"))
  
            
            print(colored("Thanks for Ordering from Us","green"))
                
