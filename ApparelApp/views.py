from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
import pymysql
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import datetime
import os

# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Initialize global variables with default values
username = ""
types = "-"
style = "-"
brand = "-"
cart = []

def TrackOrder(request):
    if request.method == 'GET':
        global username
        output = ''
        output+='<table border=1 align=center width=100%><tr><th>Purchaser Name</th><th>Product ID</th><th>Order Date</th><th>Purchaser Details</th>'
        output+='<th>Product Details</th><th>Amount</th><th>Card No</th></tr>'
        
        # Connect to database and fetch orders for the current user
        try:
            con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
            with con:
                cur = con.cursor()
                cur.execute("select * FROM customer_order WHERE purchaser_name='"+username+"'")
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        # Mask the card number for security
                        masked_card = row[6]
                        if len(masked_card) > 4:
                            masked_card = 'XXXX-XXXX-XXXX-' + masked_card[-4:]
                        
                        output+='<td><font size="" color="black">'+row[0]+'</td>'
                        output+='<td><font size="" color="black">'+row[1]+'</td>'
                        output+='<td><font size="" color="black">'+str(row[2])+'</td>'
                        output+='<td><font size="" color="black">'+row[3]+'</td>'
                        output+='<td><font size="" color="black">'+row[4]+'</td>'
                        output+='<td><font size="" color="black">'+str(row[5])+'</td>'
                        output+='<td><font size="" color="black">'+masked_card+'</td></tr>'
                else:
                    output+='<tr><td colspan="7" align="center"><font size="" color="black">No orders found for your account</font></td></tr>'
        except Exception as e:
            print("Database error:", e)
            output+='<tr><td colspan="7" align="center"><font size="" color="black">Error retrieving orders. Please try again later.</font></td></tr>'
            
        output +='</table><br><br/>'               
        context= {'data':output}
        return render(request, 'ProductList.html', context)

def ViewFeedback(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="3" color="black">Username</th><th><font size="3" color="black">Feedback</th><th><font size="3" color="black">Feedback Date</th></tr>'
        
        try:
            con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
            with con:
                cur = con.cursor()
                cur.execute("select * FROM feedback")
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        name = row[0]
                        feedback = row[1]
                        date = row[2]
                        output+='<tr><td><font size="3" color="black">'+name+'</td><td><font size="3" color="black">'+feedback+'</td><td><font size="3" color="black">'+str(date)+'</td></tr>'
                else:
                    output+='<tr><td colspan="3" align="center"><font size="3" color="black">No feedback data found</font></td></tr>'
        except Exception as e:
            print("Database error in ViewFeedback:", e)
            output+='<tr><td colspan="3" align="center"><font size="3" color="black">Error retrieving feedback: ' + str(e) + '</font></td></tr>'
            
        output +='</table><br><br/>'       
        context= {'data':output}
        return render(request, 'ViewOrders.html', context)

def FeedbackAction(request):
    if request.method == 'POST':
        global username
        feedback = request.POST.get('t1', False)
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO feedback(username, feedback, feedback_date) VALUES('"+username+"','"+feedback+"','"+str(current_time)+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            context= {'data':'Your feedback sent to admin for review'}
            return render(request, 'Feedback.html', context)
        else:
            context= {'data':'Error in accepting feedback'}
            return render(request, 'Feedback.html', context)
        
def Feedback(request):
    if request.method == 'GET':
       return render(request, 'Feedback.html', {})

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def Login(request):
    if request.method == 'GET':
       return render(request, 'Login.html', {})

def AdminLogin(request):
    if request.method == 'GET':
       return render(request, 'AdminLogin.html', {})    

def Register(request):
    if request.method == 'GET':
       return render(request, 'Register.html', {})   

def AddProduct(request):
    if request.method == 'GET':
       return render(request, 'AddProduct.html', {})
    
def ViewOrders(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th>Purchaser Name</th><th>Product ID</th><th>Order Date</th><th>Purchaser Details</th>'
        output+='<th>Product Details</th><th>Amount</th><th>Card No</th></tr>'
        
        try:
            con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
            with con:
                cur = con.cursor()
                cur.execute("select * FROM customer_order")
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        # Mask the card number for security
                        masked_card = row[6]
                        if len(masked_card) > 4:
                            masked_card = 'XXXX-XXXX-XXXX-' + masked_card[-4:]
                            
                        output+='<tr><td><font size="" color="black">'+row[0]+'</td>'
                        output+='<td><font size="" color="black">'+row[1]+'</td>'
                        output+='<td><font size="" color="black">'+str(row[2])+'</td>'
                        output+='<td><font size="" color="black">'+row[3]+'</td>'
                        output+='<td><font size="" color="black">'+row[4]+'</td>'
                        output+='<td><font size="" color="black">'+str(row[5])+'</td>'
                        output+='<td><font size="" color="black">'+masked_card+'</td></tr>'
                else:
                    output+='<tr><td colspan="7" align="center"><font size="" color="black">No orders found in the database</font></td></tr>'
        except Exception as e:
            print("Database error in ViewOrders:", e)
            output+='<tr><td colspan="7" align="center"><font size="" color="black">Error retrieving orders: ' + str(e) + '</font></td></tr>'
            
        output +='</table><br><br/>'               
        context= {'data':output}
        return render(request, 'ViewOrders.html', context)

def ItemSearch(request):
    if request.method == 'GET':
       return render(request, 'ItemSearch.html', {})

def About(request):
    if request.method == 'GET':
       return render(request, 'About.html', {})    

def getPurchaserDetails(name):
    address = ''
    contact = ''
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
    with con:
            cur = con.cursor()
            cur.execute("select address,contact FROM register where username='"+name+"'")
            rows = cur.fetchall()
            for row in rows:
                contact = row[1]
                address = row[0]
                break
    return contact,address        

def getProductDetails(pid):
    pname = ''
    cname = ''
    cost = ''
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
    with con:
            cur = con.cursor()
            cur.execute("select productname,cost FROM addproduct where productid='"+pid+"'")
            rows = cur.fetchall()
            for row in rows:
                pname = row[0]
                cost = str(row[1])
                break
    return pname,cost

def PaymentAction(request):
    if request.method == 'POST':
        global username, cart
        amount = request.POST.get('t1', False)
        card = request.POST.get('t2', False)
        cvv = request.POST.get('t3', False)
        
        # Validate credit card using Luhn algorithm
        def luhn_check(card_number):
            sum = 0
            is_even = False
            for i in range(len(card_number) - 1, -1, -1):
                digit = int(card_number[i])
                if is_even:
                    digit *= 2
                    if digit > 9:
                        digit -= 9
                sum += digit
                is_even = not is_even
            return sum % 10 == 0
        
        # Check if card number is valid
        if not luhn_check(card):
            context = {'data': 'Invalid card number. Please check and try again.'}
            return render(request, 'Purchase.html', context)
        
        # Check if CVV is valid (3 digits)
        if not cvv.isdigit() or len(cvv) != 3:
            context = {'data': 'Invalid CVV number. Please check and try again.'}
            return render(request, 'Purchase.html', context)
            
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        contact, address =  getPurchaserDetails(username)
        purchaser = "Phone : "+contact+" Address : "+address
        pids = ""
        products = ""
        for i in range(len(cart)):
            pids += cart[i]+", "
            pname,cost = getProductDetails(cart[i])
            products += pname+", "
        if len(products) > 0:
            products = products.strip()
            products = products[0:len(products)-1]
        if len(pids) > 0:
            pids = pids.strip()
            pids = products[0:len(pids)-1]    
        pids = pids.strip()
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO customer_order(purchaser_name,product_id,purchase_date,purchaser_details,product_details,amount,card_no,cvv_no) VALUES('"+username+"','"+pids+"','"+str(current_time)+"','"+purchaser+"','"+products+"','"+amount+"','"+card+"','"+cvv+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        cart.clear()
        if db_cursor.rowcount == 1:
            context= {'data':'Order Confirmed'}
            return render(request, 'UserScreen.html', context)
        else:
            context= {'data':'Error in confirming order'}
            return render(request, 'UserScreen.html', context)

def getCatalogue():
    global types, style, brand
    output = ''
    output+='<table border=1 align=center width=100%><tr><th>Product ID</th><th>Product Name</th><th>Product Type</th>'
    output+='<th>Product Style</th><th>Product Brand</th>'
    output+='<th>Cost</th><th>Description</th>'
    output+='<th>Image</th><th>Add To Cart</th><th>View Cart</th></tr>'
    
    try:
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
        query = "select * from addproduct"
        
        # Build the query with filters
        condition_added = False
        if types != '-':
            if not condition_added:
                query += " where "
            else:
                query += " and "
            query += "product_type = '"+types+"'"
            condition_added = True
            
        if style != '-':
            if not condition_added:
                query += " where "
            else:
                query += " and "
            query += "product_style = '"+style+"'"
            condition_added = True
            
        if brand != '-':
            if not condition_added:
                query += " where "
            else:
                query += " and "
            query += "product_brand = '"+brand+"'"
            condition_added = True
        
        print("Running query: " + query)
        with con:
            cur = con.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            print(f"Found {len(rows)} products")
            if rows:
                for row in rows:
                    output+='<tr>'  # Start a new row
                    output+='<td><font size="" color="black">'+str(row[0])+'</td>'
                    output+='<td><font size="" color="black">'+str(row[1])+'</td>'
                    output+='<td><font size="" color="black">'+row[2]+'</td>'
                    output+='<td><font size="" color="black">'+row[3]+'</td>'
                    output+='<td><font size="" color="black">'+row[4]+'</td>'
                    output+='<td><font size="" color="black">'+row[5]+'</td>'
                    output+='<td><font size="" color="black">'+row[6]+'</td>'
                    # Display the product image
                    output+='<td><img src="/static/products/'+row[7]+'" width="200" height="200" alt="Product Image"></td>'
                    output+='<td><a href=\'AddCart?pid='+str(row[0])+'\'><font size="" color="black">Add to Cart</a></td>'
                    output+='<td><a href=\'ViewCart?pid='+str(row[0])+'\'><font size="" color="black">View Cart</a></td></tr>'
            else:
                output+='<tr><td colspan="10" align="center"><font size="" color="black">No products found matching your criteria</font></td></tr>'
    except Exception as e:
        print("Database error in getCatalogue:", e)
        output+='<tr><td colspan="10" align="center"><font size="" color="black">Error loading products: ' + str(e) + '</font></td></tr>'
        
    output +='</table><br><br/><br/>'        
    return output

def AddCart(request):
    if request.method == 'GET':
        pid = request.GET.get('pid')
        global cart
        if pid not in cart:
            cart.append(pid)
            
        output = '<table border=1 align=center width=100%><tr><th>Product ID</th><th>Product Name</th><th>Image</th><th>Cost</th><th>Shopping Cart</th></tr>'
        try:
            con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
            with con:
                cur = con.cursor()
                cur.execute("select * from addproduct")
                rows = cur.fetchall()
                for row in rows:
                    # Format the cost value safely
                    cost_display = row[5]
                    try:
                        # Clean the cost value for display
                        cost_value = ''.join(c for c in str(row[5]) if c.isdigit() or c == '.')
                        if cost_value:
                            cost_display = f"${float(cost_value):.2f}"
                    except (ValueError, TypeError) as e:
                        print(f"Error formatting cost '{row[5]}': {e}")
                        # Use raw value if formatting fails
                    
                    pid = str(row[0])
                    output+='<tr><td><font size="" color="black">'+pid+'</td>'
                    output+='<td><font size="" color="black">'+row[1]+'</td>'
                    output+='<td><img src=/static/products/'+row[7]+' width=100 height=100></img></td>'
                    output+='<td><font size="" color="black">'+str(cost_display)+'</td>'
                    if pid not in cart:
                        output+='<td><a href=\'AddCart?pid='+pid+'\'><font size="" color="black">Add to Cart</a></td></tr>'
                    else:
                        output+='<td><font size="" color="black">Already in Cart</td></tr>'
        except Exception as e:
            print("Database error in AddCart:", e)
            output += '<tr><td colspan="5" align="center"><font size="" color="black">Error retrieving product catalog: ' + str(e) + '</font></td></tr>'
            
        output += '</table><br/><br/><center>'
        if len(cart) > 0:
            output += '<a href=\'ViewCart\'><font size="" color="black">View Your Cart</a><br><br/>'
            
        context = {'data': output}
        return render(request, 'ProductList.html', context)
        
def Checkout(request):
    if request.method == 'GET':
        global cart
        total = 0
        
        try:
            con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
            for pid in cart:
                with con:
                    cur = con.cursor()
                    cur.execute("select cost from addproduct where productid='"+pid+"'")
                    rows = cur.fetchall()
                    for row in rows:
                        try:
                            # Try to handle different formats of cost values
                            cost_value = row[0]
                            # Remove any non-numeric characters except decimal point
                            cost_value = ''.join(c for c in cost_value if c.isdigit() or c == '.')
                            if cost_value:  # Only try to convert if there's a value
                                total += float(cost_value)
                        except (ValueError, TypeError) as e:
                            print(f"Error converting cost '{row[0]}' to float: {e}")
                            # Continue with the next item instead of failing completely
        except Exception as e:
            print("Database error in Checkout:", e)
            # If there's an error, set a default value or show an error
            return render(request, 'UserScreen.html', {'data': 'Error calculating total: ' + str(e) + '. Please try again.'})
                    
        output = '<tr><td><font size="3" color="black">Total&nbsp;Amount</b></td><td><input type="text" name="t1" size="25" value="'+str(total)+'" readonly/></td></tr>'
        context= {'data1':output}
        return render(request, 'Purchase.html', context)

def ViewCart(request):
    if request.method == 'GET':
        global cart
        output = '<table border=1 align=center width=100%><tr><th>Product ID</th><th>Product Name</th><th>Cost</th><th>Remove Item</th></tr>'
        
        if len(cart) == 0:
            output += '<tr><td colspan="4" align="center"><font size="" color="black">Your cart is empty</font></td></tr>'
        else:
            try:
                con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
                for pid in cart:
                    with con:
                        cur = con.cursor()
                        cur.execute("select productname, cost from addproduct where productid='"+pid+"'")
                        rows = cur.fetchall()
                        for row in rows:
                            # Format the cost value safely
                            cost_display = row[1]
                            try:
                                # Clean the cost value for display
                                cost_value = ''.join(c for c in str(row[1]) if c.isdigit() or c == '.')
                                if cost_value:
                                    cost_display = f"${float(cost_value):.2f}"
                            except (ValueError, TypeError) as e:
                                print(f"Error formatting cost '{row[1]}': {e}")
                                # Use raw value if formatting fails
                                
                            output+='<tr><td><font size="" color="black">'+str(pid)+'</td>'
                            output+='<td><font size="" color="black">'+str(row[0])+'</td>'
                            output+='<td><font size="" color="black">'+str(cost_display)+'</td>'
                            output+='<td><a href=\'RemoveCart?pid='+str(pid)+'\'><font size="" color="black">Remove</a></td></tr>'
            except Exception as e:
                print("Database error in ViewCart:", e)
                output += '<tr><td colspan="4" align="center"><font size="" color="black">Error retrieving cart items: ' + str(e) + '</font></td></tr>'
        
        output +='</table><br><br/><center>'
        if len(cart) > 0:
            output += '<a href=\'Checkout?pid=0\'><font size="" color="black">Proceed to Checkout</a><br><br/>'
        context= {'data':output}
        return render(request, 'ProductList.html', context)

def RemoveCart(request):
    if request.method == 'GET':
        global cart
        pid = request.GET['pid']        
        cart.remove(pid)
        output = getCatalogue()  
        context= {'data':output}
        return render(request, 'ProductList.html', context)

def SearchItemData(request):
    if request.method == 'POST':
        global types, style, brand, cart
        #cart.clear()
        types = request.POST.get('t1', False)
        style = request.POST.get('t2', False)
        brand = request.POST.get('t3', False)
        output = getCatalogue()  
        context= {'data':output}
        return render(request, 'ProductList.html', context)

def AddProductData(request):
    if request.method == 'POST':
      pname = request.POST.get('t1', False)
      ptype = request.POST.get('t2', False)
      style = request.POST.get('t3', False)
      brand = request.POST.get('t4', False)
      cost = request.POST.get('t5', False)
      description = request.POST.get('t6', False)
      
      try:
          myfile = request.FILES['t7']
          
          # Get maximum product ID to assign a new one
          count = 0        
          con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
          with con:
              cur = con.cursor()
              cur.execute("select max(productid) FROM addproduct")
              rows = cur.fetchall()
              for row in rows:
                  if row[0] is not None:
                      count = int(row[0])
          
          # Increment ID or start from 1 if no products exist
          count = count + 1
          
          # Make sure the static products directory exists
          product_dir = os.path.join(BASE_DIR, 'ApparelApp', 'static', 'products')
          if not os.path.exists(product_dir):
              os.makedirs(product_dir)
              
          # Save image file
          fs = FileSystemStorage(location=product_dir)
          image_name = str(count) + '.png'
          filename = fs.save(image_name, myfile)

          # Insert product into database
          db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
          db_cursor = db_connection.cursor()
          student_sql_query = "INSERT INTO addproduct(productid,productname,product_type,product_style,product_brand,cost,description,image) VALUES('"+str(count)+"','"+pname+"','"+ptype+"','"+style+"','"+brand+"','"+cost+"','"+description+"','"+image_name+"')"
          db_cursor.execute(student_sql_query)
          db_connection.commit()
          print(db_cursor.rowcount, "Record Inserted")
          
          if db_cursor.rowcount == 1:
              context= {'data':'Product "'+pname+'" added successfully'}
              return render(request, 'AddProduct.html', context)
          else:
              context= {'data':'Error in adding product details'}
              return render(request, 'AddProduct.html', context)
          
      except Exception as e:
          print("Error in adding product:", e)
          context= {'data':'Error in adding product details: ' + str(e)}
          return render(request, 'AddProduct.html', context)

def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        contact = request.POST.get('contact', False)
        email = request.POST.get('email', False)
        address = request.POST.get('address', False)
        status = "none"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username FROM register where username='"+username+"'")
            rows = cur.fetchall()
            for row in rows:
                status = "exists"
        if status == "none":
            db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
            db_cursor = db_connection.cursor()
            student_sql_query = "INSERT INTO register(username,password,contact,email,address) VALUES('"+username+"','"+password+"','"+contact+"','"+email+"','"+address+"')"
            db_cursor.execute(student_sql_query)
            db_connection.commit()
            print(db_cursor.rowcount, "Record Inserted")
            if db_cursor.rowcount == 1:
                context= {'data':'Signup Process Completed'}
                return render(request, 'Register.html', context)
            else:
                context= {'data':'Error in signup process'}
                return render(request, 'Register.html', context)
        else:
            context= {'data':'Username already exists'}
            return render(request, 'Register.html', context) 
        
def UserLogin(request):
    if request.method == 'POST':
        global username
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        
        utype = 'none'
        try:
            con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'password@1234', database = 'ApparelApp',charset='utf8')
            with con:
                cur = con.cursor()
                cur.execute("select * FROM register WHERE username='"+username+"' AND password='"+password+"'")
                rows = cur.fetchall()
                if rows:
                    utype = "success"
        except Exception as e:
            print("Database error:", e)
            context= {'data':'Database connection error. Please try again later.'}
            return render(request, 'Login.html', context)
                
        if utype == 'success':
            context= {'data':'Welcome '+username}
            return render(request, 'UserScreen.html', context)
        else:
            context= {'data':'Invalid username or password'}
            return render(request, 'Login.html', context)

def AdminLoginAction(request):
    if request.method == 'POST':
        global username
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        
        # Keep the admin login check
        if username == 'admin' and password == 'admin':
            context= {'data':'welcome '+username}
            return render(request, 'AdminScreen.html', context)
        else:
            context= {'data':'Invalid login details'}
            return render(request, 'AdminLogin.html', context)

def TestStatic(request):
    if request.method == 'GET':
        return render(request, 'test_static.html', {})


        
